#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        return []
    
    return [num for num in num_list if num % 2 == 0]

return_evens([0, 1, 3, 5, 7, 8, 9])




def make_exclamation(sentence_list):
    my_char = "!"
    #if len(sentence_list) == 0:
        # return
    return [sentence + my_char for sentence in  sentence_list  if sentence_list[-1] != my_char ]
        
        

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
