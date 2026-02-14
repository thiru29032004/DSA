class Solution {
    public void reverseNums(int[] nums,int start,int end){
        while(start<end){
            int temp=nums[start];
            nums[start]=nums[end];
            nums[end]=temp;
            start++;end--;
        }
    }
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%(n);
        reverseNums(nums,n-k,n-1);
        reverseNums(nums,0,n-k-1);
        reverseNums(nums,0,n-1);
        

    }
}