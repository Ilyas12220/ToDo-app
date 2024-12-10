FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


"""
Read the document and return the list of todos    
"""


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


"""
Add , edit , or complete the todo
"""