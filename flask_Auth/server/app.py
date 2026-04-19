from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from model import db, bcrypt
from route import Signup, Login, Logout, CheckSession, Workouts, WorkoutByID

app = Flask(__name__)
app.secret_key = b'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Workouts, '/workouts')
api.add_resource(WorkoutByID, '/workouts/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)