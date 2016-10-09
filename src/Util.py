import collections


def argument_to_list(arg):
    if isinstance(arg, collections.Iterable):
        return arg
    else:
        return [arg]
