class School_Library:
    def __init__(self, lst, nm):
        self.name = nm
        self.books = lst
        self.borrow = {}

    def Display(self):
        print(f"{self.name}'s Library has : \n")
        for bks in self.books:
            print(bks)

    def Borrow(self, user_name, book_name):
        if book_name not in self.borrow.keys():
            self.borrow.update({book_name: user_name})
            print(
                f"The book has been added in the database. You can now borrow the book."
            )
        else:
            print(
                f"Sorry {self.borrow[book_name]} has been already been borrowed by {self.name}.Please choose another book !"
            )

    def Return_Book(self, book_name):
        if book_name not in self.borrow.keys():
            print("The book has not been returned.....")
        else:
            self.borrow.pop(book_name)
            print("Book successfully returned. \n")

    def New_Book(self, book_name):
        self.books.append(book_name)
        print("Book successfully added. ")

    def User_Choice(self):
        while True:
            user_choice = int(
                input(
                    "Welcom select your choice: \n\n1: Available books in the School library. \n2: Borrow a book of your choice. \n3: Return borrowed book before deadline. \n4: Add a new book. \n"
                )
            )
            if user_choice == 1:
                obj.Display()
            elif user_choice == 2:
                name = input("What is your name: \n")
                book = input("What is the name of the book you want to borrow: \n")
                obj.Borrow(name, book)
            elif user_choice == 3:
                rtn_book = input("what is the name of the book you want to return: \n")
                obj.Return_Book(rtn_book)
            elif user_choice == 4:
                add_book = input("What is the name of the new book: \n")
                obj.New_Book(add_book)
            else:
                print("Sorry!! ... Please try again.")
            user_choice = int(input("\nDo you want \n1: To continue.\n2: To exit.\n"))
            if user_choice == 1:
                continue
            else:
                break


if __name__ == "__main__":
    print("\t\t Welcome to School Library \t\t\n")
    obj = Schoool_Library(
        ["JAVASCRIPT", "C & C++", "MEDIAPIPE", "PYTHON", "NODE JS", "HTMl & CSS"],
        "MICHEAL SAMI",
    )
    obj.User_Choice()
