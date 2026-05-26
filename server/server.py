from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

app = FastAPI()
SECRET_KEY = "my-secret-key-123456"
ALGORITHM = "HS256"

# 登录请求结构体
class LoginRequest(BaseModel):
    username: str
    password: str

# 登录接口
@app.post("/login")
def login(req: LoginRequest):
    username = req.username
    password = req.password
    if username == "admin" and password == "123456":
        expire = datetime.utcnow() + timedelta(minutes=30)
        token = jwt.encode(
            {"sub": username, "exp": expire},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        return {"token": token}
    raise HTTPException(status_code=401, detail="账号密码错误")

# 需要Token鉴权的用户信息接口
@app.get("/user/info")
def user_info(authorization: str = None):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"username": payload["sub"], "msg": "用户信息正常"}
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", reload=True)