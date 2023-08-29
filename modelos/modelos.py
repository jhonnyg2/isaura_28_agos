from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    contrasena = db.Column(db.String(120))
    albunes = db.relationship('Album', cascade='all, delete, delete-orphan')

class Medio(enum.Enum):
    disco = 1
    casete = 2
    cd = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(180))
    anio = db.Column(db.Integer)
    description = db.Column(db.String(180))
    medios = db.Column(db.Enum(Medio))
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    __tables_args__=(db.UniqueConstraint("usuario", "titulo", name="titulo_unico_album"),)




