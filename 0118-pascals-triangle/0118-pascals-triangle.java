class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        
        if(numRows == 1){
            List<Integer> col = new ArrayList<>();
            col.add(1);
            res.add(col);
            return res;
        }

        res = generate(numRows-1);
        List<Integer> p = res.get(numRows-2);
        List<Integer> c = new ArrayList<>();
        c.add(1);
        for(int i=1;i<numRows-1;i++){
            c.add(p.get(i-1) + p.get(i));
        }
        c.add(1);
        res.add(c);
        return res;
    }
}