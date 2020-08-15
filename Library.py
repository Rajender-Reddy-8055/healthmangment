class Library:
    def __init__(self, list_of_books, library_name):
        self.books = list_of_books
        self.library = library_name
        self.dict = {}

    def display_books(self):
        print(f"These are the books currently available in our library **{self.library}**")
        m = 1
        for i in self.books:
            print(m, end=".")
            print(i)
            m += 1

    def lend_books(self, book, name):
        if book not in [self.dict.keys()]:
            if book in self.books:
                # self.dict[book] = name
                self.dict.update({book: name})
                print("you can take the book")
            else:
                print("no book with that name")
        else:
            print(f"book is with {self.dict[book]}")

    def add_books(self, book):
        print(f" {book} is added successfully")
        self.books.append(book)

    def return_books(self, book):
        self.dict.pop(book)
        print(f"{book} is returned successfully")


while True:
    print("Welcome to Library")
    while True:
        print("Enter the options for the operation you want to do:")
        print("1.Display books \n2.Lend books\n3.Add books\nAnd press any other key Return books")
        n = input()
        user = Library(["Rich Dad Poor Dad", "Charlie", "Quiet", "Dream Big"], "Power Your Mind")
        if n == "1":
            user.display_books()
        elif n == "2":
            x = input("Please enter your name:")
            y = input("Please enter the name of book you want to lend:")
            user.lend_books(y, x)
        elif n == "3":
            x = input("please enter the name of book you want to add:")
            user.add_books(x)
        else:
            x = input("Enter the name of book you want to return:")
            user.return_books(x)
        break
    print("If want to Quit press q and to continue press any key:")
    b = input()
    if b == "q":
        quit()
    else:
        continue
