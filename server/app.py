#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure your database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable tracking modifications for SQLAlchemy (optional but recommended)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Uncomment this line if you have models in separate files
# db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
