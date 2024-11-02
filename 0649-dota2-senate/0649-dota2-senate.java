class Solution {
    public String predictPartyVictory(String senate) {

        char[] c = senate.toCharArray();
        return solve(c,0);

    }

    public String solve(char[] c , int vote){

        int r = 0 , d = 0;

        for(int i=0;i<c.length;i++){
            if(c[i] == 'R'){
                if(vote >= 0) r++;
                else c[i] = '0';
                vote++;
            }else if(c[i] == 'D'){
                if(vote <= 0) d++;
                else c[i] = '0';
                vote--;
            }
        }

        if(r != 0 && d == 0) return "Radiant";
        if(d != 0 && r == 0) return "Dire";
        return solve(c,vote);
    }
}