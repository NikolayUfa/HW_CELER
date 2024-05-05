import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../../../../Documents/Netologia/HW_CELERY/app/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


SALT = b'MY_super_salt_982347jwhfiwu3rociI^%FK@%'
