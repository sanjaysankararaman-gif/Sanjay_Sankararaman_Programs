def bubble_sort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                t = l[j]
                l[j] = l[j+1]
                l[j+1] = t
    return l
