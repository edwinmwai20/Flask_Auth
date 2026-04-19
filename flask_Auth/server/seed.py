from app import app
from model import db, User, Workout

with app.app_context():
    print("Deleting data...")
    User.query.delete()
    Workout.query.delete()

    print("Seeding users...")
    u1 = User(username="Edwin")
    u1.password_hash = "moringa2024"
    
    print("Seeding workouts...")
    w1 = Workout(exercise="Running", duration_minutes=30, intensity="High", user=u1)
    w2 = Workout(exercise="Yoga", duration_minutes=45, intensity="Low", user=u1)
    w3 = Workout(exercise="Cycling", duration_minutes=60, intensity="Medium", user=u1)
    w4 = Workout(exercise="Swimming", duration_minutes=40, intensity="High", user=u1)
    w5 = Workout(exercise="Weight Training", duration_minutes=50, intensity="High", user=u1)
    w6 = Workout(exercise="Walking", duration_minutes=20, intensity="Low", user=u1)
    w7 = Workout(exercise="HIIT", duration_minutes=25, intensity="High", user=u1)
    w8 = Workout(exercise="Pilates", duration_minutes=35, intensity="Medium", user=u1)
    w9 = Workout(exercise="Jump Rope", duration_minutes=15, intensity="High", user=u1)
    w10 = Workout(exercise="Stretching", duration_minutes=10, intensity="Low", user=u1)

    db.session.add_all([u1, w1, w2])
    db.session.commit()
    print("Success!")