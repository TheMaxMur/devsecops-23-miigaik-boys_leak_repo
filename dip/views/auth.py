from flask import Blueprint, make_response, render_template, request, url_for, current_app, redirect, g
from sqlalchemy import text

from dip.utils.session import get_current_user, create_session
from dip.utils.session import set_user_identity, SESSION_COOKIE_NAME
from dip.utils.security import generate_password_hash
from dip.models import User
from dip.extensions import db


bp = Blueprint('bp_auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        user = get_current_user()

        if not user:
            return render_template('login.html')

        return redirect(url_for('bp_user.profile'))

    if request.method == 'POST':
        username = request.form['username']
        plain_password = request.form['password']

        hashed_password = generate_password_hash(plain_password, current_app.config['PASSWORD_SALT'])

        user_query = db.session.query(User).filter(User.username == username, User.password == hashed_password)

        user = user_query.first()

        if not user:
            return render_template('login.html', error='Неверный логин или пароль'), 403

        session = create_session(user.username, user.role)

        resp = redirect(url_for('bp_user.profile'))
        resp.set_cookie(SESSION_COOKIE_NAME, session)

        g.user = user.json()

        return resp


@bp.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect(url_for('bp_auth.login')))
    resp.delete_cookie(SESSION_COOKIE_NAME)
    return resp