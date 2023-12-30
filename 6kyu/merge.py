# https://www.codewars.com/kata/5ae840b8783bb4ef79000094/train/python
def merge(*dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                if not isinstance(merged_dict[key], list):
                    merged_dict[key] = [merged_dict[key]]
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [value]
    return merged_dict

merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}, {}, {"E": 6, "D": 7})