from flask import Blueprint

posts = Blueprint('posts',__name__)



@posts.route('/')
@posts.route('/home', methods=['GET', 'POST'])
def home():
    return 'hello world'
