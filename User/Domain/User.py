class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str, password:int):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email
        self._password = password

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def set_first_name(self, first_name:str):
        self._first_name = first_name

    def set_last_name(self, last_name:str):
        self._last_name = last_name

    def set_username(self, username:str):
        self._username = username

    def set_email(self, email:str):
        self._email = email

    def set_password(self, password:int):
        self._password = password

        
