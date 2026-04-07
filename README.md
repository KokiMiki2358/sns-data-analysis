# SNS Data Analysis

## 現在のステータス
FastAPIを用いたWebサーバーの基本構築が完了。ローカル環境での正常動作（Successレスポンス）を確認済み。

## 次のステップ
この基盤をベースに、SNSのデータ分析ロジックの実装と、AWSへのデプロイを計画中。

## 実行方法
```bash
$ pip install fastapi uvicorn
$ python main.py

※ http://127.0.0.1:8000 で疎通確認済み。

技術選定
FastAPI: 高速かつモダンなPython用Webフレームワーク。

選定理由: 将来的なデータ分析APIへの拡張性と、型安全な開発を重視したため。