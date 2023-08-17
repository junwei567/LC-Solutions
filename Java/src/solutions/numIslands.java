package solutions;

public class numIslands {
    public static int getNumIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j, grid);
                    count++;
                }
            }
        }
        return count;
    }

    // dfs is a recursive function
    public static void dfs(int row,int col,char[][]grid){
        if (row >= 0 && row < grid.length && col >= 0 && col < grid[0].length && grid[row][col] == '1'){
            grid[row][col] = '0'; // change value to '0' so that it will not be traversed again
            dfs(row, col+1, grid);
            dfs(row, col-1, grid);
            dfs(row+1, col, grid);
            dfs(row-1, col, grid);
        }
    }

    public static void main(String[] args) {
        char[][] array = {{'1','1','0'}, {'1','1','0'}, {'0','0','1'}};
        System.out.println(numIslands.getNumIslands(array));
    }

}
