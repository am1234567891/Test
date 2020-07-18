from flask import Blueprint, redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required, roles_required
from app import db
from app.models.user_models import UserProfileForm

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.app_errorhandler(401)
def FUN_401(error):
    return render_template("main/page_401.html"), 401


@main_blueprint.app_errorhandler(403)
def FUN_403(error):
    return render_template("main/page_403.html"), 403


@main_blueprint.app_errorhandler(404)
def FUN_404(error):
    print("****404 error")
    return render_template("main/page_404.html"), 404


@main_blueprint.app_errorhandler(405)
def FUN_405(error):
    return render_template("main/page_405.html"), 405


@main_blueprint.app_errorhandler(413)
def FUN_413(error):
    return render_template("main/page_413.html"), 413


# The Home page is accessible to anyone
@main_blueprint.route('/')
def home_page():
    return render_template('main/home_page.html')


# The User page is accessible to authenticated users (users that have logged in)
@main_blueprint.route('/public')
def pubic_page():
    data = { 10: 30, 20: 40, 30: 50, 40:70, 50: 80 }
    return render_template('main/public_page.html',data=data)


# hello world
@main_blueprint.route('/cifun')
def hello_world():
    return "Hello, World!"
    # return render_template('main/cifun.html')


# The User page is accessible to authenticated users (users that have logged in)
@main_blueprint.route('/member')
@login_required  # Limits access to authenticated users
def member_page():
    data = { 10: 30, 20: 40, 30: 50, 40:70, 50: 80 }
    return render_template('main/member_page.html',data=data)


# The Admin page is accessible to users with the 'admin' role
@main_blueprint.route('/admin')
@roles_required('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('main/admin_page.html')


@main_blueprint.route('/main/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, obj=current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('main.home_page'))

    # Process GET or invalid POST
    return render_template('main/user_profile_page.html',
                           form=form)


