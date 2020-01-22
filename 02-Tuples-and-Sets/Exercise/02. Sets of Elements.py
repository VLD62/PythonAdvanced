if __name__ == "__main__":
    n, m = input().split()
    n_set = set()
    m_set = set()
    for i in range(0,int(n)):
        n_set.add(input())
    for i in range(0,int(m)):
        m_set.add(input())
    total_set = n_set.union(m_set)
    for element in total_set:
        if element in n_set and element in m_set:
            print(element)
