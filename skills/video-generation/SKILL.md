---
name: video-generation
description: >-
  Create short videos or motion assets from a script, storyboard, slide, or
  diagram. Use whenever the user asks for a generated video, motion explainer,
  YouTube material, or animated visual.
---

# Video Generation

目的、尺、画角、字幕、音声、納品形式を整理し、最小の生成経路を選ぶ。
外部APIや有料サービスは、利用先・費用・入力データを示して承認を得るまで呼び出さない。

## 既定の流れ

1. 台本をシーン表にする（秒数、画、音、テロップ）。
2. まずHTML/CSS/SVGまたは既存素材でプレビューを作る。
3. 生成APIが必要な場合だけ、候補と概算費用を提示する。
4. 元素材を保持したままMP4/WebM等へ書き出し、再生・尺・音ズレを確認する。

説明動画は、複雑な生成より再編集しやすいHTML/SVGを優先する。
