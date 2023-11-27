from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Replace 'YourApp' with the actual name of your Flask app instance
# (the variable you used to create your Flask app in __init__.py)
# Example: app = Flask(__name__)
manager = Manager(app)

# Replace 'YourApp' and 'db' with the actual names you used
# for your Flask app instance and SQLAlchemy database instance
migrate = Migrate(app, db)

# Add Flask-Migrate commands to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
