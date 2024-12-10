# import functions
import time
from functions import get_todos,write_todos

prompt = "Type add, show, edit, complete, or exit:"
now = (time.strftime("%b %d, %Y %H:%M:%S"))
print("It is",now)

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            print(f"{index + 1}.{item}")

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            num = num - 1

            todos = get_todos()

            new_Todo = input("Input a new Todo:")
            todos[num] = new_Todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todos.pop(number - 1)
            write_todos(todos)

        except IndexError:
            print("Such todo does not exist")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print("Bye!")
