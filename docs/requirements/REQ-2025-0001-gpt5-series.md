# REQ-2025-0001: GPT-5 系列対応（gpt-5 / gpt-5-mini / gpt-5-nano）

## 1. 要件定義（REQUIREMENT_GATHER_SINGLE）
【入力データ】
- 要望ID: REQ-2025-0001
- タイトル: GPT-5 系列対応
- 概要: OpenAI の GPT-5 系列（gpt-5 / gpt-5-mini / gpt-5-nano）をCLIの選択肢に追加し、既存フローで安定動作させる。

【静的解析による影響箇所（推定）】
- 画面/CLI: cli/utils.py（モデル選択肢）, cli/main.py（説明表示）
- クラス/メソッド: tradingagents/graph/trading_graph.py（モデル名伝播）, tradingagents/default_config.py（既定モデル可変化）, tradingagents/dataflows/interface.py（OpenAI互換確認）
- DB: なし

【要件ジャッジ】
- やるべきか？: Yes
- 優先度: 高
- 影響範囲メモ: モデル選択肢とモデル名受け渡し
- 判断理由/追加ヒアリング事項: 既存OpenAI互換のため実装リスク低。コスト上限/既定モデルの希望有無を確認。

## 2. 詳細設計  方針作成（DETAIL_POLICY）
- 変更対象
  - cli/utils.py / get_llm_provider_and_models: OpenAIのモデル候補に gpt-5 / gpt-5-mini / gpt-5-nano を追加
  - tradingagents/default_config.py: deep_think_llm/quick_think_llmにGPT-5系を設定可能に
  - tradingagents/graph/trading_graph.py: 渡されたモデル名をそのまま利用（現状互換）
  - tradingagents/dataflows/interface.py: モデル指定の透過性を確認（変更最小）
- データ設計: 変更なし
- 画面設計: モデル候補と説明文の追記
- ヒアリング依頼: 既定モデル/上限トークン/コスト上限の希望

## 3. レビュー＆ブラッシュアップ（REVIEW_PACKET）
- フロー（mermaid）
`mermaid
flowchart TD
  A[CLIでGPT-5系選択] --> B[Configへ反映]
  B --> C[LangChain/Clientへモデル名伝播]
  C --> D[各エージェント推論]
  D --> E[レポート生成/保存]
`
- 工数見積: 実装0.5d + 調整/テスト0.5d = 合計1.0人日
- 段階的更新: 候補追加既定設定動作確認回帰
- 未確定事項: 既定モデル/コスト上限

## 4. ドキュメントアウトプット（FINAL_DOC）
- 要件ジャッジ: Yes / 高
- 変更対象一覧: 上記
- リスク/対応: 互換APIで低リスク、ロールバックはブランチで担保
