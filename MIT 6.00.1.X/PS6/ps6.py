def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


print(search([3, 4, 1, 2, 3, 4, 3, 43, 4, 90, 909], 2101))
print(newsearch([3, 4, 1, 2, 3, 4, 3, 43, 4, 90, 909], 2101))
