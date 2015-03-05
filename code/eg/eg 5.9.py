def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    elif len(str1) == 1 or len (str2) == 1:
        return False
    
    elif str1[0] != str2[-1]:
        return False
    elif str1[len(str1)-1] == str2[-len(str2)]:
        return True
    else:
        return semordnilap(str1[1:],str2[:-1])
    