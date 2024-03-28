# models/result.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    prediction = db.Column(db.JSON)

    def __repr__(self):
        return f'<Result {self.name}: {self.prediction}>'
