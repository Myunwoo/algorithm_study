import java.util.Arrays;
import java.util.Comparator;

public class SortExample {
    public String solution(int[] numbers) {
        // 숫자를 문자열로 변환
        String[] strNums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strNums[i] = String.valueOf(numbers[i]);
        }

        // 커스텀 비교: 두 수를 붙였을 때 어떤 순서가 더 큰지 비교
        Arrays.sort(strNums, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                String ab = a + b;
                String ba = b + a;
                // 내림차순 정렬: 큰 문자열이 앞에 오도록
                return ba.compareTo(ab);
            }
        });

        // 정렬 후 가장 큰 수가 "0"이면 (모두 0으로만 이루어짐) "0"만 리턴
        if (strNums[0].equals("0")) {
            return "0";
        }

        // 결과 문자열 합치기
        StringBuilder sb = new StringBuilder();
        for (String num : strNums) {
            sb.append(num);
        }
        return sb.toString();
    }
}
