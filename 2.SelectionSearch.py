def find_smallest(arr):
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index

def select_search(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

if __name__ == "__main__":
    arr = [3, 2, 7, 5]
    print(select_search(arr)) 