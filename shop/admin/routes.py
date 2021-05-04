from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db
from .forms import RegistrationForm

@app.route('/')
def home():
  return "home page of your shop"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_sessi on.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title="registration page")