S=input()
alp=[-1]*26

for i in range(len(S)):
    if alp[ord(S[i])-97] != -1:
        continue
    else:
        alp[ord(S[i])-97]=i

for i in range(26):
    print(alp[i],end=' ')
