
def count_digits(s):
    """
    Count the number of digits in a string of fixed length.
    args:
        string: string of fixed length
    returns:
        number of digits in the string
    """
    sum = 0
    idx = 0
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    return sum
    
print(count_digits("a1b23c"))

    # Your code goes here
