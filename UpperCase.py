def convert_to_upper(s):
    result=" "
    for i in s:
        if 'a'<=i<='z':
            result+=chr(ord(i)-32)
        else:
            result+=i
    return result
        
a="aAabb"
print(convert_to_upper(a))

#AAABB
#use +32 for lowercase