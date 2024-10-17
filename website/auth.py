from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>" 

@auth.rutine('/logout')
def logout():
    return"<p>Logout</p>" 

@auth.route('/sign-up')
def logout():
    return "<p>sign up</p>" 