class Solution {

    public long dividePlayers(int[] skill) {
        int n = skill.length;
        int total = 0;
        int[] freq = new int[1001];
        for (int p : skill) {
            total += p;
            freq[p]++;
        }
        if (total % (n / 2) != 0) {
            return -1;
        }
        int target = total / (n / 2);
        long chem = 0;
        for (int p : skill) {
            int q = target - p;
            if (freq[q] == 0) {
                return -1;
            }

            chem += (long) p * (long) q;
            freq[q]--;
        }
        return chem / 2;
    }
}