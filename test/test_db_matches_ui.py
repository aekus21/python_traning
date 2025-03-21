from model.group import Group

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(ids=group.id, name=group.test_name.strip())
    db_list = map(clean, filter(lambda x: x is not None, (db.get_group_list())))
    assert sorted(ui_list, key= Group.id_or_max) == sorted(db_list, key= Group.id_or_max)