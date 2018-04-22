from flask import render_template, redirect, url_for,request, flash
from . import auth
from .form import LoginForm
from ..model import Admin
from flask_login import login_user, login_required, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.verify_password(form.password.data):
            login_user(admin)
            return redirect(url_for('main.index'))
        flash('密码错误！')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已登出.")
    return redirect(url_for('main.index'))