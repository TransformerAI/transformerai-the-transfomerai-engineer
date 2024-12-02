public class Solution7 {

    public int combinationSum4(int[] nums, int target) {
        int len = nums.length;
        if (len == 0) {
            return 0;
        }

        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (num <= i) {
                    dp[i] = dp[i] + dp[i - num];
                }
            }
        }
        return dp[target];
    }
}