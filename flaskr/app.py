from flaskr import create_app
from .modelos import db, Usuario, Album, Medio
from .modelos import AlbumSchema

#LINK para acceder a la explicacion teorica en prezi https://prezi.com/i/uhrp65hnbmwh/
app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
with app.app_context():
    Album_Schema = AlbumSchema()
    u = Usuario(nombre='jhonny', contrasena='kirito123')
    a = Album(titulo='superman', anio=2016, descripcion='emi', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([Album_Schema.dumps(album) for album in Album.query.all()])

