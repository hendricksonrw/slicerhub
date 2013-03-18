from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "base_blog"}
app.config["SECRET_KEY"] = "base_pass"

db = MongoEngine(app)

def register_blueprints(app):
    from blogapp.views import posts
    from blogapp.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
