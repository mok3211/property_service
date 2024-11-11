from ..main import app

@app.post("/login")
def login():
    # 登陆信息
    return {"success": "ok"}

@app.post("/register")
def register():
    
    # 注册信息
    return {"success": "ok"}

@app.post("/change_password")
def change_password():
    return {"success": "ok"}