  def heapify(ls, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and ls[i] < ls[l]:
          largest = l
  
      if r < n and ls[largest] < ls[r]:
          largest = r
 
      if largest != i:
          ls[i], ls[largest] = ls[largest], ls[i]
          heapify(ls, n, largest)
  
  
  def heapSort(ls):
      n = len(ls)
  
      for i in range(n//2, -1, -1):
          heapify(ls, n, i)
  
      for i in range(n-1, 0, -1):
 
          ls[i], ls[0] = ls[0], ls[i]
  
          heapify(ls, i, 0)
  
