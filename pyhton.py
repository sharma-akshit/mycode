print ("linear search algorithm")
def linearsearch(list ,x):
    for i in list:
        if (i == x):
            return  i
    return - 1
list = [2,3,4,8,6,35]
x = int (input ("enter the nmber:"))
n =len(list )
result = linearsearch(list ,n,x)
if (result ==-1):
    print("element not found")
else:
    print("element found at index : ",result)
