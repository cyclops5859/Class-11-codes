def bubblesort(elements):
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        elements[i], elements[i + 1] = elements[i + 1], elements[i]

elements = [69,12,108,85,72,10,92,18]

print("Unsorted list is", elements) 
bubblesort(elements)
print("Sorted Array is", elements)
