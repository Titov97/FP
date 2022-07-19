import os
from flask import Flask, redirect, request
import stripe

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://http://127.0.0.1:8000'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LLJ6QDuIvUrf1Cm7GxJdlcq',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN +'/success.html',
            cancel_url=YOUR_DOMAIN +'/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect("/checkout.html", code=303)


if __name__ == '__main__':
    app.run(port=4242)
