class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
        }

        if (totalGas < totalCost) {
            return -1;
        }
        int len = gas.length;
        int result = 0;
        int remainGas = 0;
        for(int i = 0; i < len; i++){
            remainGas += gas[i];
            remainGas -= cost[i];
            if(remainGas < 0){
                remainGas = 0;
                result = i + 1;
            }
        }
        return result;
    }
}