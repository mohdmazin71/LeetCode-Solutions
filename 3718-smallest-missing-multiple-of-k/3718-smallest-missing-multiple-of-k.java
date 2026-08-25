class Solution {
    public int missingMultiple(int[] nums, int k) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();

        for (int x : nums)
            if (x % k == 0)
                set.add(x);

        int ans = k;

        while (set.contains(ans))
            ans += k;

        return ans;
    }
}