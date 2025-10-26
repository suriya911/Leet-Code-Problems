class Bank {

private:
    vector<long long> bal;
    int n;
    bool valid(int acc){
        return acc>0 && acc<=n;
    }
public:
    Bank(vector<long long>& balance) {
        bal = balance;
        n=balance.size();
    }
    
    bool transfer(int account1, int account2, long long money) {
        if(valid(account1)&&valid(account2)&&bal[account1-1]>=money){
            bal[account1-1] -= money;
            bal[account2-1] += money;
            return true;
        }
        else{
            return false;
        }
    }
    
    bool deposit(int account, long long money) {
        if(valid(account)){
            bal[account-1] += money;
            cout<<bal[account-1]<<endl;;
            return true;
        }
        else{
            return false;
        }
    }
    
    bool withdraw(int account, long long money) {
        if(valid(account) && bal[account-1]>=money){
            bal[account-1] -= money;
            cout<<bal[account-1]<<endl;
            return true;
        }
        else{
            return false;
        }
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */