from datetime import timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from models.Tokens import Token
from service.user_service import UserService
from utils.token_utils import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user
from ..main import app
from pydantic import BaseModel, ValidationError
from typing import List, Union


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    # 登陆信息
    user = UserService().authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
    

@app.post("/register")
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    # 注册信息
    user_service = UserService()
    user = user_service.create_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="User registration failed")
    return {"success": "User registered successfully"}

@app.post("/change_password")
def change_password(form_data: OAuth2PasswordRequestForm = Depends(get_current_user)):
     # 修改密码信息
    user_service = UserService()
    user = user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # 假设我们有一个方法来更新用户密码
    user_service.update_password(user, form_data.password)  # 这里需要传入新密码
    return {"success": "Password changed successfully"}

@app.post("/forgot_password")
async def forgot_password(email: str):
    # 处理忘记密码请求
    user_service = UserService()
    user = user_service.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 假设我们有一个方法来发送重置密码的电子邮件
    user_service.send_password_reset_email(user)
    return {"success": "Password reset email sent"}

@app.post("/reset_password")
async def reset_password(new_password: str, user: OAuth2PasswordRequestForm = Depends(get_current_user)):
    # 处理重置密码请求
    user_service = UserService()
    # 更新用户密码
    user_service.update_password(user, new_password)
    return {"success": "Password has been reset successfully"}