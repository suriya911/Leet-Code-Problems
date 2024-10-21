class Solution {
    public int maxUniqueSplit(String s) {
        return backtrack(0,s,new HashSet<>());
    }
    private int backtrack(int n, String s, HashSet<String> seen){
        if(n == s.length()){
            return 0;
        }
        int maxSplits = 0;
        for(int e = n+1; e <= s.length(); e++){
            String sub = s.substring(n,e);
            if(!seen.contains(sub)){
                seen.add(sub);
                maxSplits = Math.max(maxSplits, 1 + backtrack(e,s,seen));
                seen.remove(sub);
            }
        }
        return maxSplits;
    }
}