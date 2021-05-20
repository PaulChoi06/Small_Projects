import random

def rand_arr(size=10, max=50):
    return [random.randint(0, max) for i in range(size)]

def merge(a,b):
    c = []

    a_ind, b_ind = 0, 0

    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind += 1
        else:
            c.append(b[b_ind])
            b_ind += 1

    if a_ind == len(a):
        c.extend(b[b_ind:])
    else:
        c.extend(a[a_ind:])

    return c

def merge_sort(a):
    if len(a) <= 1:
        return a

    left, right = merge_sort(a[:int(len(a)/2)]), merge_sort(a[int(len(a)/2):])

    return merge(left, right)


x = rand_arr()

print(x)
print(merge_sort(x))