class Employee():

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return ("Имя: {} ID: {}.".format(self.name,self.id))

class Manager(Employee):

    def __init__(self, name="", id="", department=""):
        super().__init__(name, id)
        self.department = department

    def manage_project(self, pr_name):
        return ("Менеджер {} работает над проектом {}.".format(self.name, pr_name))

class Technician(Employee):

    def __init__(self, name, id, specialization=""):
        self.specialization = specialization
        super().__init__(name, id)

    def perform_maintenance(self):
        return("Техник {} производит техническое обслуживание.".format(self.name))

class TechManager(Manager, Technician):

    team_info=[]

    def __init__(self, name, emp_id, department, specialization):
        super().__init__(name, emp_id, department)
        super().__init__(name, emp_id, specialization)
    
    @classmethod
    def add_employee(cls, member):
        cls.member = member
        TechManager.team_info.append(cls.member)

    @classmethod
    def get_team_info(cls):
        print("Тима:")
        for member in cls.team_info:
            print("Имя: {} ID: {}".format(member.name,member.id))

emp1 = Employee("Маша", 1)
emp2 = Employee("Иван", 2)
manager = Manager("Миша", 3, "Продажиии")
technician = Technician("Егор", 4, "Электрик воу воу")
tech_manager = TechManager("Андрей", 5, "IT-разработка", "Специалист по машинному обучению")

print(emp1.get_info())
print(emp2.get_info())
print(manager.get_info())
print(technician.get_info())

print(manager.manage_project("Увелечение товарооборота"))
print(technician.perform_maintenance())

tech_manager.add_employee(emp1)
tech_manager.add_employee(emp2)
tech_manager.get_team_info()
