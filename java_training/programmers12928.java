class Solution {
  public int solution(int n) {
    int answer = 0;
    int idx = 1;

    while (idx <= n) {
      if (n % idx == 0) {
        answer += idx;
      }
      idx++;
    }

    return answer;
  }
}