class Book:

    title = "Kuroko no Basuke"
    author = "Tadatoshi Fujimaki"
    year = 2014

    def get_info(self):
        print("Название книги: {}, Автор: {}, Год издания: {}".format(self.__class__.title,self.__class__.author,self.__class__.year))
    
book = Book()
book.get_info()
