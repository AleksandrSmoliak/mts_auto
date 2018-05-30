# -*- coding: utf-8 -*-
def test_loginlogout(app):
    app.session.login(username='a_smoliak', password='123qwe')
    app.session.logout()
