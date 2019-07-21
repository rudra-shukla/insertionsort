x = [4,89,12,9,66,78,82]

def insertion(a): 
 c = 0
 for j in range(1,len(a)):
   key = a[j];
   i = j-1
   while i>=0 and a[i]>key:
        a[i+1] = a[i];
        i = i-1;
        c = c+1;
   a[i+1] = key;
 print(c)


insertion(x);
print(x)  
  


