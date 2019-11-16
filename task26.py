def count_even_odd():
    x=[1,2,3,4,5,6,7,11]
    odd=0
    even=0
    i=0
    counter=0
    while counter!=len(x):
        if x[i]%2==1 or  x[i]==1:
            odd+=1
            i+=1
            counter+=1
        else:
            even+=1
            i+=1
            counter+=1
    return 'even:'+str(even) +'and odd:'+str(odd)
print(count_even_odd())