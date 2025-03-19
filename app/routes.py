from flask import request, jsonify
from .models import db, User  # Assuming you have a User model in models.py
import re

def submit():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    # Server-side validation for phone number
    if phone and not re.match(r'^\d{10}$', phone):
        return jsonify({"error": "Phone number must be numeric and exactly 10 digits."}), 400

    # Save to database
    new_user = User(name=name, email=email, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Form submitted successfully!"}), 200
