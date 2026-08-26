class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int l = 0, ones = 0;
        String ans = "";

        for (int r = 0; r < s.length(); r++) {
            if (s.charAt(r) == '1') ones++;

            while (ones > k) {
                if (s.charAt(l++) == '1') ones--;
            }

            if (ones == k) {
                while (s.charAt(l) == '0') l++;

                String cur = s.substring(l, r + 1);

                if (ans.equals("") || cur.length() < ans.length()
                    || (cur.length() == ans.length() && cur.compareTo(ans) < 0))
                    ans = cur;
            }
        }

        return ans;
    }
}