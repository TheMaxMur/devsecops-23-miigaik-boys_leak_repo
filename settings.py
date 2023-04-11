import pathlib
from os import getenv

class DevConfig:
    SECRET_KEY='dev'
    PASSWORD_SALT = 'dev'
    DATABASE_PATH=pathlib.Path('instance', 'devel.db')
    SQLALCHEMY_DATABASE_URI='sqlite:///' + str(DATABASE_PATH.resolve())

    PATHS = {
        'user_md_files': pathlib.Path('user_md_files'),
        'user_documents': pathlib.Path('user_documents'),
        'user_images': pathlib.Path('user_images'),
    }

    ADMIN = {
        'username': 'admin',
        'password': 'admin',
        'email': 'admin@admin.com'
    }
    
    ROLES = [
        'admin',
        'user'
    ]

class ProdConfig:
    SECRET_KEY=getenv('SECRET_KEY')
    PASSWORD_SALT = getenv('PASSWORD_SALT')
    SQLALCHEMY_DATABASE_URI=getenv('DB_URI')

    PATHS = {
        'user_md_files': pathlib.Path('user_md_files'),
        'user_documents': pathlib.Path('user_documents'),
        'user_images': pathlib.Path('user_images'),
    }

    ADMIN = {
        'username': getenv('ADMIN_USERNAME'),
        'password': getenv('ADMIN_PASSWORD'),
        'email': 'admin@admin.com'
    }
    
    ROLES = [
        'admin',
        'user'
    ]