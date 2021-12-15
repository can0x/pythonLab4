from datetime import date
from Person import Person
from Notebook import Notebook

def main():
    person1 = Person()
    person2 = Person('Kiril', 'Marchenko', '+380(67)-200-21-45', date(2003, 3, 25))
    notebook = Notebook(person1)
    notebook += person2
    notebook -= person1
    print(*(notebook*'Unknown'))
    print(*(notebook*'+380(67)-200-21-45'))

main()
