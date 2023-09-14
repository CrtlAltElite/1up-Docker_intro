from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hits = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    # Increment the hit counter
    counter = Counter.query.first()
    if not counter:
        counter = Counter(hits=1)
        db.session.add(counter)
    else:
        counter.hits += 1

    db.session.commit()
    return f"This page has been visited {counter.hits} times!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
