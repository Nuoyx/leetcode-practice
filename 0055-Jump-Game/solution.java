class Solution {
    public boolean canJump(int[] nums) {
        int max = nums[0];
        int temp = 0;
        for(int i = 1; i < nums.length; i++){
            if(i > max || max >= nums.length-1){
                break;
            }
            temp = i + nums[i];
            if (temp > max){
                max = temp;
            }
        }
        return max >= nums.length-1;

    }
}