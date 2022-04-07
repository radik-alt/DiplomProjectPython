import datetime
import sqlalchemy as db


class Users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    first_name = db.Column('first_name', db.String(50), nullable=False),
    last_name = db.Column("last_name", db.String(50), nullable=False),
    password = db.Column("password", db.String(50), nullable=False),
    date = db.Column("data", db.DATETIME, default=datetime.datetime.now())

    def __repr__(self):
        return f"<users{self.id}>"
