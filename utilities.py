def create_greeting(name="World"):
    """creates a greeting message

    By default, 'World' is greeted, but
    another value can be provided instead.

    """
    return "Hello, {}!".format(name)


def append(element, to=[]):
    """Appends the given data to a list

    If no list is provided, then a new list 
    will be created, containing only the
    given data

    """

    to.append(element)

    return to

def add_three_numbers(num_one, num_two, num_three):
    """Adds three numbers"""
    total = num_one + num_two + num_two

    return total


def multiply_three_numbers(num_one, num_two, num_three):
    """Multiplies three numbers"""
    pass
