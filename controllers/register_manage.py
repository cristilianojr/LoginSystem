from models import database

def check_username_exitence(database: database.DataBase, username: str) -> bool:
    # Just update to verify
    database._do_update_data()

    for line in database.data:
        if username in line:
            return True
    return False

def register_user(full_name: str, username: str, password: str) -> None:
    __table = 'users'
    __database = database.DataBase(r'models\registered_users.db', __table)

    # Update before applying
    for var in [full_name, username, password]:
        var._update_text_options()

    if check_username_exitence(__database, username):
        print('Send Signal -> This username alredy exist!')
    else:
        __database.insert_dataline((full_name.text, username.text, password.text))

