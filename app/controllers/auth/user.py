from flask import Blueprint, request
from flask import jsonify
from app.dao.auth.user_dao import UserDao
from app.handle.factory import ResponseFactory
from app.middleware.jwt import UserToken

auth = Blueprint('auth',__name__,url_prefix='/auth')

@auth.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=400, msg="用户名或密码不能为空"))
    email, name = data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(code=402, msg="姓名或邮箱不能为空"))
    err = UserDao.register_user(username, name, password, email)
    if err is not None:
        return jsonify(dict(code=500, msg=err))
    return jsonify(dict(code=200, msg="注册成功"))

@auth.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=400, msg="用户名或密码不能为空"))
    user,err = UserDao.login(username, password)
    if err is not None:
        return jsonify(dict(code=500, msg=err))
    user = ResponseFactory.model_to_dict(user,'password')
    token = UserToken.get_token(user)
    return jsonify(dict(code=200, msg='登录成功',data = dict(user=user, token=token)))
