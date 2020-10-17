def flat_list(my_list):
    result = []
    for sublist in my_list:
        if isinstance(sublist, list):
            result += flat_list(sublist)
        else:
            result.append(sublist)
    return result


# It looks only at values, not nesting of inner lists.
# it returns true for [[1, 2]] and [1, 2]
def are_lists_deep_equal(list_a, list_b):
    flat_a = flat_list(list_a)
    flat_b = flat_list(list_b)
    return len(flat_a) == len(flat_b) and all(a == b
                                              for a, b in zip(flat_a, flat_b))


def are_dictionaires_equal(dict_a, dict_b):
    return len(dict_a) == len(dict_b) and all(dict_a[key] == dict_b[key]
                                              for key in dict_a)
