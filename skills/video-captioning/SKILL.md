---
name: video-captioning
description: >-
  Transcribe audio and create, correct, style, or burn captions into a video.
  Use whenever the user asks for subtitles, captions, telops, SRT/VTT, or text
  overlays on video.
---

# Video Captioning

元動画を上書きせず、音声認識→字幕整形→確認→書き出しを分離する。
固有名詞・数字・タイミングは機械認識を鵜呑みにせず確認する。

## 手順

1. 元動画のコピーまたはハッシュを保持する。
2. 利用可能なローカルSTTを優先し、SRTまたはVTTを生成する。
3. 話者の意図を変えない範囲で誤字、改行、読速、表示時間を整える。
4. 字幕ファイル単体を確認してから、必要な場合だけ動画へ焼き込む。
5. 出力動画の再生、字幕表示、音ズレ、元動画非破壊を確認する。

外部STTや有料APIに音声を送る場合は、送信先とデータ範囲を先に示して承認を得る。
