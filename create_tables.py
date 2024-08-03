from app import db, app

# Create a new application context
with app.app_context():
    # Create the database tables
    db.create_all()
    print("Database tables created successfully!")
