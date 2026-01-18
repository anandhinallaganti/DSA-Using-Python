class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        int[][] row = new int[m + 1][n + 1];
        int[][] col = new int[m + 1][n + 1];
        int[][] diag1 = new int[m + 1][n + 1];
        int[][] diag2 = new int[m + 1][n + 2];

        // Prefix sums
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row[i + 1][j + 1] = row[i + 1][j] + grid[i][j];
                col[i + 1][j + 1] = col[i][j + 1] + grid[i][j];
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j];
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j];
            }
        }

        for (int size = Math.min(m, n); size >= 2; size--) {
            for (int i = 0; i + size <= m; i++) {
                for (int j = 0; j + size <= n; j++) {
                    int target = row[i + 1][j + size] - row[i + 1][j];

                    boolean ok = true;

                    // Check rows
                    for (int r = i; r < i + size && ok; r++) {
                        int sum = row[r + 1][j + size] - row[r + 1][j];
                        if (sum != target) ok = false;
                    }

                    // Check columns
                    for (int c = j; c < j + size && ok; c++) {
                        int sum = col[i + size][c + 1] - col[i][c + 1];
                        if (sum != target) ok = false;
                    }

                    // Check diagonals
                    int d1 = diag1[i + size][j + size] - diag1[i][j];
                    int d2 = diag2[i + size][j] - diag2[i][j + size];
                    if (d1 != target || d2 != target) ok = false;

                    if (ok) return size;
                }
            }
        }
        return 1;
    }
}
