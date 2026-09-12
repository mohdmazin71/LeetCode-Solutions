import java.util.*;

class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        int n = intervals.size();
        List<Interval> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new Interval(intervals.get(i).get(0), intervals.get(i).get(1), intervals.get(i).get(2), i));
        }
        
        list.sort(Comparator.comparingInt(a -> a.right));
        
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            ends[i] = list.get(i).right;
        }
        
        Result[][] dp = new Result[n + 1][5];
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= 4; k++) {
                dp[i][k] = new Result(-1, new ArrayList<>());
            }
        }
        
        for (int k = 1; k <= 4; k++) {
            dp[0][k] = new Result(0, new ArrayList<>());
        }
        dp[0][0] = new Result(0, new ArrayList<>());
        
        for (int i = 1; i <= n; i++) {
            Interval curr = list.get(i - 1);
            int prevIdx = binarySearch(list, i - 1, curr.left);
            
            for (int k = 0; k <= 4; k++) {
                dp[i][k] = dp[i - 1][k];
                
                if (k > 0 && dp[prevIdx + 1][k - 1].weight != -1) {
                    long newWeight = dp[prevIdx + 1][k - 1].weight + curr.weight;
                    List<Integer> newIndices = new ArrayList<>(dp[prevIdx + 1][k - 1].indices);
                    newIndices.add(curr.origIdx);
                    Collections.sort(newIndices);
                    
                    Result candidate = new Result(newWeight, newIndices);
                    if (compare(candidate, dp[i][k]) > 0) {
                        dp[i][k] = candidate;
                    }
                }
            }
        }
        
        Result best = new Result(-1, new ArrayList<>());
        for (int k = 0; k <= 4; k++) {
            if (compare(dp[n][k], best) > 0) {
                best = dp[n][k];
            }
        }
        
        int[] res = new int[best.indices.size()];
        for (int i = 0; i < best.indices.size(); i++) {
            res[i] = best.indices.get(i);
        }
        return res;
    }
    
    private int binarySearch(List<Interval> list, int limit, int targetLeft) {
        int low = 0, high = limit - 1, ans = -1;
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (list.get(mid).right < targetLeft) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private int compare(Result a, Result b) {
        if (a.weight != b.weight) {
            return Long.compare(a.weight, b.weight);
        }
        // Lexicographically smallest comparison (reverse order for matching smallest array)
        int size = Math.min(a.indices.size(), b.indices.size());
        for (int i = 0; i < size; i++) {
            int cmp = Integer.compare(b.indices.get(i), a.indices.get(i));
            if (cmp != 0) return cmp;
        }
        return Integer.compare(b.indices.size(), a.indices.size());
    }
    
    private static class Interval {
        int left, right, weight, origIdx;
        Interval(int left, int right, int weight, int origIdx) {
            this.left = left;
            this.right = right;
            this.weight = weight;
            this.origIdx = origIdx;
        }
    }
    
    private static class Result {
        long weight;
        List<Integer> indices;
        Result(long weight, List<Integer> indices) {
            this.weight = weight;
            this.indices = indices;
        }
    }
}
