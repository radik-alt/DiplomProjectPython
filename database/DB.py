import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
import sqlalchemy as db
import sqlalchemy.sql as select
from sqlalchemy import create_engine, MetaData
from flask_sqlalchemy import SQLAlchemy


class DB:

    def db_flask(self):
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'

        db = SQLAlchemy(app)



    def db_alchemy(self):
        connection = create_engine('sqlite:///db.sqlite', echo=True)
        metadata = MetaData()

        books = db.Table(
            "books", metadata,
            db.Column('id', db.Integer, primary_key=True, autoincrement=True),
            db.Column('first_name', db.String(50), nullable=False),
            db.Column("last_name", db.String(50), nullable=False),
            db.Column("password", db.String(50), nullable=False),
            db.Column("data", db.DATETIME, default=datetime.datetime.now())
        )

        metadata.create_all(bind=connection)

        connection.execute(
            books.insert(),
            {
                'first_name': "Radik",
                'last_name': "Abdulhakov",
                'password': "jokerobmana31"
            }
        )

