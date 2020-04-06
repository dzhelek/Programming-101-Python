def validate_iterable(iterable, key):
    if type(iterable) != tuple and type(iterable) != list:
        raise ValueError("Could sort only tuples and lists!")

    previous_element_type = type(iterable[0])
    for element in iterable[1:]:
        element_type = type(element)
        if element_type != int and element_type != dict:
            raise ValueError("Cannot sort iterable with not-integer element!")
        elif element_type != previous_element_type:
            raise ValueError("Cannot sort heterogeneous iterable!")

        previous_element_type = element_type

    if element_type == dict:
        for element in iterable:
            try:
                element[key]
            except KeyError:
                raise ValueError(f"There is element with no '{key}' key!")




def sort_list(lst, ascending, key):
    if ascending:
        edge = min
    else:
        edge = max

    sorted_lst = []

    for i in range(len(lst)):
        if type(lst[0]) == int:
            edge_element = edge(lst)
        elif type(lst[0]) == dict:
            edge_element = edge(lst, key=lambda x: x[key])
        else:
            raise ValueError
        lst.remove(edge_element)
        sorted_lst.append(edge_element)


    return sorted_lst


def my_sort(iterable=None, ascending=True, key=0):
    if not iterable:
        iterable = []
    else:
        validate_iterable(iterable, key)

    if type(iterable) == tuple:
        return tuple(sort_list(list(iterable), ascending, key))
    else:
        return sort_list(iterable, ascending, key)    


def main():
    print(my_sort(iterable=[{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}], key='age'))


if __name__ == '__main__':
    main()