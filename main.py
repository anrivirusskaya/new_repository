def merge(*lists):
    k = len(lists)
    list1=[]
    for i in range(0,k):
        small_list = lists[i]
        list1.extend(small_list)
    list1.sort()
    print(list1)





