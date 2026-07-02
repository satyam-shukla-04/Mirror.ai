from sqlalchemy.orm import Session
from backend.utils.security import verify_password
from backend.utils.jwt_handler import create_access_token
from backend.database.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.utils.security import hash_password

def login_user(db, email, password):

    user = UserRepository.get_by_email(db, email)

    print("========== LOGIN DEBUG ==========")
    print("Email:", email)
    print("User Found:", user)

    if user:
        print("Stored Hash:", user.password_hash)

    if not user:
        raise ValueError("Invalid email or password.")

    is_valid = verify_password(password, user.password_hash)

    print("Password Match:", is_valid)

    if not is_valid:
        raise ValueError("Invalid email or password.")

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return token

def register_user(
    db: Session,
    username: str,
    email: str,
    password: str
):
    """
    Register a new user.
    """

    # Check username
    if UserRepository.get_by_username(db, username):
        raise ValueError("Username already exists.")

    # Check email
    if UserRepository.get_by_email(db, email):
        raise ValueError("Email already exists.")

    # Hash password
    password_hash = hash_password(password)

    # Create user object
    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    # Save to database
    user = UserRepository.create_user(
        db,
        user
    )

    return user