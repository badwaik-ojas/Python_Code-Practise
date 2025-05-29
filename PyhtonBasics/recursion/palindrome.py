def is_palindrome(st):

    if st == "":
        return True
    return helper(st, 0, len(st)-1)

def helper(st, start, end):
    if start >= end:
        return True
    if st[start] != st[end]:
        return False
    
    return helper(st, start+1, end-1)

st = 'malayalam'
print(is_palindrome(st))
st = 'ojas'
print(is_palindrome(st))

