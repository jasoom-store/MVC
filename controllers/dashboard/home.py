from flask import Blueprint, render_template

dashboard_home = Blueprint('dashboard_home_page', __name__)

@dashboard_home.route('/')
def dashboard_home_page():
    return render_template(
        'dashboard/home.html'
    )