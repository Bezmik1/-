class Book:

    title = "War and world"
    author = "Alexey Tolstoy"
    year = 1815

    def get_info(self):
        print("Название книги: {}, Автор: {}, Год издания: {}".format(self.__class__.title,self.__class__.author,self.__class__.year))
    
book = Book()
book.get_info()
