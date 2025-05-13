using namespace std;

class Solution {
public:
    static constexpr int MOD = 1000000007;

    int lengthAfterTransformations(const string& s, long long t) {
        array<long long, 26> freq{};
        for (char c : s) {
            freq[c - 'a']++;
        }

        while (t >= 26) {
            array<long long, 26> temp{};
            for (int j = 0; j < 25; j++) {
                temp[j + 1] += freq[j];
                temp[j]     += freq[j];
            }
            temp[25] += freq[25];
            temp[0]  += freq[25];
            temp[1]  += freq[25];

            for (int i = 0; i < 26; i++) {
                freq[i] = temp[i] % MOD;
            }

            t -= 26;
        }

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (t >= 26 - i) {
                freq[i] = (freq[i] * 2) % MOD;
            }
            ans = (ans + freq[i]) % MOD;
        }

        return ans;
    }
};
struct FastIO {
    FastIO() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
} fastio;