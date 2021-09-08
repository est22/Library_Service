from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    import models

    # 블루프린트
    from views import main_views
    app.register_blueprint(main_views.bp)


    return app

# import pymysql
# from flask import *
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from user_api import user
# from db_connect import db
# from flask_bcrypt import Bcrypt

# import config

# db = SQLAlchemy()
# migrate = Migrate()

# # 추가
# # app.secret_key = ''
# # app.config['SESSION_TYPE'] = 'filesystem'


# # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:devpass@127.0.0.1:3306/LibraryData"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)

#     # ORM
#     db.init_app(app)
#     migrate.init_app(app, db)
#     bcrypt = Bcrypt(app) # 추가
#     from . import models

#     # 블루프린트
#     from views import main_views
#     app.register_blueprint(user)
#     app.register_blueprint(book)

#     return app
    
# # app = Flask(__name__)
# # app.register_blueprint(user)
# # app.register_blueprint(book)
# # app.secret_key = ''
# # app.config['SESSION_TYPE'] = 'filesystem'


# # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:devpass@127.0.0.1:3306/LibraryData"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# # db.init_app(app)
# # bcrypt = Bcrypt(app)

# @app.route("/")
# def home():
#     if session.get('logged_in'):
#         return render_template('loggedin.html')
#     else:
#         return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)