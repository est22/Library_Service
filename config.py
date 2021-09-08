import os

BASE_DIR = os.path.dirname(__file__)
# db 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'user.db'))
# SQLAlchemy 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

