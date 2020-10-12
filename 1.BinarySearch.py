def binary_search(list, item):   
    low = 0
    high = len(list) + 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if(guess == item):
            return mid
        if(guess > item):
            high = mid - 1
        else:
            low = mid + 1 
    return None

if __name__ == '__main__':
    list = [1, 3, 5, 6, 8]
    item = 6
    print(binary_search(list, item))