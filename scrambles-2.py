def scramble(s1, s2):
    for i in s2:
        if i in s1:
            s1 = s1.replace(i,'',1)
        else:
            return False
    return True
    