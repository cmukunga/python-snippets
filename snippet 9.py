class Person:
    species  = 'Homo sapiens'
    count = 0
    def __init__(self,id):
        self.id = id
    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}')
    @staticmethod
    def detais():
        pass