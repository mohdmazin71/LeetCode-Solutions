class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        n=len(a); b=[10**9]*n; s=j=0; m=r=10**9
        for i,x in enumerate(a):
            s+=x
            while s>t: s-=a[j]; j+=1
            if s==t:
                m=i-j+1
                r=min(r,m+(b[j-1] if j else 10**9))
            b[i]=min(m,b[i-1] if i else 10**9)
        return -1 if r==10**9 else r