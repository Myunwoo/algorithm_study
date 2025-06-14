import java.util.HashMap;

public class HashMap {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hashMap = new HashMap<>();
        
        for (String[] clothe: clothes) {
            String val = clothe[0];
            String typ = clothe[1];
            
            hashMap.put(typ, hashMap.getOrDefault(typ, 1) + 1);
        }
        
        for (String key: hashMap.keySet()) {
            answer *= hashMap.get(key);
        }
        
        return answer - 1;
    }
}
