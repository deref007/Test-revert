
def search_Substring(s):
    lookup=set()
    left=0
    cur_len=0
    max_len=0
    for i in range(len(s)):
        while s[i] in lookup:
            lookup.remove(s[left])
            left=left+1
            cur_len=cur_len-1
        lookup.add(s[i])
        cur_len=cur_len+1
        if cur_len>max_len:max_len=cur_len
    return print(max_len)
s=input().split()
s=map(str,s)
s=list(s)
search_Substring(s)