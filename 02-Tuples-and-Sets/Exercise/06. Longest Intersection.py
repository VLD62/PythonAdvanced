def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def longest_list(lsts):
    longest_lst = []
    for lst in lsts:
        if len(lst) > len(longest_lst):
            longest_lst = lst
    return longest_lst

if __name__ == "__main__":
    N = int(input())
    intersc = []
    for i in range(0,N):
        lst1, lst2 = input().split("-")
        lst1 = list(map(int,lst1.split(",")))
        lst2 = list(map(int,lst2.split(",")))
        new_lst1 = [i for i in range(lst1[0],lst1[1]+1)]
        new_lst2 = [i for i in range(lst2[0],lst2[1]+1)]
        intersc.append(intersection(new_lst1, new_lst2))
    longest_intrsc = longest_list(intersc)
    print(f'Longest intersection is {longest_intrsc} with length {len(longest_intrsc)}')
