import java.util.*;

public class Solution {
  public int[] solution(int[] arr) {
    int[] answer = null;
    List<Integer> l = new ArrayList<>();
    l.add(arr[0]);

    for (int i = 1; i < arr.length; i++) {
      if (l.get(l.size() - 1) != arr[i]) {
        l.add(arr[i]);
      }
    }

    answer = new int[l.size()];
    for (int i = 0; i < l.size(); i++) {
      answer[i] = l.get(i);
    }

    return answer;
  }
}