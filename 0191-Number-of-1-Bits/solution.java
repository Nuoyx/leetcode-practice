//  Optimal solution using bit manipulation
//  public class Solution {
//     public int hammingWeight(int n) {
//         int res = 0;
//         for (int i = 0; i < 32; i++) {
//             if (((n >> i) & 1) == 1) {
//                 res += 1;
//             }
//         }
//         return res;        
//     }
// }



class Solution {
    public int hammingWeight(int n) {
        String binaryString = Integer.toBinaryString(n);
        int exp = binaryString.length() - 1;
        int count = 0;
        double temp = Math.pow(2, exp);
        while(true){
            if(n == 0){
                break;
            }
            System.out.print(temp);
            if(n >= temp){
                n -= temp;
                count++;
            }
            exp--;
            temp = Math.pow(2, exp);
        }
        return count;
    }
}