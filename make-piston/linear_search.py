# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def lsearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 20
n = len(arr)
result = lsearch(arr, n, x)
if result:
    print(result)
else:
    print(result)

"""
*** une tonne de c1 = 400
*** une tonne de c2 = 500
*** machine M1 est dispo pour 6h de travail par jour
*** machine M2 est dispo pour 8h de travail par jour

______________________
Equation: tC1 = 40M1 + 20M2


"""