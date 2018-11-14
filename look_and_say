def look_and_say(data='1', maxlen=5):
  
  seqlist=[]    #list to store the sequence
  n=maxlen      #store the maxlen of the sequence
  
  #base case
  if data=='1': 
    seqlist.append('11') 
    seq = str(11)    #initialise the first sequence
  else:
    seq = data       #initialise for cases other than base case
    n+=1                


  #Find all the terms of sequence
  #Each sequence is generated using the previous sequence
  for i in range(0, n-1):    

    #length of the sequence   
    l = len(seq) 
    j = 0
    
    #temporary variable to store the sequence
    temp = ""    

    #for jth index of the previous sequence 
    #find the number of occurrences of a particular number in a sequence
    #count var keeps the track of occurrences
    #count is intialised to 1 for new number
    while j< l-1:  
        count = 1
        
        #loop to find the number of occurrences of a number
        while j < l-1 and seq[j] == seq[j + 1]:
            count += 1
            j += 1

        temp += str(count)
        temp += str(seq[j])
        j += 1

        #special case when there is single occurrence 
        #of a number at the end of the sequence
        
        if j == l-1:
            temp += str(1)
            temp += str(seq[j])
    
    #save the temp into seq for next iteration
    seq = temp
    #add the generated sequence to the list
    seqlist.append(seq)
    
  return seqlist
