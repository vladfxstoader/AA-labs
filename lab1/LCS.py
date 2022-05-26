def readData(filename):
    f=open(filename)
    string1=f.readline().strip()
    string2=f.readline().strip()
    return string1, string2

def LCS(string1, string2, len1, len2):  # O(2^n)
    if len1==0 or len2==0:  # if we reached the end of one of the strings
        return 0
    elif string1[len1-1]==string2[len2-1]:  # if we have equals characters, we advance in both strings
        return 1+LCS(string1, string2, len1-1, len2-1)
    else:   # else, we take both options: we either iterate further through the first string, or through the second
        return max(LCS(string1, string2, len1, len2-1), LCS(string1, string2, len1-1, len2))


def LCS_ProgDin(string1, string2):  # O(len1*len2)
    len1=len(string1)
    len2=len(string2)
    L=[[None] * (len2+1) for i in range(len1+1)]

    # L[i][j] = length of LCS of string1[0..i-1] and string2[0..j-1]
    for i in range(len1+1):
        for j in range(len2+1):
            if i==0 or j==0:    # first column or first line
                L[i][j] = 0
            elif string1[i-1] == string2[j-1]:  # the characters in both strings are equal
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[len1][len2]

string1,string2=readData("lcs.in")
print(LCS(string1,string2,len(string1),len(string2)))
print(LCS_ProgDin(string1,string2))