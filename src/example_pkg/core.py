import json
from uvicorn import run
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# 设置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# 定义一个路由
@app.get("/")
def index():
    response = Response(content=json.dumps({"message": "Hello, world!"}))
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    return response

# 定义一个路由，接受一个 User 对象作为请求体
@app.post("/user")
def create_user(user: User):
    if user is not None:
        response = Response(content=json.dumps(user.dict()))
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200
        return response
    else:
        raise HTTPException(status_code=400, detail="用户信息不能为空")

# 启动 app
if __name__ == "__main__":
    run(app, host="0.0.0.0", port=80, reload=True)
