from flask import Blueprint,redirect,url_for,render_template
from app.user.forms import RegisterForm, LoginForm
from app import db
from app.user.models import User

users = Blueprint('users', __name__)


@users.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('posts.home'))
    return render_template("register.html", title="Registration", form=form)


@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            return redirect(url_for('posts.home'))
    return render_template("login.html", title="Login", form=form)