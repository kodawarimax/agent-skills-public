---
name: obsidian-auto-capture
description: >
  Obsidian Vault に学習内容を自動保存し、必要な範囲で共有するスキル。
  一定条件（30分経過/wiki書き込み/重要決定/TIL検出/新プロセス学習）で自動発火。
  Obsidianネイティブ形式（YAML frontmatter/タグ/バックリンク/dataview）で構造化し、
  任意の索引タグで検索可能なナレッジとして整理する。
  発動キーワード: 「保存して」「覚えて」「TIL」「wikiに追加」「Obsidianに保存」「学習した」「プレイブック」「ナレッジ保存」「remember」
allowed-tools: bash:* write:*
---

# obsidian-auto-capture — Obsidian Vault 自動知識保存スキル

セッション中に学習した知識・決定・プロセスを Obsidian ネイティブ形式で Vault に保存し、
索引タグを付与して、後から検索・再利用しやすい形で保存するスキル。

## 自動発火条件

以下のいずれかを検知したら、ユーザーへの確認なしで即座に発火する:

| 条件 | 検知方法 |
|---|---|
| 「保存して」「覚えて」「TIL」「remember」キーワード | ユーザー発言 |
| 新しいプロセス・playbook を学習した | AI が判断 |
| 重要な意思決定（ADR/方針確定）が発生 | AI が判断 |
| wiki/ 配下に新規ファイルを書いた直後 | PostToolUse フック経由 |
| セッション開始から 30 分以上経過 | Stop フック経由 |

## Obsidian 保存フォーマット (MANDATORY)

保存するすべての wiki ファイルは以下の YAML frontmatter を持つこと:

```yaml
---
title: "ナレッジタイトル"
date: YYYY-MM-DD
type: playbook | case | concept | entity | strategy | ADR
tags:
  - knowledge-index
  - relevant-tag-1
  - relevant-tag-2
aliases: ["別名1", "別名2"]
source_session: "YYYY-MM-DD セッション概要"
related:
  - "[[関連エンティティ1]]"
  - "[[関連エンティティ2]]"
status: active | draft | deprecated
---
```

### type 別の保存先

| type | 保存先 | 用途 |
|---|---|---|
| `playbook` | `wiki/playbooks/` | 再現可能な手順・SOP |
| `case` | `wiki/cases/` | 事例・成功/失敗パターン |
| `concept` | `wiki/concepts/` | 理論・フレームワーク |
| `entity` | `wiki/entities/` | 人物・組織・システム定義 |
| `strategy` | `wiki/strategies/` | 戦略・ロードマップ |
| `ADR` | `wiki/playbooks/decisions/` | 意思決定記録 |

## 実行フロー

### Step 1: 知識の種類を判定

保存する内容を分類する:
- **再現可能な手順** → `playbook`
- **このセッションで起きた特定の事例** → `case`
- **概念・理論の理解** → `concept`
- **新しいエンティティ（人/組織/システム）** → `entity`
- **戦略・方針の確定** → `strategy`
- **意思決定** → `ADR`

### Step 2: Obsidian ファイルを生成

ファイル名規則: `YYYY-MM-DD_<kebab-case-title>.md`

バックリンクを積極的に使う:
- 関連エンティティは `[[エンティティ名]]` 形式で記述
- 既存 wiki ファイルとの接続を意識する
- Dataview クエリを body に含める（type=playbook の場合）

実際のファイル書き込みは Write ツールで直接実行する:
```bash
# ファイルパス例
<vault>/wiki/playbooks/YYYY-MM-DD_example.md
```

### Step 3: 索引タグを付与

`tags:` にプロジェクトで定めた索引タグ（例: `knowledge-index`）を含める。
利用環境に共有フックがある場合のみ、そのフックの仕様に従う。

### Step 4: 保存完了を報告

```
✅ Obsidian に保存しました
  - ファイル: wiki/playbooks/2026-05-30_example.md
  - タイプ: playbook
  - タグ: #knowledge-index #skill-management
  - バックリンク: [[polyskill]], [[workflow-runner]]
  - 共有: 利用環境の共有フック設定に従う
```

## Dataview クエリのテンプレート (playbook 必須)

playbook ファイルには末尾に以下を追加する（Obsidian で活きる）:

```dataview
LIST
FROM #knowledge-index
WHERE contains(related, this.file.link)
SORT date DESC
```

## このセッションで保存すべき知識の検出ルール

以下のパターンを含む会話が発生した場合、即座に wiki 保存を実行する:

1. **新しいツール・スキルの使い方を学んだ** → `playbook`
2. **バグの根本原因と修正パターンを発見** → `playbook` (mistakes/ サブディレクトリ)
3. **ADR 番号が言及された** → `ADR`
4. **「〜が確定した」「〜に決めた」** → `strategy` or `ADR`
5. **新しいエージェント・システムが追加された** → `entity`
6. **失敗事例・教訓が明確になった** → `case`

## ファイルパス

- Vault ルート: 利用環境の Obsidian Vault
- 共有索引: 利用環境で定義した索引ファイルまたはデータベース
- フック: 利用環境で設定した保存・共有フック
