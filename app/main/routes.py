from flask import Blueprint


main = Blueprint("main", __name__)


@main.route('/about', methods=['POST', 'GET'])
def about():
    return 'About Page'

@main.route("/")
@main.route('/home', methods=['POST', 'GET'])
def home():
    return 'Home Page'
