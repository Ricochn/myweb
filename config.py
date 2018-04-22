import os
password = os.environ.get("dbpassword")
class Config:
    SECRET_KEY = "whatthefuck???"
    SQLALCHEMY_DATABASE_URI = "mysql://root:"+str(password)+"@localhost/myweb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_POSTS_PER_PAGE = 5
    Debug=True
    @staticmethod
    def init_app(app):
        pass

config = {
    'default':Config
}
