import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int l = nums.length / 2;
        
        HashMap<Integer, Boolean> hashMap = new HashMap<>();
        
        for (int n: nums) {
            if (hashMap.size() >= l) {
                return l;
            }
            
            hashMap.put(n, true);
        }
        
        return hashMap.size();
    }
}