from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    """
    サーバーの稼働確認と、学習の進捗を表示するエンドポイント
    """
    return {
        "status": "Success",
        "message": "Cloud Infrastructure Engineer in the making!",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ローカルでの実行用（python main.py で起動）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)