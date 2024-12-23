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

bezmik = UserAccount("Ivan", "99@inbox.ru", "basketball12345")
bezmik.set_password("oo11")
print(bezmik.check_password("basketball12345"))
print(bezmik.check_password("oo11"))
