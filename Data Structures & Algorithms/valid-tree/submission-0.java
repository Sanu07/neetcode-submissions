class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) {
            return false;
        }

        int[] p = new int[n + 1];
        for (int i = 0; i < n; i++) {
            p[i] = i;
        }

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];

            int pu = find(p, u);
            int pv = find(p, v);

            if (pu == pv) {
                return false;
            }

            p[v] = u;
        }
        return true;
    }

    private int find(int[] p, int x) {
        if (p[x] != x) {
            p[x] = find(p, p[x]);
        }
        return p[x];
    }
}
