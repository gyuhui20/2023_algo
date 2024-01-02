__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: heap.py 2023-02-02'

"""
Heap homework
2023-02 - S2
@author: gyuhui.kwon
"""

#given function

def Heap():
    """ returns a fresh new empty heap
    
       :rtype: list (heap)
    """
    return [None]
    
###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import


    
def isempty(H):
    """ tests if the heap H is empty -> bool
    """
    if H == [None] : 
        return True
    else : 
        return False 

def heappush(H, elt, val):
    """ adds the pair (val, elt) to heap H (in place: no need to return H)
    """
    H.append(((val,elt)))
    import_idx = len(H)-1
    parent_idx = import_idx // 2
    while parent_idx > 0:
        if H[import_idx][0] < H[parent_idx][0] :
            H[import_idx], H[parent_idx] = H[parent_idx], H[import_idx]
            import_idx = parent_idx
            parent_idx = import_idx // 2
        else :
            break

def heappop(H) :
    """ removes and returns the pair of smallest value in the heap H
    	 return: (num, any) (the removed pair)
    """
    if len(H) <= 1 :
        raise Exception("empty heap")
    parent_idx = 1 
    idx = parent_idx * 2 
    min = H[1]
    H[1]=H[-1]
    del H[-1]
    while True :
        if idx >= len(H) :
            break 
        elif idx+1 >= len(H) : 
            if H[idx] < H[parent_idx] :
                H[parent_idx], H[idx] = H[idx], H[parent_idx]
                parent_idx=idx
                idx = parent_idx * 2 
            else : 
                break
        else : 
            if H[idx] > H[idx+1] :
                if H[idx+1] < H[parent_idx] :
                    H[parent_idx], H[idx+1] = H[idx+1], H[parent_idx]
                    parent_idx=idx+1
                    idx = parent_idx * 2
                else: 
                    break
            else:
                if H[idx] < H[parent_idx] :
                    H[parent_idx], H[idx] = H[idx], H[parent_idx]
                    parent_idx=idx
                    idx = parent_idx * 2
                else: 
                    break
    return min
#---------------------------------------------------------------
def isheap(T):
    """ tests whether the complete tree T (in hierarchical implementation) is a heap -> bool
    """
    if len(T) <= 2 :
        return True
    for idx in range(2, len(T)) :
        parent_idx = idx // 2
        if idx >= len(T) :
            break 
        elif idx+1 >= len(T) : 
            if T[idx] < T[parent_idx] :
                return False
            else :
                break
        else :
            if T[idx] > T[idx+1] :
                if T[idx+1] < T[parent_idx] :
                    return False
                else : 
                    break
            else :
                if T[idx] < T[parent_idx] :
                    return False
                else : 
                    break
    return True

def heapsort(L):
    """ sorts the associative list of (elements, values) L in increasing order according to values (not in place)
    	return: (any, num) list (the new list sorted)
    """
    for i in range(len(L)-1) :
        k = i
        while (k>=0) and (L[k][1] > L[k+1][1]) :
            temp = L[k]
            L[k] = L[k+1]
            L[k+1] = temp
            k -= 1
    return(L)
