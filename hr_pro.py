import weakref
class Employee:
    instances=[]
    def __init__(self,name,age,salary,employment_years):
        self.__class__.instances.append(weakref.proxy(self))
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_years=employment_years

def get_annual_salary(self):
    return self.salary*12

def __str__(self):
    return f"\n\nEmployees\n\nName: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years} "


class Manager(Employee):
    def __init__(self,name,age,salary,employment_years,bonus_percentage):
        super().__init__(name,age,salary,employment_years)
        self.bonus_percentage=bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage*self.salary

    def __str__(self):
        return f"\n\nManagers\n\nName: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bonus: {self.get_bonus()} "

employee_1=Employee("Dana",34,1050,8)
employee_2=Employee("Abeer",27,1600,3)

manager_1=Manager("Asma",29,1200,9,0.5)
manager_2=Manager("Eqbal",32,1800,13,0.7)

        
def main():
    print("Welcome to HR Pro")
    print("Options: ")
    print("1. Show Employees\n2. Show Managers\n3. Add An Employess\n4. Add A Manager\n5. Exit\n")
    user_choice=int(input("What would you like to do?\n----------------\n "))
    if user_choice == 1:
        for instance in Employee.instances:
            print(instance)
   
    elif user_choice==2: 
        for instance in Manager.instances:
            print(instance)
       
    
    elif user_choice==3:
        Employee(input("Name:"),input("Age:"),input("Salary"),input("Emplyement Years:"),input("Bonus Percentage: "))
        
    elif user_choice==4:
        Manager(input("Name:"),input("Age:"),input("Salary"),input("Emplyement Years:"),input("Bonus Percentage: "))
    
    else:
        print("Invalid Input")

    


if __name__ == '__main__':
	main()
    
