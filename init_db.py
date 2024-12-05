from app import app, db

with app.app_context():
    if db.engine.has_table('data'):
        print("La tabla 'data' ya existe. No se creó una nueva.")
    else:
        db.create_all()
        print("Base de datos inicializada")