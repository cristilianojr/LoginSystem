from models import database


def forgot_password_verfication(username) -> None:
    __table = 'users'
    __database = database.DataBase(r'models\registered_users.db', __table)

    # Update before applying
    username._update_text_options()

    for line in __database.data:
        if username in line:
            print(f'Your password if {line[2]}')
            return

    print('Username not exist')
