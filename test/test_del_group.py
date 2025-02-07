

def test_delete_first_group(app):
    app.session.login_form("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()