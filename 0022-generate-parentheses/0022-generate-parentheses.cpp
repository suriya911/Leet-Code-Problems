class Solution {
public:

    void backtrack(int n, string& s, int open, int close, vector<string>& ans){
        if(s.length() == 2*n){
            ans.push_back(s);
            return;
        }

        if(open < n){
            s.push_back('(');
            backtrack(n,s,open+1,close,ans);
            s.pop_back();
        }

        if(close<open){
            s.push_back(')');
            backtrack(n,s,open,close+1,ans);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string s;
        backtrack(n,s,0,0,ans);
        return ans;
    }
};