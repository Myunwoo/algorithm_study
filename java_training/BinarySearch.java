import java.util.Arrays;

public class BinarySearch {
    public long solution(int n, int[] times) {
        Arrays.sort(times);

        long left = 1;
        long right = (long) times[times.length - 1] * n;
        long answer = right;

        while (left <= right) {
            long mid = (left + right) / 2;
            long count = 0;

            for (int time : times) {
                count += mid / time;
            }

            if (count >= n) {
                // 처리 가능하므로 시간 줄여보기
                answer = mid;
                right = mid - 1;
            } else {
                // 처리 불가능, 시간 늘려야 함
                left = mid + 1;
            }
        }

        return answer;
    }
}
