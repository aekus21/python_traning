def test_delete_first_contact(app):
    app.session.login_form("admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()