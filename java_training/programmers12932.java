public class programmers12932 {
  public int[] solution(long n) {
    int count = 0;
    long nCopy = n;
    while (nCopy > 0) {
      nCopy /= 10;
      count++;
    }

    int[] answer = new int[count];

    for (int i = 0; i < count; i++) {
      long d = n % 10;
      answer[i] = (int) d;
      n /= 10;
    }

    return answer;
  }
}
