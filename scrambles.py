def scramble(s1, s2):
    for i in s2:
        if i in s1:
            s1 = s1.replace(i,'',1)
        else:
            return False
    return True
    
#  This approach only passes 510 test cases while the one above passes 512 but both timeout for some reason
# def scramble(s1, s2):
#     for i in s2:
#         if i not in s1:
#             return False
#         s1 = s1.replace(i,'',1)
#     return True
            