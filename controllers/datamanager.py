import sqlite3
from kivy.uix.widget import Widget

from kivy.properties import (
    ListProperty, NumericProperty,
    StringProperty,
)

class DataManager(Widget):
    path: str = StringProperty('')
    data: list = ListProperty([])
    
    def __init__(self, path: str = None, **kwargs) -> None:

        # Call the parent init class
        super(DataManager, self).__init__(**kwargs)

        # Binding Properties
        self.bind(
            path = self._extract_data,
            )

        # Set default path 
        self.path = path if path != None else self.path

    def _extract_data(self, *args) -> None:
        try:
            connection = sqlite3.connect(self.path)
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users')

            for item in cursor.fetchall():
                self.data.append(item)

        except Exception as Error:
            print('ERROR:', Error)

    def get(self, row: int, column: int) -> str:
        try: 
            response = self.data[row][column]
            return response
        except Exception as Error:
            print('ERROR:', Error)
            return []

    def set(self) -> None: ...

