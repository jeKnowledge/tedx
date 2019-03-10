from flask import request, render_template, flash, redirect, url_for
from app import app, db
from app.forms import InsertOratorForm, LoginForm
from app.models import Orator, User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="TEDx UC", page="home")

@app.route('/tedx')
def tedx():
    return render_template('tedx.html', page="tedtedx", title="TED & TEDx")

@app.route('/vieworators')
def vieworators():
    orators = Orator.query.all()
    return render_template('vieworators.html', orators=orators, page="oradores")


# @app.route('/insertorator', methods=['GET', 'POST'])
# @login_required
# def insertorator():
#     form = InsertOratorForm()
#     if(request.method == 'POST' and form.validate_on_submit()):
#         new_orator = Orator(form.name.data, form.job.data, form.age.data, form.info.data)
#         if form.photo.data:
#             new_orator.set_photo(form.photo.data)
#         db.session.add(new_orator)
#         db.session.commit()
#         flash('Record was successfully added')
#         return redirect(url_for('index'))
#     return render_template('insertorator.html', form=form)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('insertorator'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form)
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

@app.route('/program')
def program():
    return render_template('program.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')
