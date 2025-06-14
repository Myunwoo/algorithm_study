import java.util.Arrays;
import java.util.Collections;

public class Sort {
    public long solution(long n) {
        String answerStr = "";
    
        String[] str = Long.toString(n).split("");
        Arrays.sort(str, Collections.reverseOrder());
        
        for (String s: str) {
            answerStr += s;
        }
        
        return Long.parseLong(answerStr);
    }
}
