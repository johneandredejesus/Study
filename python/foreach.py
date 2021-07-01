def foreach(callback, start, stop, step=0):
  
    if stop == start:
        return start
    else:
        callback(start)
        
        start = start + 1 if step == 0  else  start + step  
        
        return foreach(callback, start, stop, step)

 
def callback(count):
    print(count)

foreach(callback, 0, 10)
