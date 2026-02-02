class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> ps= new HashMap<>();
        int[] ans= new int[2];
        for(int i=0;i<nums.length;i++){
            int element2=target-nums[i];
            if(ps.containsKey(element2)){
                ans[0]=ps.get(element2);
                ans[1]=i;
                return ans;
            }else{
                ps.put(nums[i],i);
            }
        }
        return ans;
    }
}