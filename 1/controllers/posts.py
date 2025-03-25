from flask import Blueprint, render_template

posts = Blueprint('posts_page', __name__)

@posts.route('/')
def posts_page():
    return render_template(
        'posts.html'
    )
    