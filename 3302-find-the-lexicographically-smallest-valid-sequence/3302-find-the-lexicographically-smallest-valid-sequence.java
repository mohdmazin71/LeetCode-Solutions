class Solution {
    public int[] validSequence(String word1, String word2) {
        char[] c1 = word1.toCharArray();
        char[] c2 = word2.toCharArray();
        int n = c1.length;
        int m = c2.length;
        
        // last[j] stores the rightmost possible index in word1 
        // that can match the suffix of word2 starting from index j
        int[] last = new int[m];
        java.util.Arrays.fill(last, -1);
        
        int j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; i--) {
            if (c1[i] == c2[j]) {
                last[j] = i;
                j--;
            }
        }
        
        int[] ans = new int[m];
        boolean canSkip = true; // Tracks if we can still change/skip 1 character
        j = 0;
        
        for (int i = 0; i < n; i++) {
            if (j == m) break;
            
            // Scenario 1: Natural exact character match
            if (c1[i] == c2[j]) {
                ans[j] = i;
                j++;
            } 
            // Scenario 2: Force a mismatch modification (Lexicographically greedy)
            else if (canSkip && (j == m - 1 || i < last[j + 1])) {
                canSkip = false;
                ans[j] = i;
                j++;
            }
        }
        
        // Return index array if entire word2 was successfully matched, else empty array
        return j == m ? ans : new int[0];
    }
}
