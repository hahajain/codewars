def dirReduc(list):
    
    #new list to store the reduced directions
    redDir = []
    
    #flag to check if it is 1st iteration or not
    flag =1

    #loop till the list cannot be further reduced
    while len(list) != len(redDir):

        #if it is not first iteration
        #assign reduced list to current list
        if flag!=1:
            list=redDir
            redDir=[]

        
        i=0
        while i<len(list)-1:

            #check if the nearby list items lead to needless effort
            #else continue with next item in list
            if (list[i]=="NORTH" and list[i+1]=="SOUTH") or (list[i]=="EAST" and list[i+1]=="WEST") or (list[i]=="SOUTH" and list[i+1]=="NORTH") or (list[i]=="WEST" and list[i+1]=="EAST"):
                list[i]=""
                list[i+1]=""
                i +=2

            else:
                i +=1

        
        #add items which are not needless to reduced dimension list
        j=0
        while j<len(list):
            if list[j]!='':
                redDir.append(list[j])
            j+=1
        
        #update flag
        flag =0

    return redDir
