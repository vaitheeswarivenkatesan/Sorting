def partition(ls, l, h): 
    i = (l-1)          
    pivot = ls[h] 
      
    for j in range(l, h): 
        if ls[j] <= pivot: 
            i = i+1
            ls[i], ls[j] = ls[j], ls[i] 
    ls[i+1], ls[h] = ls[h], ls[i+1] 
    return (i+1) 
  

def quick_sort(ls, l, h): 
    if len(ls) == 1: 
        return ls
    if l < h: 
  
        pi = partition(ls, l, h) 
  
        quickSort(ls, l, pi-1) 
        quickSort(ls, pi+1, h) 
