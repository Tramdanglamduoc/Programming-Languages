
'''
Ngoc Bao Tram Tran 
231ADB294 '''

#Exercise 1
testing = str(input("Enter any number: "))

def get_num_count(num):
    digit_count = {str(d): 0 for d in range(10)} 
    
    for digit in str(num):
        if digit in digit_count:
            digit_count[digit] += 1
            
    return digit_count

print(get_num_count("126181"))
print(get_num_count(testing)) 

#Exercise 2
testing = str(input("Enter the sequence of number or a string: ))

def get_min_med_max(sequence):
    sorted_sequence = sorted(sequence)
    minimum = sorted_sequence[0]
    maximum = sorted_sequence[-1]
    
    n = len(sorted_sequence)
    if n % 2 == 1:
        median = sorted_sequence[n // 2] 
    else:
        if isinstance(sequence, str):
            median = sorted_sequence[n // 2 - 1] + sorted_sequence[n // 2]  
        else:
            median = (sorted_sequence[n // 2 - 1] + sorted_sequence[n // 2]) / 2  
    
    return (minimum, median, maximum)

print(get_min_med_max([0, 9, 2, 5, 3]))        
print(get_min_med_max([9, 9, 2, 2, 4, 3]))     
print(get_min_med_max("baaac"))                
print(get_min_med_max("faaacb"))
print(get_min_med_max(testing))

#Exercise 3
testing = str(input("Enter the input string: "))

def unique_words_count(sequence):
    words = sequence.lower().split()
    unique_words = set(words)
    unique_count = len(unique_words)
    return f"{unique_count} unique words:", unique_words
    
print(unique_words_count("Python is fun and python is easy to learn"))
print(unique_words_count(testing))

     
