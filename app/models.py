from app import db


class City(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(50), nullable=False)

db.create_all()
db.session.commit()