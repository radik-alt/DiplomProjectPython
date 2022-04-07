import sqlalchemy as db


class Profiels(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    name = db.Column('first_name', db.String(50), nullable=False),
    age = db.Column("age", db.Integer, nullable=False),
    city = db.Column("password", db.String(50), nullable=False),

    users_id = db.Column("users_id", db.Integer, db.ForeignKey('users_id'))

    def __repr__(self):
        return f"<users{self.id}>"