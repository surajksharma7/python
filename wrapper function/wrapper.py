import time 

# # defining count function 
# def count(n):
#     for i in range(1,n):
#         a = n*10


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

ns = [10,23,4,34,43]
# for i in ns:
#     start = time.time()
#     print(start,end='\n')
#     count(i)
#     print(time.time())


# def funct(n):
#     for i in n:
#         start = time.time() * 1_000_000
#         # print(start,end='\n')
#         count(i)
#         end = time.time() * 1_000_000
#         print(f"the time taken to execute is {end - start} microsecond")
# funct(ns)



# wrapper class code 
def wrapper(func,*args,**kwargs):
    def wrapped(*args,**kwargs):
        start_time = time.time()
        func(n)
        end_time = time.time()
        print(f"the time taken to execute is {end_time - start_time} microsecond")
    
    return wrapped

# normal count function 
@wrapper
def count(n):
    for i in range(0,n):
        a = n*10

# value of n
n = 10000


wrapped_function = wrapper(count,n)
wrapped_function(n)
    

