# Module-level constants are conventionally written in UPPER_CASE and
# placed near the top of the module. (You see the same pattern in the
# standard library — open up `time.py` in your Python install and
# scroll to the top.) Capitalizing the name signals "this is a fixed
# value, don't reassign it at runtime".
FILEPATH = "Files/todos.txt"


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list to a text file. """
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
