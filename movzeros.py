def first_non_repeating_letter(string):
    strArr = [*string]
    for i in strArr:
        tmp = i
        index = strArr.index(tmp)
        strArr.pop(index)
        if tmp.upper() not in strArr:
            if tmp.lower() not in strArr: 
                return tmp
        strArr.insert(index,tmp)
    return None


print(first_non_repeating_letter('Stress'))
