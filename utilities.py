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
