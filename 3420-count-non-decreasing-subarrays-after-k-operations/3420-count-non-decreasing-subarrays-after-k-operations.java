
import java.util.*;

class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {

        int n = nums.length;
        long ans = 0;
        long operations = 0;

        int right = n - 1;
        Deque<Integer> dq = new ArrayDeque<>();

        for (int left = n - 1; left >= 0; left--) {

            // Maintain decreasing values in deque
            while (!dq.isEmpty() &&
                   nums[dq.peekLast()] < nums[left]) {

                int index = dq.pollLast();

                int end = dq.isEmpty()
                        ? right + 1
                        : dq.peekLast();

                operations += (long)(end - index)
                              * (nums[left] - nums[index]);
            }

            dq.offerLast(left);

            // Reduce window if operations exceed k
            while (operations > k) {

                operations -= nums[dq.peekFirst()]
                              - nums[right];

                if (dq.peekFirst() == right) {
                    dq.pollFirst();
                }

                right--;
            }

            // Count valid subarrays
            ans += right - left + 1;
        }

        return ans;
    }
}
