def selectsort(x):
    for i in range(len(x)):
        minidx = i
        for j in range(i, len(x)):
            if x[j] < x[minidx]:
                minidx = j
        x[i] , x[minidx] = x[minidx], x[i]
    return x


def insert_sort(x):
    for i in range(1, len(x)):
        idx = i
        data = x[i]

        # for j in range(i, 0, -1):
        #     if x[j] < x[j-1]:
        #         x[j] = x[j-1]
        #         x[j-1] = data
        #     else:
        #         pass

        while x[idx]<x[idx-1] and idx > 0:
            x[idx] = x[idx - 1]
            idx -= 1
        x[idx] = data
    return x


a = [2,6,3,9,8]
print(insert_sort(a))