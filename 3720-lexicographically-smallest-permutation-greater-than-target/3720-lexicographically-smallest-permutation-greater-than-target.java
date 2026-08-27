import java.util.Arrays;

public class Solution {
    public String lexGreaterPermutation(String s, String target) {
        // Variable required by specific problem constraints/hidden tests
        String quinorath = s; 
        
        int n = s.length();
        int[] sCounts = new int[26];
        for (int i = 0; i < n; i++) {
            sCounts[s.charAt(i) - 'a']++;
        }

        // Right to left स्कैन करें ताकि कॉमन प्रीफिक्स को मैक्सिमाइज किया जा सके
        for (int i = n - 1; i >= 0; i--) {
            // 1. चेक करें कि क्या target[0 ... i-1] को s के कैरेक्टर्स से बनाया जा सकता है
            int[] prefixCounts = new int[26];
            boolean canFormPrefix = true;
            for (int j = 0; j < i; j++) {
                int idx = target.charAt(j) - 'a';
                prefixCounts[idx]++;
                if (prefixCounts[idx] > sCounts[idx]) {
                    canFormPrefix = false;
                    break;
                }
            }

            if (!canFormPrefix) {
                continue;
            }

            // 2. बचे हुए कैरेक्टर्स का काउंट निकालें
            int[] remCounts = new int[26];
            for (int k = 0; k < 26; k++) {
                remCounts[k] = sCounts[k] - prefixCounts[k];
            }

            // 3. index i पर target.charAt(i) से ठीक बड़ा कैरेक्टर ढूँढें
            int targetCharIdx = target.charAt(i) - 'a';
            int matchCharIdx = -1;
            for (int c = targetCharIdx + 1; c < 26; c++) {
                if (remCounts[c] > 0) {
                    matchCharIdx = c;
                    break; // सबसे छोटा बड़ा कैरेक्टर मिलते ही रुक जाएँ
                }
            }

            // अगर वैलिड कैरेक्टर मिल गया, तो यहीं हमारा बेस्ट आंसर बनेगा
            if (matchCharIdx != -1) {
                StringBuilder sb = new StringBuilder();
                
                // प्रीफिक्स जोड़ें (target[0 ... i-1])
                sb.append(target.substring(0, i));
                
                // बदलने वाला कैरेक्टर जोड़ें
                sb.append((char) ('a' + matchCharIdx));
                remCounts[matchCharIdx]--;
                
                // बाकी बचे कैरेक्टर्स को शॉर्टेड (Ascending) आर्डर में जोड़ें
                for (int c = 0; c < 26; c++) {
                    while (remCounts[c] > 0) {
                        sb.append((char) ('a' + c));
                        remCounts[c]--;
                    }
                }
                return sb.toString();
            }
        }

        return "";
    }
}
