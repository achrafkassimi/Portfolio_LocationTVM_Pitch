# from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy


# class Admin():
#     """User Model

#     Args:
#         db (_type_): Model from SQL Alchemy

#     Returns:
#         string: Only check_password returns, else used to store user info
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password_hash = db.Column(db.String(150), nullable=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)