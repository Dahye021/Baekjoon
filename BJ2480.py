a , b , c = map(int,input().split())

if a == b == c :
    print (10000+a*1000)
elif a == b :
    print (1000+a*100)
elif a == c : 
    print (1000+a*100)
elif b == c :
    print (1000+b*100)
else :
    print (100*max(a,b,c))