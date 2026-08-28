---
name: image-generation
description: >-
  Generate original images for slides, websites, diagrams, and video assets.
  Use whenever the user asks for an image, illustration, visual asset, or
  generated background. Delegate to the platform imagegen skill when available.
---

# Image Generation

用途、サイズ、画風、透明背景、文字入れの有無を確認し、オリジナル素材として生成する。
既存ブランドや人物を含む場合は利用権と公開範囲を確認する。

標準の `imagegen` が利用できる場合はそれを使う。外部APIを使う場合は、送信データ・費用・保存先を示し、承認を得てから実行する。

生成物は原本を保持し、用途別の書き出しとライセンス情報を記録する。

## 90点運用

生成前に、用途・対象者・サイズ・主役・構図・雰囲気・文字・禁止事項を短い仕様に固定する。原則として構図違いを3案作り、要件適合20点、見た目20点、一貫性15点、技術品質15点、文字10点、展開性10点、原本・権利・再現性10点で比較する。

最高点の案を1点だけ修正して再確認する。画像内の長い文字、価格、ボタン、字幕は生成画像に埋め込まず、HTML/CSS/SVG等の編集可能なレイヤーに分離する。最終素材は、用途・採用理由・プロンプト・参照画像の役割・権利状態を記録する。
