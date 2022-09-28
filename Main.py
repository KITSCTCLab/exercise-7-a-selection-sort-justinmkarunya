from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(len(array)):
    minimum = i
    for j in range(i+1,len(array)):
      if array[j] < array[minimum]:
        minimum = j
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
