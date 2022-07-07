from flask import Blueprint, request
from flask import jsonify
from app.dao.auth.user_dao import UserDao

auth = Blueprint('auth',__name__,url_prefix='/auth')

@auth.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=404, msg="用户名或密码不能为空"))
    email, name = data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(code=404, msg="姓名或邮箱不能为空"))
    err = UserDao.register_user(username, name, password, email)
    if err is not None:
        return jsonify(dict(code=500, msg=err))
    return jsonify(dict(code=200, msg="注册成功"))
