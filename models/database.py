from sqlite3.dbapi2 import Error
import sys, sqlite3

class DataBase:
    __data: list = []
    __path: str = ''
    __table: str = ''
    __connection: sqlite3.Connection = None
    __cursor: sqlite3.Cursor = None

    @property
    def data(self) -> list:
        return self.__data

    def _do_update_data(self) -> None:
        self.__cursor.execute(f'SELECT * FROM "{self.__table}"')
        
        for current_data in self.__cursor.fetchall():
            self.data.append(current_data)

    @property
    def table(self) -> str:
        return self.__table

    @table.setter
    def table(self, new_table: str) -> None:
        if not isinstance(new_table, str):
            raise TypeError(f'TypeError: Inappropriate argument type, data not to be a instance of {type(new_table)}')

        self.__table = new_table

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, new_path: str) -> None:
        if not isinstance(new_path, str):
            raise TypeError(f'TypeError: Inappropriate argument type, data not to be a instance of {type(new_path)}')

        self.__path = new_path

        try:
            self.__connection = sqlite3.connect(new_path)
            self.__cursor = self.__connection.cursor()
        except Exception as ConnectionError:
            print(f'Connection Error | {ConnectionError}')

    @property
    def connection(self) -> sqlite3.Connection:
        return self.__connection

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.__cursor

    def __init__(self, path: str, table: str) -> None:
        # Setting a init path, table and connect
        self.path = path
        self.table = table

        # Extracting and add to data property
        self._do_update_data()

    def __del__(self) -> None:
        # when class is destroyied, close the cursor and connection with database
        self.__cursor.close()
        self.__connection.close()

    def insert_dataline(self, data: list) -> None:
        # Insert Modification in database
        try:
            self.__cursor.execute(f'INSERT INTO {self.table} VALUES {tuple(data)};')
            self.__connection.commit()
        except sqlite3.IntegrityError as InsertError:
            print(f'InsertError | {InsertError}')
        # Setting the new data
        self._do_update_data()

    def delete_dataline(self, column: str, value: str) -> None:
        # Deleting line from database
        try:
            self.__cursor.execute(f'SELECT * from {self.table}')
            self.__cursor.execute(f'DELETE FROM {self.table} WHERE {column} = "{value}"')
            self.__connection.commit()
        except Exception as DeleteError:
            print(f'DeleteError | {DeleteError}')

        # Setting the new data
        self._do_update_data()

    def update_dataline(self, changed_column: str, new_value: str, reference_column: str, reference_value: str) -> None:
        try:
            # Checking if changed column and reference column are the same
            if changed_column == reference_column:
                raise Exception('EqualityError | The value of the column that will be changed cannot be the same as the reference column!')
            
            # Updating value from database
            self.__cursor.execute(f'SELECT * from {self.table}')
            self.__cursor.execute(f'UPDATE {self.table} SET {changed_column} = "{new_value}" WHERE {reference_column} = "{reference_value}"')
            self.__connection.commit()
        except Exception as UpdateError:
            print(f'UpdateError | {UpdateError}')

        # Setting the new data
        self._do_update_data()


if __name__ == '__main__':
    db = DataBase(r'models\registered_users.db', 'users')

    for line in db.data:
        print(line)    
