# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group("test_group2", "test_header_2", "test_footer_2"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
