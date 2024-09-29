def isPalindrome(s):

    s = ''.join([char.lower() for char in s if char.isalnum()])
    if not s:
        return True
    fstIdx = 0
    lstIdx = len(s) - 1
    while fstIdx <= lstIdx:
        if s[fstIdx] != s[lstIdx]:
            return False
        fstIdx += 1
        lstIdx -= 1
        
    return True

response = isPalindrome("A man, a plan, a canal: Panama")
print(response)