class Solution {
    public double separateSquares(int[][] squares) {
        double totalArea = 0;
        double low = Double.MAX_VALUE, high = Double.MIN_VALUE;

        for (int[] s : squares) {
            double y = s[1], l = s[2];
            totalArea += l * l;
            low = Math.min(low, y);
            high = Math.max(high, y + l);
        }

        double target = totalArea / 2.0;

        for (int i = 0; i < 100; i++) { // enough for 1e-5 precision
            double mid = (low + high) / 2.0;
            if (areaBelow(squares, mid) < target) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return low;
    }

    private double areaBelow(int[][] squares, double h) {
        double area = 0;
        for (int[] s : squares) {
            double y = s[1], l = s[2];
            if (h <= y) continue;
            else if (h >= y + l) area += l * l;
            else area += l * (h - y);
        }
        return area;
    }
}
