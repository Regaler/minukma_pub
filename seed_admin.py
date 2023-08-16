"""
This script seeds the initial data to the Admin table.
"""
from app import app, db
from models import Admin
from werkzeug.security import generate_password_hash

admin_data = {
    'username': 'minuk',
    'password': 'password'  # I deleted it for security reasons.
}

def seed_admin():
    """
    This function seeds the initial data to the Admin table.
    """
    new_admin = Admin(username=admin_data['username'])
    new_admin.set_password(admin_data['password'])
    db.session.add(new_admin)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_admin()
