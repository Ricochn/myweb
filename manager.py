from app import create_app, db
from app.model import Article
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import pymysql
pymysql.install_as_MySQLdb()

app = create_app('default')
manage = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, Article=Article)
manage.add_command("shell", Shell(make_context=make_shell_context))
manage.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manage.run()
