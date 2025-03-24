from flask import Blueprint, render_template

dashboard_posts = Blueprint('dashboard_posts_page', __name__)

@dashboard_posts.route('/')
def dashboard_posts_page():
    return render_template(
        'dashboard/posts.html'
    )

@dashboard_posts.route('/New_Post')
def dashboard_new_post_page():
    return render_template(
        'dashboard/new_post.html'
    )
    