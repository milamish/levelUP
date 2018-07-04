from flask import *


user=Blueprint('user',__name__)
@user.route('/login/',method=('GET','POST'))
def login():
    form=login()
    if form.validate_on_submit():
        login_user(form.user)
        flash("logged in succsessfully!")
        return redirect(request.args.get("next") or url_for("tracking.index"))
        return render_template('user/login.html', form =form)