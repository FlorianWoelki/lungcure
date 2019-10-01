from flask import render_template
from app import app
import stripe
from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


#app = Flask(__name__)
#app.secret_key = os.urandom(12)  # Generic key for dev purposes only

stripe_keys = {
  'secret_key': 'pk_test_EXQzqiADhufPflyUzyMAgske00ZAJZdtQj',
  'publishable_key': 'sk_test_kdA54XOEj0GzAQPvsGpgfbOA00AewhFkYC'
}

stripe.api_key = stripe_keys['secret_key']

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))


@app.route('/charge', methods=['POST'])
def charge():
    if session.get('logged_in'):
        amount = 1000   # amount in cents
        customer = stripe.Customer.create(
            email= email,
            source=request.form['stripeToken']
        )
        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Lung Cure'
        )
        return render_template('index.html', user=user)


