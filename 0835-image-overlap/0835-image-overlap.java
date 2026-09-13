class Solution {
    public int largestOverlap(int[][] a, int[][] b) {
        int n = a.length, ans = 0;

        for (int x = -n + 1; x < n; x++)
            for (int y = -n + 1; y < n; y++) {
                int count = 0;

                for (int i = 0; i < n; i++)
                    for (int j = 0; j < n; j++) {
                        int r = i + x, c = j + y;
                        if (r >= 0 && r < n && c >= 0 && c < n)
                            count += a[i][j] & b[r][c];
                    }

                ans = Math.max(ans, count);
            }

        return ans;
    }
}
