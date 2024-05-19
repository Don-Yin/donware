# post_install.py


MESSAGE = """
try:
from donware import inspect_package; inspect_package(donware)
"""


def print_message():
    print(MESSAGE)


if __name__ == "__main__":
    print_message()
