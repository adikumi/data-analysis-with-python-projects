import numpy as np

def calculate(l):
    while True :
      try :
        arr = np.array(l).reshape(3, 3)
        # mean  
        mean_arr = list([list(arr.mean(axis = 0)), list(arr.mean(axis = 1)), arr.mean()])
        # variance
        var_arr = list([list(arr.var(axis = 0)), list(arr.var(axis = 1)), arr.var()])
        # standard deviation
        std_arr = list([list(arr.std(axis = 0)), list(arr.std(axis = 1)), arr.std()])
        # max
        max_arr = list([list(arr.max(axis = 0)), list(arr.max(axis = 1)), arr.max()])
        # min
        min_arr = list([list(arr.min(axis = 0)), list(arr.min(axis = 1)), arr.min()])
        # sum
        sum_arr = list([list(arr.sum(axis = 0)), list(arr.sum(axis = 1)), arr.sum()])
        # dictionart with all values
        calculations = {'mean': mean_arr,
                        'variance': var_arr,
                        'standard deviation': std_arr,
                        'max': max_arr,
                        'min': min_arr,
                        'sum': sum_arr
                      }
        return calculations
      except:
        # ValueError
        if len(l) != 9: raise ValueError('List must contain nine numbers.')
    