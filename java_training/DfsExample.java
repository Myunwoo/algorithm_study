public class DfsExample {
    private int count = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return count;
    }

    private void dfs(int[] numbers, int target, int idx, int sum) {
        if (idx == numbers.length) {
            if (sum == target) count++;
            return;
        }
        // 현재 번호에 + 기호 붙이기
        dfs(numbers, target, idx + 1, sum + numbers[idx]);
        // 현재 번호에 - 기호 붙이기
        dfs(numbers, target, idx + 1, sum - numbers[idx]);
    }
}
