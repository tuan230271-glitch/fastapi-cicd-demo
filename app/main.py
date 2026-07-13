
from fastapi import FastAPI, HTTPException
# Khởi tạo ứng dụng. title/version hiển thị trong trang docs tự sinh.
app = FastAPI(title="CI/CD Demo App", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello DevOps! App đang chạy."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/add")
def add(a: float, b: float):
    return {"a": a, "b": b, "result": a + b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Không thể chia cho 0")
    return {"a": a, "b": b, "result": a / b}