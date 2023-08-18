package solutions;

import java.util.HashMap;
import java.util.HashSet;

public class maximalNetworkRank {
    public int getMaximalNetworkRank(int n, int[][] roads) {
        // initialise the hashmap
        HashMap<Integer, HashSet<Integer>> networks = new HashMap<>();
        for (int i = 0; i < n; i ++) {
            networks.put(i, new HashSet<Integer>());

        }
        // populate the hashset in hashmap
        for (int i = 0; i < roads.length; i++) {
            networks.get(roads[i][0]).add(roads[i][1]);
            networks.get(roads[i][1]).add(roads[i][0]);
        }
        // calculate the max network rank
        int max = 0;
        for (int i = 0; i < n-1; i ++) {
            for (int j = i+1; j < n; j ++) {
                int tmp = 0;
                tmp += networks.get(i).size() + networks.get(j).size();
                // if road is connected between cities, avoid double counting
                if (networks.get(i).contains(j)) tmp --;
                max = Math.max(max, tmp);
            }
        }
        return max;
    }
}