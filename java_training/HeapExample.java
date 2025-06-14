import java.util.PriorityQueue;

public class HeapExample {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) {
            pq.offer(s);
        }

        int mixes = 0;
        // 가장 맵지 않은 음식이 K 이상이면 종료
        while (!pq.isEmpty() && pq.peek() < K) {
            if (pq.size() < 2) {
                // 더 이상 섞을 수 있는 음식이 부족하면 -1 반환
                return -1;
            }
            int first = pq.poll();
            int second = pq.poll();
            int mixed = first + second * 2;
            pq.offer(mixed);
            mixes++;
        }

        return mixes;
    }
}
