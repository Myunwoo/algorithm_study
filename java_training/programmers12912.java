import java.util.stream.LongStream;

class Solution {
    public long solution(int a, int b) {
        if (a == b) return a;
        return LongStream.rangeClosed(Math.min(a, b), Math.max(a, b)).sum();
    }
}