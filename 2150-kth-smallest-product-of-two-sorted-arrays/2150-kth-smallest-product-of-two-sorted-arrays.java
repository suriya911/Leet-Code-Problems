class Solution {
    int findPivot(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] >= 0)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        return lo;
    }

    long countLE(int[] X, int[] Y, long limit) {
        long cnt = 0;
        int j = Y.length - 1;
        for (int x : X) {
            while (j >= 0 && (long) x * Y[j] > limit)
                j--;
            cnt += j + 1;
        }
        return cnt;
    }

    int[] reverseNeg(int[] arr, int len) {
        int[] res = new int[len];
        for (int i = 0; i < len; i++)
            res[i] = -arr[len - 1 - i];
        return res;
    }

    public long kthSmallestProduct(int[] A, int[] B, long k) {
        int piv1 = findPivot(A);
        int piv2 = findPivot(B);

        int[] Apos = Arrays.copyOfRange(A, piv1, A.length);
        int[] Bpos = Arrays.copyOfRange(B, piv2, B.length);
        int[] Aneg = reverseNeg(A, piv1);
        int[] Bneg = reverseNeg(B, piv2);

        int negCnt = Aneg.length * Bpos.length + Apos.length * Bneg.length;
        long sign = 1;

        if (k > negCnt) {
            k -= negCnt;
        } else {
            int[] tmp = Bneg;
            Bneg = Bpos;
            Bpos = tmp;
            sign = -1;
            k = negCnt - k + 1;
        }

        long lo = 0, hi = (long) 1e10;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (countLE(Aneg, Bneg, mid) + countLE(Apos, Bpos, mid) >= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        return lo * sign;
    }

}
