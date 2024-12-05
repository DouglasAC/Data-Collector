from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os

app = Flask(__name__)

db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = 'height_collector'

db_uri = f'postgresql://{db_user}:{db_password}@localhost/{db_name}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        print(email, height)
        
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            db.session.add(Data(email, height))
            db.session.commit()
            
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
        else:
            return render_template('index.html', text="¡Parece que ya tenemos algo de esa dirección de correo electrónico!")

if __name__ == '__main__':
    app.run(debug=True)