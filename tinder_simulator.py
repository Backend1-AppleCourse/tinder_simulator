
users_db = {1:{'name': "name1", 'gender': "male", 'age': 25, 'profession': "teacher", 'tv_show': "friends", 'food': "pasta"},
        2:{'name': "name2", 'gender': "male", 'age': 30, 'profession': "engineer", 'tv_show': "breaking bad", 'food': "pizza"},
        3:{'name': "name3", 'gender': "female", 'age': 18, 'profession': "student", 'tv_show': "stranger things", 'food': "sushi"},
        4:{'name': "name4", 'gender': "female", 'age': 22, 'profession': "professor", 'tv_show': "game of thrones", 'food': "burger"}}

class Person:
    def __init__(self, name, gender, age, profession, tv_show, food):
        if not name:
            raise ValueError("Name cannot be empty")
        if gender not in ['male', 'female', 'other']:
            raise ValueError("Gender must be 'male', 'female', or 'other'")
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120")
        if not profession:
            raise ValueError("Profession cannot be empty")
        if not tv_show:
            raise ValueError("TV Show cannot be empty")
        if not food:
            raise ValueError("Food cannot be empty")

        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.tv_show = tv_show
        self.food = food

    def __str__(self):
        return (f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}, "
                f"Profession: {self.profession}, Favorite TV Show: {self.tv_show}, "
                f"Favorite Food: {self.food}")
    
    @staticmethod
    def from_cmd():
        name = input("Enter your name: ")
        while not name:
            print("Name cannot be empty.")
            name = input("Enter your name: ")
        gender = input("Enter your gender (male, female, other): ")
        while gender not in ['male', 'female', 'other']:
            print("Invalid gender. Gender must be 'male', 'female', or 'other'.")
            gender = input("Enter your gender (male, female, other): ")
        
        age = input("Enter your age: ")
        while (not age) :
            print("cant be empty.")
            age = input("Enter your age: ")
        while not age.isdigit() :
            print("Has to be a number, not string.")
            age = input("Enter your age: ")
        while (not (0 <= int(age) <= 120)):
            print("Invalid age. Age must be between 0 and 120.")
            age = input("Enter your age: ")
        age = int(age)
        
        profession = input("Enter your profession: ")
        while not profession:
            print("Profession cannot be empty.")
            profession = input("Enter your profession: ")
        
        tv_show = input("Enter your favorite TV show: ")
        while not tv_show:
            print("TV Show cannot be empty.")
            tv_show = input("Enter your favorite TV show: ")
        
        food = input("Enter your favorite food: ")
        while not food:
            print("Food cannot be empty.")
            food = input("Enter your favorite food: ")
        
        return Person(name, gender, age, profession, tv_show, food)

class Tinder:
    def __init__(self, users_db):
        self.users_db = users_db
        persons = []
        for user in users_db.values():
            person = Person(name=user['name'], gender=user['gender'],age=user['age'], profession=user['profession'], tv_show=user['tv_show'], food=user['food'])
            persons.append(person)
        self.persons = persons

    def get_users_db():
        return self.users_db
    
    def run_check_match(self):
        temp=Person.from_cmd()
        for person in self.persons:
            if ((person.name == temp.name or
                10 > person.age - temp.age > -10 or
                person.profession == temp.profession or
                person.tv_show == temp.tv_show or
                person.food == temp.food) and
                person.gender != temp.gender):
                    print(f"You have things in common with the following person:\n{person}")


tinderApp = Tinder(users_db)

tinderApp.run_check_match()
    