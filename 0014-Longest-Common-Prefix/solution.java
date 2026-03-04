import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length - 1];
        int len = 0;
        for(int i = 0; i < strs[0].length(); i++){
            
            if(first.charAt(i) == last.charAt(i)){
                len++;
            } else{
                break;
            }
        }
        return first.substring(0, len);
    }
}