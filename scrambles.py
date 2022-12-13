def scramble(s1, s2):
    for i in s2:
        if i not in s1:
            return False
        s1 = s1.replace(i,'',1)
    return True
            