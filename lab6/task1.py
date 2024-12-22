class UserAccount():

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

andrey = UserAccount("Andrey", "123@gmail.com", "qwerty123")
andrey.set_password("lol123")
print(andrey.check_password("qwerty123"))
print(andrey.check_password("lol123"))
