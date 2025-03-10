#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 9, 2025
# Shows how global and local variables work

# GLOBAL VARIABLE
the_entity = ":)"


def func1():
    # The comment below will raise an error
    # print(f"func1 (1): {the_entity}")
    # This variable is local
    the_entity = ":("
    # It can be accessed within the scope of this function
    print(f"func1: {the_entity}")
    # The declaration of the local variable won't affect the global one


def func2():
    # This function wants to access the global variable
    global the_entity
    # The value is changed
    the_entity = ":-("
    # The change will appear globally
    print(f"func2: {the_entity}")


def main():
    # State before func1
    print(f"State before func1: {the_entity}")
    # Call func1
    func1()
    # State after func1 and before func2
    print(f"State after func1: {the_entity}")
    print(f"State before func2: {the_entity}")
    # Call func2
    func2()
    # State after func1 [the change appears]
    print(f"State after func2: {the_entity}")


if __name__ == "__main__":
    main()
