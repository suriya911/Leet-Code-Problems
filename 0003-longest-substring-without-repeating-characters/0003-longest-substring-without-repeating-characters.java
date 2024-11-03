class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> indexmap = new HashMap<>();
        int max = 0;
        int left = 0;
        for(int right = 0;right<s.length(); right++){
            if(indexmap.containsKey(s.charAt(right))){
                left = Math.max(left,indexmap.get(s.charAt(right))+1);
            }
            indexmap.put(s.charAt(right),right);
            max = Math.max(max,right-left+1);
        }
        return max;
    }
}