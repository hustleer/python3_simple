# python3_simple reusable codes

############# Progress Bar ####################<br>
-To show progress of current process.<br>
USAGE:<br>
  syntax: progress(current, total, bar_length)<br>
         	where default bar_length= 65<br>
  
  example: <br>
      from code.py import progress
      import time
      
      for i in range(1,100):
          progress(i,100)
          time.sleep(1)
