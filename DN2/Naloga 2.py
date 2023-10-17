our_list = [1,2,3,4,5,6,7]

our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}

our_tuple = (357, 12, 12, 8, 5, 2, 2)

our_dict["d"] = our_list[4]
our_list.remove(4)
new_tuple = tuple(our_dict.values())
print("Tuple objekta sta enaka:",new_tuple == our_tuple)