#!/usr/bin/env python3
"""Fetch a public X/Twitter status with yt-dlp and write local summaries."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STATUS_RE = re.compile(r"(?:x|twitter)\.com/[^/]+/status/(\d+)")


def run(cmd: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def find_downloader() -> list[str]:
    if shutil.which("yt-dlp"):
        return ["yt-dlp"]
    probe = run([sys.executable, "-m", "yt_dlp", "--version"])
    if probe.returncode == 0:
        return [sys.executable, "-m", "yt_dlp"]
    raise SystemExit("yt-dlp was not found. Install yt-dlp or make python -m yt_dlp available.")


def status_id_from_url(url: str) -> str:
    match = STATUS_RE.search(url)
    if not match:
        raise SystemExit(f"Could not find a status id in URL: {url}")
    return match.group(1)


def ffprobe(path: Path) -> dict[str, Any] | None:
    if not shutil.which("ffprobe"):
        return None
    proc = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,format_name",
            "-show_entries",
            "stream=index,codec_type,codec_name,width,height,avg_frame_rate",
            "-of",
            "json",
            str(path),
        ]
    )
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def first_file(directory: Path, pattern: str) -> Path | None:
    files = sorted(directory.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def load_info(directory: Path) -> dict[str, Any]:
    info_path = first_file(directory, "*.info.json")
    if not info_path:
        raise SystemExit("yt-dlp did not produce an .info.json file.")
    return json.loads(info_path.read_text(encoding="utf-8"))


def iso_from_timestamp(value: Any) -> str | None:
    if not isinstance(value, (int, float)):
        return None
    return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()


def write_outputs(directory: Path, url: str, info: dict[str, Any]) -> None:
    video = first_file(directory, "*.mp4") or first_file(directory, "*.mkv") or first_file(directory, "*.webm")
    thumbnail = first_file(directory, "*.jpg") or first_file(directory, "*.png") or first_file(directory, "*.webp")
    info_file = first_file(directory, "*.info.json")
    probe = ffprobe(video) if video else None

    summary = {
        "source_url": url,
        "status_id": status_id_from_url(url),
        "media_id": info.get("id"),
        "title": info.get("title"),
        "description": info.get("description"),
        "uploader": info.get("uploader"),
        "uploader_id": info.get("uploader_id"),
        "uploader_url": info.get("uploader_url"),
        "upload_date": info.get("upload_date"),
        "timestamp_utc": iso_from_timestamp(info.get("timestamp")),
        "duration": info.get("duration"),
        "like_count": info.get("like_count"),
        "repost_count": info.get("repost_count"),
        "comment_count": info.get("comment_count"),
        "webpage_url": info.get("webpage_url"),
        "video_path": str(video) if video else None,
        "thumbnail_path": str(thumbnail) if thumbnail else None,
        "info_json_path": str(info_file) if info_file else None,
        "ffprobe": probe,
    }
    (directory / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# X投稿取得サマリー",
        "",
        f"- 投稿URL: {url}",
        f"- 投稿者: {info.get('uploader')} (@{info.get('uploader_id')})",
        f"- 投稿日: {info.get('upload_date')} / {summary['timestamp_utc']}",
        f"- 本文: {info.get('description') or info.get('title')}",
        f"- 動画: {video if video else 'なし'}",
        f"- サムネ: {thumbnail if thumbnail else 'なし'}",
        f"- メタデータ: {info_file if info_file else 'なし'}",
        f"- duration: {info.get('duration')}",
        f"- like/repost/comment: {info.get('like_count')} / {info.get('repost_count')} / {info.get('comment_count')}",
    ]
    if probe:
        streams = probe.get("streams") or []
        video_stream = next((s for s in streams if s.get("codec_type") == "video"), {})
        fmt = probe.get("format") or {}
        lines.extend(
            [
                f"- ffprobe video: {video_stream.get('width')}x{video_stream.get('height')} {video_stream.get('codec_name')} {video_stream.get('avg_frame_rate')}",
                f"- ffprobe format: {fmt.get('format_name')} duration={fmt.get('duration')} size={fmt.get('size')}",
            ]
        )
    lines.append("")
    (directory / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a public X/Twitter status with yt-dlp.")
    parser.add_argument("url", help="x.com/twitter.com status URL")
    parser.add_argument("--out", default="tmp/x-post-fetch", help="Base output directory")
    parser.add_argument("--cookies", help="Optional cookies.txt path, only when user explicitly provided it")
    parser.add_argument("--keep", action="store_true", help="Keep intermediate yt-dlp files")
    args = parser.parse_args()

    sid = status_id_from_url(args.url)
    out_dir = Path(args.out) / sid
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        *find_downloader(),
        "--write-info-json",
        "--write-thumbnail",
        "--no-playlist",
        "-o",
        str(out_dir / "%(id)s.%(ext)s"),
    ]
    if args.keep:
        cmd.append("--keep-video")
    if args.cookies:
        cmd.extend(["--cookies", args.cookies])
    cmd.append(args.url)

    proc = run(cmd)
    (out_dir / "yt-dlp.log").write_text(proc.stdout, encoding="utf-8")
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    info = load_info(out_dir)
    write_outputs(out_dir, args.url, info)
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
