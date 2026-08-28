---
name: cloud-publish
description: >-
  Prepare a website, HTML slide, web tool, manual, or game for cloud hosting.
  Use whenever the user asks to deploy, publish, upload, release, or put a local
  artifact on a cloud server or public URL.
---

# Cloud Publish

公開前に成果物、ビルド、対象サービス、ドメイン、公開範囲を確認する。
まずローカル検証とプレビューを行い、公開操作は明示的な人間承認まで保留する。

## 手順

1. 成果物のパスと固定SHAを記録する。
2. 本番相当のビルド・最小スモーク・秘密情報混入チェックを行う。
3. 公開先と変更内容を短く提示する。
4. 明示承認後だけ、プロジェクト指定の deploy.sh など正規経路を使う。
5. 完了時は SHA・デプロイログ・実URLのスモーク結果を分けて報告する。

承認なしの外部公開、秘密情報の出力、仮URLを本番証拠として扱うことを禁止する。
