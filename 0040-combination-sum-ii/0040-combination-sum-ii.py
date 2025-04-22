class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        candidates.sort()
        def cs2helper(ind,tar,ds):
            if tar==0:
                ans.append(list(ds))
                return
            if ind==n:
                return 
            if candidates[ind]<=tar:
                ds.append(candidates[ind])
                cs2helper(ind+1,tar-candidates[ind],ds)
                ds.pop()
            next_ind=ind+1
            while next_ind<n and candidates[ind]==candidates[next_ind]:
                next_ind+=1
            cs2helper(next_ind,tar,ds)
        cs2helper(0,target,[])
        return ans
        