class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        int l = 0;
        int longestSubstring = 1;
        HashSet<Character> numSet = new HashSet<Character>();

        for (int r = 0; r < s.length(); r++) {
            if (numSet.contains(s.charAt(r))) {
                while (s.charAt(l) != s.charAt(r)) {
                    numSet.remove(s.charAt(l));
                    l++;
                }
                l++;
            } else {
                numSet.add(s.charAt(r));
                longestSubstring = Math.max(longestSubstring, numSet.size());
            }
        }

        return longestSubstring;

    }
}
