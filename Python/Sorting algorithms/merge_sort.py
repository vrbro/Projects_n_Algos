'''
Merge sort
'''

def merge ( lst1 , lst2 ):
    '''
    This function merges 2 lists.
    :param lst1:
    :param lst2:
    :return list 1 merged with list 2:

    >>> merge ([1, 2, 4, 6] ,[3, 5, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    res = []
    n1 , n2 = len( lst1 ) , len( lst2 )
    i , j = 0 , 0
    while i < n1 and j < n2 :
        if lst1 [ i ] <= lst2 [ j ]:
            res += [ lst1 [ i ]]
            i += 1
        else :
            res += [ lst2 [ j ]]
            j += 1
    return res + lst1 [ i :] + lst2 [ j :]


def merge_sort ( lst ):
    '''
    :param lst:
    :return sorted list:

    Input : list of elements
    Output : Sorted list of elements
    >>> merge_sort ([3, 7, 9, 6, 2, 5, 4, 1, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> merge_sort ([11, 0, 1, 5, 7, 2])
    [0, 1, 2, 5, 7, 11]
    >>> merge_sort ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    '''
    k , n = 1 , len ( lst )
    while k < n :
        nxt = []
        for a in range (0 , n , 2* k ):
            b , c = a + k , a + 2* k
            nxt += merge ( lst [ a : b ] , lst [ b : c ])
        lst = nxt
        k = 2* k
    return lst