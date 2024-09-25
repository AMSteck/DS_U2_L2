#Alannah Steck
#U2L2
#DynamicArray class
import ctypes

class DynamicArray:
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()

  def __str__(self):
    if self.__n == 0:
        return "[]"
    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'

  def __resize(self):
    self.__capacity = self.__n * 2

  def append(self,item):
    if self.__capacity <= self.__n:
      self.__resize()
    try:
      ArrayStr = " ".join(self.__A)
      x = type(item)
      strItem = str(item)
      ArrayStr += f" {item}"
      ArrayList = ArrayStr.split(" ")
      if x == int:
        ArrayList[self.__n] = int(ArrayList[self.__n])
      elif x == bool:
        ArrayList[self.__n] = bool(ArrayList[self.__n])
      elif x == float:
        ArrayList[self.__n] = float(ArrayList[self.__n])
    except:
      ArrayList =[item]
      
    self.__A = ArrayList
    self.__n += 1
    return self.__A
    

  def __len__(self):
    return self.__n

  def get_cap(self):
    return self.__capacity

  
  def __getitem__(self, k):
      """return element at index"""
      if k <= 0 or k >= self.__n:
          raise IndexError("invalid index")
    
      return self.__A[k]
