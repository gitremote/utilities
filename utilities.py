def create_greeting(name="World"):
    """Creates a greeting message

    By default, 'World' is greeted, but
    another value can be provided instead.

    """
    return "Hello, {}!".format(name)


def append(data, input_list=[]):
    """Appends the given data to a list

    If no list is provided, then a new list 
    will be created, containing only the
    given data

    """

    input_list.append(data)

    return input_list
