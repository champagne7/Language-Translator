

# inorder = [2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20]
# postorder = [2, 4, 3, 9, 13, 7, 6, 17, 20, 18, 15]

def check(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            return False
    return True


def palindromes(a, i, k, temp, ans):
    if i==len(a):
        return
    if len(temp)==k: 
        if check(temp):
            t = [temp[j] for j in range(len(temp))]
            ans.append(t)
        return
    palindromes(a, i+1, k, temp+[a[i]], ans)
    palindromes(a, i+1, k, temp, ans)
    
from collections import defaultdict

def soln(a):
    d = defaultdict(int)
    for i in range(len(a)):
        d[a[i]]+=1
    res = []
    for i in range(len(a)):
        ans = []
        for j in range(len(a)):
            if i==j:
                break
            if d[a[j]]>1:
                ans.append(a[j])
                ans.append(a[i])
                ans.append(a[j])
        if len(ans)==3:
            res.append(ans)
    print(res)

a = [1, 3, 1, 2, 5, 2, 4, 4, 4, 6, 7, 5]
k = 3
# ans = []
# palindromes(a, 0, k, [], ans)
# print(ans)
print(soln(a))


