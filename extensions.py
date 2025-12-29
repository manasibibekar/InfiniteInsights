# Central place for shared infra.
# This file exists to avoid circular imports
# no app, no config here, only objects

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()