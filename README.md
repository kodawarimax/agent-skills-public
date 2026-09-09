# Agent Skills Starter Pack

Claude Code / Codex向けのエージェントスキル集です。

## 収録内容

| 動画の分類 | このリポジトリのスキル |
|---|---|
| メモ | `obsidian-auto-capture` |
| 自然な日本語 | `japanese-native-voice` |
| デザインシステム | `apple-design` |
| スキル検索 | `skill-search` |
| スライド | `slide-generator` |
| クラウド公開 | `cloud-publish` |
| 画像生成 | `image-generation` |
| 動画生成 | `video-generation` |
| 図解生成 | `diagram-generation` |
| テロップ | `video-captioning` |
| 動画からSkill/Prompt | `video-to-skill` |

## 公開版について

このリポジトリは、個人情報・秘密情報・内部パス・特定組織の固有設定を含まない汎用版です。利用環境に合わせて、保存先・フック・API・ブランドルールを設定してください。

外部API、デプロイ、課金、公開操作は各スキルの人間承認ルールに従います。

## 動画からSkill/Prompt

`video-to-skill` は、YouTubeまたはローカル動画を字幕・音声・キーフレームから分析し、証拠付きのAgent Skillへ変換します。拡張版では、手順Skillに加えて、入力・出力契約・停止条件・根拠タイムスタンプを持つ再利用可能なPromptも `prompts/` に生成できます。

Prompt出力は秘密情報、動画由来のPrompt Injection、危険な取得・実行コマンドを検査してから利用します。上流の `brenoepics/video-to-skill` を基礎にした改良版で、詳細は [`skills/video-to-skill/README.md`](skills/video-to-skill/README.md) を参照してください。
