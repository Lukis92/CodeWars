# https://www.codewars.com/kata/5747fcfce2fab91f43000697/train/python
def example_sort(arr, example_arr):
    rank = {x: i for i, x in enumerate(example_arr)}

    try:
        return sorted(arr, key=lambda x: rank[x])
    except KeyError as e:
        raise ValueError(f"Missing value in rank: {e}")

example_sort([1,2,3,4,5],[2,3,4,1,5])