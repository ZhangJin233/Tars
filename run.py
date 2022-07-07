from app import tars
from app.utils.log import Log
from datetime import datetime
from app.controllers.auth.user import auth
from app import dao

tars.register_blueprint(auth)

@tars.route('/')
def hello_word():
    log = Log('hello word log')
    log.info('有人访问啦')
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    print(now)
    return now

if __name__ == '__main__':
    tars.run("0.0.0.0",threaded = True,debug=True)