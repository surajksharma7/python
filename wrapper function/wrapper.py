import time 

# defining count function 
def count(n):
    for i in range(1,n):
        a = n*10


# this is starting time
# start = time.time()
# print(start,end='\n')
# # program execution 
# count(1_00_00_000)

# # end time 
# end = time.time()
# print(end,end='\n')
# # total time taken 
# print(end-start,end='\n')

# ns = [10,23,4,34,43]
# for i in ns:
#     start = time.time()
#     print(start,end='\n')
#     count(i)
#     print(time.time())


def funct(n):
    for i in n:
        start = time.time()
        print(start,end='\n')
        count(i)
        print(time.time())

funct(ns)