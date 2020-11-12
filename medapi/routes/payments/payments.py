from flask_cors import cross_origin
from flask import jsonify
import stripe

from wsgi import app
from settings import STRIPE_API_KEY

prefix = "/api/payment"
stripe.api_key = STRIPE_API_KEY


@app.route(prefix + '/subscribe')
def subscribe():
    return "Hello, World!"


@app.route(prefix + '/pay-once', methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def pay_once():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'name': 'One month access',
            'description': 'One month of access to DoctorsAustralia',
            'amount': 100,
            'currency': 'aud',
            'quantity': 1,
        }],
        success_url='https://doctorsaustralia.fun',
        cancel_url='https://doctorsaustralia.fun'
    )
    return jsonify(data=session.stripe_id)


@app.route(prefix + '/success')
def payment_success():
    return "Thank you for paying Elliott some dosh!"


