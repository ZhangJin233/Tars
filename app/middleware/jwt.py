from datetime import timedelta, datetime
import jwt
from jwt.exceptions import ExpiredSignatureError
import hashlib

EXPIRED_HOUR = 3

class UserToken(object):
    key = 'tarsToken'
    salt = 'tars'

    @staticmethod
    def get_token(data):
        payload = dict({'exp': datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)}, **data)
        
        return jwt.encode(payload, key=UserToken.key, algorithm='HS256').decode('utf-8')

    @staticmethod
    def parse_token(token):
        try:
            payload = jwt.decode(token,key = UserToken.key, algorithm=['HS256'])
            return payload
        except ExpiredSignatureError as error:
            print(f'Unable to decode the token, error: {error}')

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        bt = f'{password}{UserToken.salt}'.encode('utf-8')
        m.update(bt)
        return m.hexdigest()


