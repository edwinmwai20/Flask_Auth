from app import app
from model import db, User, Workout

with app.app_context():
    print("Deleting data...")
    Workout.query.delete()
    User.query.delete()

    print("Seeding users...")
    u1 = User(username="Edwin")
    u1.password_hash = "moringa2024"
    db.session.add(u1)
    db.session.commit() 
    
    print("Seeding workouts...")
    workouts = [
        Workout(exercise="Running", duration_minutes=30, intensity="High", user=u1),
        Workout(exercise="Yoga", duration_minutes=45, intensity="Low", user=u1),
        Workout(exercise="Cycling", duration_minutes=60, intensity="Medium", user=u1),
        Workout(exercise="Swimming", duration_minutes=40, intensity="High", user=u1),
        Workout(exercise="Weight Training", duration_minutes=50, intensity="High", user=u1),
        Workout(exercise="Walking", duration_minutes=20, intensity="Low", user=u1),
        Workout(exercise="HIIT", duration_minutes=25, intensity="High", user=u1),
        Workout(exercise="Pilates", duration_minutes=35, intensity="Medium", user=u1),
        Workout(exercise="Jump Rope", duration_minutes=15, intensity="High", user=u1),
        Workout(exercise="Stretching", duration_minutes=10, intensity="Low", user=u1)
    ]

    db.session.add_all(workouts)
    db.session.commit()
    print(f"Success! Seeded {len(workouts)} workouts for {u1.username}.")