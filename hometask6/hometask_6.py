class Person:
    def __init__(self, name, hometown, age, gender):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.gender = gender
        if self.gender == 'мужской':
            self.family_status = 'холост'
        if self.gender == 'женский':
            self.family_status = 'свободна'



    def change_family_status(self):
        if self.gender == 'мужской':
            if self.family_status == 'холост' or self.family_status == 'разведён':
                self.family_status = 'женат'
            elif self.family_status == 'женат':
                self.family_status = 'разведён'
        if self.gender == 'женский':
            if self.family_status == 'свободна' or self.family_status == 'разведена':
                self.family_status = 'замужем'
            elif self.family_status == 'замужем':
                self.family_status = 'разведена'


    def introduce_person(self):

        print(f'Имя: {self.name}\n'
              f'Место рождения: {self.hometown}\n'
              f'Возраст: {self.age}\n'
              f'Пол: {self.gender}\n'
              f'Семейный статус: {self.family_status}')
        print()

class Student(Person):
    def __init__(self, name, hometown, age, gender, year_of_education, school):
        super().__init__(name, hometown, age, gender)
        self.year_of_education = year_of_education
        self.school = school


    def add_year_of_education(self):
        self.year_of_education += 1
        self.age += 1

    def introduce_student(self):
        print(f'Имя: {self.name}\n'
              f'Место рождения: {self.hometown}\n'
              f'Возраст: {self.age}\n'
              f'Пол: {self.gender}\n'
              f'Год обучения: {self.year_of_education}\n'
              f'Школа: {self.school}')
        print()


user_male = Person(name='Джон', age='28', hometown='Нижний тагил', gender='мужской')
user_female = Person(name='Барбара', age='23', hometown='Воркута', gender='женский')

user_male.introduce_person() # представляем мужской пол

user_female.introduce_person() # представляем женский пол

user_male.change_family_status() # женимся

user_female.change_family_status() # выходим замуж

user_male.introduce_person() # проверка

user_female.introduce_person() # проверка

user_male.change_family_status() # разводимся

user_male.introduce_person() # проверка

user_student = Student(name='Томас', age=12, hometown='Челябинск', gender='мужской', year_of_education=5, school='Физико-матемачиский лицей №355')

user_student.introduce_student() # представляем школьника
user_student.add_year_of_education() # переходим в следующий класс
user_student.introduce_student() # проверяем