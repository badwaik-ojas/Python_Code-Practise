def remove_char(s, ch):
    if s == "":
        return ''
    
    st = remove_char(s[1:], ch)

    if s[0] == ch:
        return st
    else:
        return s[0] + st
    
st = 'abdeetdddaaardssdd'

print(remove_char(st, 'd'))