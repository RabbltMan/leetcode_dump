public class Solution {
    public int[][] RestoreMatrix(int[] rowSum, int[] colSum) {
        int[][] result = new int[rowSum.Length][];
        for (int i = 0; i < rowSum.Length; i++) {
            result[i] = new int[colSum.Length];
        }
        for (int row = 0; row < rowSum.Length; row++) {
            for (int column = 0; column < colSum.Length; column++) {
                result[row][column] = Math.Min(rowSum[row], colSum[column]);
                rowSum[row] -= result[row][column];
                colSum[column] -= result[row][column];
            }
        }
        return result;
    }
}