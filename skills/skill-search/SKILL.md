---
name: skill-search
description: >-
  Search the local agent skill library and recommend the smallest reusable skill
  for a task. Use whenever the user asks which skill to use, has many skills,
  or wants to find, organize, or invoke an existing skill.
---

# Local Skill Search

依頼内容を短く分解し、まず現在のエージェント環境で利用可能なスキル一覧を検索する。
新設を勧める前に、完全一致・部分一致・組み合わせの順で候補を確認する。

## 動画で紹介された10種の対応表

| 目的 | 使用スキル |
|---|---|
| メモ | `obsidian-auto-capture` |
| 自然な日本語 | `japanese-native-voice` |
| デザイン | `apple-design` |
| スキル検索 | `skill-search` |
| スライド | `slide_generator` |
| クラウド公開 | `cloud-publish` |
| 画像生成 | `imagegen` |
| 動画生成 | `video-generation` |
| 図解生成 | `diagram-generation` |
| テロップ | `video-captioning` |

`slide_generator` は `.agents/skills` 配下、`imagegen` はシステム標準スキルとして提供される場合がある。

## 出力

1. 推奨スキル（最大3件）と用途
2. 既存スキルで足りるか
3. 足りない場合だけ、最小の新設案

スキルのインストール、変更、外部送信はユーザーの明示承認なしに行わない。
