from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    species = db.Column(db.String(255), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)
    owner = db.relationship('Owner', backref=db.backref('pets', lazy=True))

    def __repr__(self):
        return f'<Pet {self.name},{self.species}>'