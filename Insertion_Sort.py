data = [5,6,4,2,1,2,8,1,9]

def Insertion_Sort(data):
    new = []   
    for i in data:
        new.append(i)
        for count in range(0,len(new)-1): 
            if i <= new[count]:
                print(new)
                new.insert(count,i)
                del new[-1]
                break
    return new

def Binary_Search(key,data):
    up = len(data)-1
    mid = int(round(up/2,0))
    low = 0
    while True:
        if key == data[mid]:
            return f'index : {mid} Value :{data[mid]}'
        if key >= data[mid]:
            low = mid 
        else:
            up =  mid
        chack = mid
        mid = int(round((up+low)/2,0))  
        if mid == chack:
            return "data not fount."

data = Insertion_Sort(data)
print(data)
print(Binary_Search(key=5,data=data))
        