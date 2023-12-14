import math

def split_list(grade):
  list_less = []
  list_more = []

  if not len(grade):
      return list_less, list_more
  
  aver_sum = int(sum(grade) / len(grade))

  for value in grade:
      if value <= aver_sum:
        list_less.append(value)
      else:
          list_more.append(value)
  return list_less, list_more
       
    
  