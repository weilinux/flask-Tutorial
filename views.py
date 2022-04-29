from flask import Blueprint, render_template, request

views = Blueprint(__name__, 'views')


@views.route("/")
def home():
    return render_template("index.html", name="horse")


@views.route("/profile/<username>")  # access path from url path
def profile(username):
    args = request.args
    field = args.get('field')  # access path field value by post through url
    return render_template("index.html", name=username, field=field)
