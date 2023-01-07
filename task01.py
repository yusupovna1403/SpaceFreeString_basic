def remove_spaces(s):
    """
    Removes all spaces from a string of fixed length of 5 characters.
    args:
        string: str
    returns:
        str
    """
    sum = ''
    idx = 0
    if s[idx] != " ":
        sum+=s[idx]
    idx+=1
    if s[idx] != " ":
        sum+=s[idx]
    idx+=1
    if s[idx] != " ":
        sum+=s[idx]
    idx+=1
    if s[idx] != " ":
        sum+=s[idx]
    idx+=1
    if s[idx] != " ":
        sum+=s[idx]
    return sum
print(remove_spaces('a b c'))


    
    