from flask import request, session
from flask_restful import Resource
from model import db, User, Workout


class Signup(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = User(username=data.get('username'))
            user.password_hash = data.get('password')
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 422

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.authenticate(data.get('password')):
            session['user_id'] = user.id
            return user.to_dict(), 200
        return {"error": "Invalid credentials"}, 401

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return user.to_dict(), 200
        return {"error": "No active session"}, 401
    


class Workouts(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {"error": "Unauthorized"}, 401
        
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        query = Workout.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)
        
        return {
            "workouts": [w.to_dict() for w in query.items],
            "total_pages": query.pages,
            "current_page": query.page
        }, 200

    def post(self):
        user_id = session.get('user_id')
        if not user_id:
            return {"error": "Unauthorized"}, 401
        
        data = request.get_json()
        try:
            workout = Workout(
                exercise=data['exercise'],
                duration_minutes=data.get('duration_minutes'),
                intensity=data.get('intensity'),
                user_id=user_id
            )
            db.session.add(workout)
            db.session.commit()
            return workout.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 400

class WorkoutByID(Resource):
    def patch(self, id):
        user_id = session.get('user_id')
        workout = Workout.query.filter_by(id=id, user_id=user_id).first()
        if not workout:
            return {"error": "Workout not found"}, 404
        
        data = request.get_json()
        for attr in data:
            setattr(workout, attr, data[attr])
        db.session.commit()
        return workout.to_dict(), 200

    def delete(self, id):
        user_id = session.get('user_id')
        workout = Workout.query.filter_by(id=id, user_id=user_id).first()
        if not workout:
            return {"error": "Workout not found"}, 404
        
        db.session.delete(workout)
        db.session.commit()
        return {}, 204