class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int drink = numBottles;
        int empty = 0;
        int sum = 0;
        while(drink+empty >= numExchange){
            sum += drink;
            empty = drink + empty;
            drink = empty/numExchange;
            empty = empty % numExchange;
        }
        sum += drink;
        return sum;
    }
};