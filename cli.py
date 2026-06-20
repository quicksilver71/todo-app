# Add a date/time line to the user output.
#
# `time` is part of Python's STANDARD LIBRARY — it ships with Python, so
# all you need is `import time` (no install). To discover the available
# names you can also do `dir(time)` in the Python console.
#
# `time.strftime(format)` returns the current local time formatted into
# a string. The format string uses "%-letter" codes that get replaced
# with the corresponding piece of the date:
#
#     %B  full month name      ("November")
#     %b  short month name     ("Nov")
#     %m  month as a number    ("11")
#     %d  day of the month     ("28")
#     %Y  4-digit year         ("2026")
#     %H  hour (24-hour)       ("14")
#     %M  minutes              ("05")
#     %S  seconds              ("09")
#
# Any other character in the format string is kept as a literal — so
# spaces, commas, colons, and dashes all stay where you put them.
# Full list: https://docs.python.org/3/library/time.html#time.strftime

import time

from functions import get_todos, write_todos


now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}.")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = get_todos()
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye!")
