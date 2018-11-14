def mix(s1, s2):
    
    #list to store all 
    #the occurrences of a char 
    #and the string it came from
    newlist=[]

    #loop using ascii values of all the lowercase letters
    for i in range(97,123):
    
        #count ith letter (a-z) in both strings
        
        count1 = s1.count(chr(i))
        count2 = s2.count(chr(i))
        
        # if count of letter is greater in a string than other
        #and count is greater than 1, append in specific format
        #i.e. stringnumber:no. of occurences of letter
        if count1 > count2 and count1 > 1:
            newlist.append('1:'+chr(i) * count1)
        if count2 > count1 and count2 > 1:
            newlist.append('2:' + chr(i) * count2)
        if count2 == count1 and count2 > 1:
            newlist.append('=:' + chr(i) * count1)

    #sort list in ascending order
    #list fields are sorted by number (i.e. string 1 or 2) &
    #then by the chars e.g 1:a before 2:a and 2:bb before 2.e
    newlist.sort()
    
    #finally sort by len in reverse, 
    #taking adv. of stable sort of python
    #e.g 2:aaa before 1:hh and so on
    newlist.sort(key=lambda x: len(x), reverse=True)
    
    #join the list with /
    final_str='/'.join(newlist)

    return final_str
