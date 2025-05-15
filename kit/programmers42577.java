import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String, Boolean> hashMap = new HashMap<>();
        
        for (String p: phone_book) {
            hashMap.put(p, true);
        }
        
        for (String key: hashMap.keySet()) {
            String word = "";
            
            for (int i=0; i<key.length(); i++) {
                word += key.charAt(i);
                
                if (hashMap.containsKey(word) && !word.equals(key)) {
                    return false;
                }
            }
        }
        
        return answer;
    }
}