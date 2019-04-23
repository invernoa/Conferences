m = {}
arr = []

def add(k):
    arr.append(k)
    m[k] = len(arr) - 1

def delete(k):
    i = m[k]
    del m[k]
    arr[i] = arr[-1]
    del arr[-1]

def get_rand():
    return arr[randint(len(arr))]