class Solution {
    public void islandsAndTreasure(int[][] grid) {
        
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 0) {
                    q.add(new int[]{i, j});
                }
            }
        }

        int[] dirR = {-1, 0, 1, 0};
        int[] dirC = {0, 1, 0, -1};
        while (!q.isEmpty()) {
            int[] gate = q.poll();
            int r = gate[0];
            int c = gate[1];
            for (int i = 0; i < 4; i++) {
                int newR = r + dirR[i];
                int newC = c + dirC[i];
                if (newR >= 0 && newR < grid.length && newC >= 0 && newC < grid[0].length && grid[newR][newC] == Integer.MAX_VALUE) {
                    grid[newR][newC] = grid[r][c] + 1;
                    q.add(new int[]{newR, newC});
                }
            }
        }
    }
}
