import sys

def makingAnagrams(s1, s2):
    # Complete this function
    
    list_s1 = list(s1)
    list_s2 = list(s2)
    s1_values = list(s1)
    for i in s1_values:
        if i in list_s2:
            list_s1.remove(i)
            list_s2.remove(i)
            
    return len(list_s1) + len(list_s2)
            
  
        
     
        

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
