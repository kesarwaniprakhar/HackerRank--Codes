n = int(input())

c = list(map(int, input().rstrip().split()))

def jumpingOnClouds(c):
    hop = i = 0              #starting with i as 0
    while(i<len(c)-1):     #taking a loop until complete array is traversed
        if (i + 2) <= len(c)-1 :   #if condition to check the array is not going out of bound and if there exits- 
                                   # - an alternate element which might be 0. 
            
            if c[i+2] == 0:        #if alternate element is 0 then this will be the shorter path
                hop += 1           #increase the value of hop by 1
                i += 2             #increase the value of i by 2
             
                
                                   #remember there could be no consecutive 1's
            
            else:                  # else if alternate element is 1 then take the consecutive element of the i.
                hop += 1           #increase the value of hop by 1 
                i += 1             #increase the value of i by 1
        
        else:             #if the alternate element is not 0 or is 1. 
            hop += 1
            i += 1 
            
            
    print(hop)
    
jumpingOnClouds(c)    



        
    
    
    
    

    

