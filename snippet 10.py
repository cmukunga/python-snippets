class Course:
    def __init__(self, title, instructor, lectures, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0
    def __str__(self):
        return f'{self.title} by {self.instructor}'
    @staticmethod
    def detais():
        pass
    def new_user_enrolled(self, user):
        self.users.append(user)
    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating)/(self.ratings + 1)
        self.ratings += 1
    def show_details(self):
        print('Course Title : ', self.title)
        print('Intructor : ', self.instructor)
        print('Price : ', self.price)
        print('Number of Lectures : ', self.lectures)
        print('Users : ', self.users)
        print('Average rating : ', self.avg_rating)