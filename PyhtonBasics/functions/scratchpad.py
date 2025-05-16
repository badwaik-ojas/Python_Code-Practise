def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    s1 = list(i for i in s.lower())
    s2 = list(i for i in t.lower())
    pat = []
    if s2 == []:
        return True
    for i in s2:
        if i in s1:
            pat.append(i)
        if i not in s1:
            return False
    print(pat)
    print(s2)
    return s2 == pat

print(is_subsequence("abcde", "aec"))