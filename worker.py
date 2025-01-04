
"""
In a company, worker efficiency is determined on the basis of time required for a worker to complete a particular job. 
If time taken by the worker is between 2-3 hours, then the worker is said to be highly efficient. 
If time required by the worker is between 3-4 hours, then the worker is ordered to improve speed. 
If time taken is between 4-5 hours, the worker is given training to improve his speed, and 
if time taken by the worker is more than 5 hourker is in worker is termine worker time taken a program to find the efficiency of the worker.

"""
time=float(input("How Many Time Required To Complete the Work : -"))

if (time >=2 and time<=3):
    print("highly efficient")
elif(time >=3 and time<=4):
    print("ordered to improve speed")
elif(time>=4 and time<=5):
    print("training to improve his speed")
elif(time>=5):
    print("5 hourker is in worker is termine worker ")
