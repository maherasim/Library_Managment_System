from app import app

@app.route('/admin/dashboard')
def admin_dashboad():
    return '<h1>This is the admin dashboard page</h1>'

@app.route('/admin/profile')
def admin_profile():
    return '<h1>This is the admin profile page</h1>'