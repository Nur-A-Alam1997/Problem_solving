c=0
s1="abcbabcsbabcscabc"
s2="abc"
for i in range((len(s1)-len(s2))+1):
    # print(i)
    if s1[i:i+len(s2)]==s2:
        print(c,i)
        c+=1
        