public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        int[] stats = new int[n];
        bool[][] roadmap = new bool[n][];
        for (int i = 0; i < n; i++) {
            roadmap[i] = new bool[n];
        }

        for (int i = 0; i < roads.Length; i++) {
            stats[roads[i][0]] += 1;
            stats[roads[i][1]] += 1;
            roadmap[roads[i][0]][roads[i][1]] = true;
            roadmap[roads[i][1]][roads[i][0]] = true;
        }

        int result = stats.Max();
        int index1 = Array.IndexOf(stats, result);
        stats[index1] = 0;

        int max = stats.Max();
        int index2 = Array.IndexOf(stats, max);
        result += max - 1;

        if (roadmap[index1][index2]) {
            stats[index2] = 0;
            while (Array.IndexOf(stats, max) != -1) {
                stats[index2] = 0;
                index2 = Array.IndexOf(stats, max);
                stats[index2] = 0;
                if (!roadmap[index1][index2]) {
                    result += 1;
                    break;
                }
            }
        }
        else {
            result += 1;
        }
        return result;
    }
}

class A{
    static void Main(){
        Solution s = new Solution();
        int[][] testcase = new int[4][] {
            new int[] {2,3},
            new int[] {0,3},
            new int[] {0,4},
            new int[] {4,1}
        };
        s.MaximalNetworkRank(5, testcase);
    }
}