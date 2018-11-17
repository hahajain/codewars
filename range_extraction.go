package kata

import(
      "strconv"
      "strings"
)

func Solution(list []int) string {
  
    //if list is empty return empty string
      if len(list) == 0{
        return ""}

    //var to store final string
    var string_final = ""
    
    //var to keep track of current index
    var ind=0
    
    //recursive sol to find the range
    string_final = recSolution(list, string_final, ind)

    //trim trailing "," and return final string
    string_final = strings.TrimRight(string_final,",")
    
    return string_final
    
}

//recursive solution to find the range
func recSolution(ls []int, str1 string, ind int)string{
    
    //check if we have reached end of list
    if ind == len(ls){
        return str1
    }
    
    var ind1 = nextind(ls, ind)

    //check and append if range is greater than or equal to 3
    if ind1 - ind >= 2{
        str1 = str1 + strconv.Itoa(ls[ind]) + "-" + strconv.Itoa(ls[ind1]) + ","
    
    }else{
    
        //check and append if there is no range and there is single element
        if ind1 == ind{
        str1 = str1 + strconv.Itoa(ls[ind]) + ","
        
        }else{
    
        //append individually if range is less than 3 
        str1 = str1 + strconv.Itoa(ls[ind]) + "," + strconv.Itoa(ls[ind1]) + ","
        }
    }
  return recSolution(ls, str1, ind1 + 1)
    
}
    
//function to find the next index
//upto which the values are back to back
func nextind(ls []int, ind int) int{

    //check if we have reached end of list
    //or if next value is not consecutive
    if ind == len(ls) - 1 || ls[ind] + 1 != ls[ind + 1]{
        return ind
    }else{
        return nextind(ls, ind + 1)
    }
}

  
