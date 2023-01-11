from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from team_bc import config
from flask_session import Session


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

sess = Session()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    db.init_app(app)
    sess.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        migrate.init_app(app, db)
        CORS(app, supports_credentials=True)
        from team_bc.views import api
        from team_bc.views import question_view
        app.register_blueprint(api.bp)
        app.register_blueprint(question_view.bp)
    return app
