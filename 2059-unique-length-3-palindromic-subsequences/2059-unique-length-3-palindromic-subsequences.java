import java.util.*;

class Solution {
    public int countPalindromicSubsequence(String s) {
        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.putIfAbsent(s.charAt(i), new ArrayList<>());
            map.get(s.charAt(i)).add(i);
        }

        int ans = 0;
        for (Map.Entry<Character, List<Integer>> entry : map.entrySet()) {
            List<Integer> indices = entry.getValue();
            int start = indices.get(0);
            int end = indices.get(indices.size() - 1);

            if (end - start <= 1) {
                continue;
            }

            Set<Character> seen = new HashSet<>();
            for (int i = start + 1; i < end; i++) {
                seen.add(s.charAt(i));
            }
            ans += seen.size();
        }

        return ans;
    }
}