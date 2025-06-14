import java.util.Stack;

public class StackExample {
    public boolean solution(String s) {
        // 문자열 길이가 홀수면 바로 false
        if (s.length() % 2 == 1) return false;

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else { // c == ')'
                // 닫는 괄호인데 비어있거나, 짝이 안 맞으면 false
                if (stack.isEmpty() || stack.peek() != '(') {
                    return false;
                }
                // 올바른 짝이면 pop
                stack.pop();
            }
        }

        // 최종적으로 스택이 비어 있으면 true, 아니면 false
        return stack.isEmpty();
    }
}
