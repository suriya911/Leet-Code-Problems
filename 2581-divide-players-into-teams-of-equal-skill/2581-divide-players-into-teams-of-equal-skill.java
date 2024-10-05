import java.util.*;

class Solution {
    public long dividePlayers(int[] skill) {
        long sum = 0;
        for (int s : skill) {
            sum += s;
        }

        int n = skill.length;

        if (n == 2) {
            return (long) skill[0] * skill[1];
        }

        if (sum % (n / 2) != 0) {
            return -1;
        }

        Arrays.sort(skill);

        int score = skill[0] + skill[n - 1];
        long result = 0;

        for (int i = 0; i < n / 2; i++) {
            int l = skill[i], r = skill[n - 1 - i];
            if (l + r != score) {
                return -1;
            }
            result += (long) l * r;
        }

        return result;
    }
}