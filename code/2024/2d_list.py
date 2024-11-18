nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
search = int(input("Enter a number to search for: "))

def search_func(search):
    for i in range(3):
        for n in range(3):
            num = nums[i][n]
            if num == search:
                print("Found", search, "at index", i, n)
                return True
    return False
search_func(search)
