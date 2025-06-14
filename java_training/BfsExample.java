import java.util.LinkedList;
import java.util.Queue;

public class BfsExample {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        int[][] directions = { {0,1}, {1,0}, {0,-1}, {-1,0} };
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[] {0, 0, 1}); // x, y, distance
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0], y = current[1], dist = current[2];

            if (x == n - 1 && y == m - 1) return dist;

            for (int[] dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];

                if (nx >= 0 && ny >= 0 && nx < n && ny < m &&
                    maps[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx, ny, dist + 1});
                }
            }
        }

        return -1; // 목적지 도달 불가능
    }
}
