#!/usr/bin/env bash
set -euo pipefail

file="\${1:-}"
if [[ -z "\$file" || ! -f "\$file" ]]; then
  printf 'usage: %s VIDEO_FILE\n' "\$0" >&2
  exit 2
fi
command -v ffprobe >/dev/null || { printf 'ffprobe is required\n' >&2; exit 2; }

duration="\$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "\$file")"
video="\$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of default=nw=1 "\$file")"
audio="\$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate -of default=nw=1 "\$file" || true)"

printf 'file=%s\nduration=%s\n[video]\n%s\n[audio]\n%s\n' "\$file" "\$duration" "\$video" "\${audio:-none}"
