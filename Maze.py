def find_paths(maze):
    n = len(maze)
    paths = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    find_path_helper(maze, 0, 0, "", visited, paths, n)
    return paths

def find_path_helper(maze, x, y, path, visited, paths, n):
    # Base case: if (x, y) is outside maze or blocked or already visited
    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == 0 or visited[x][y]:
        return

    # If destination is reached
    if x == n - 1 and y == n - 1:
        paths.append(path)
        return

    # Mark current cell as visited
    visited[x][y] = True

    # Move Down
    find_path_helper(maze, x + 1, y, path + "D", visited, paths, n)

    # Move Left
    find_path_helper(maze, x, y - 1, path + "L", visited, paths, n)

    # Move Right
    find_path_helper(maze, x, y + 1, path + "R", visited, paths, n)

    # Move Up
    find_path_helper(maze, x - 1, y, path + "U", visited, paths, n)

    # Unmark current cell as visited (backtrack)
    visited[x][y] = False

# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0], 
        [1, 1, 0, 1], 
        [1, 1, 0, 0], 
        [0, 1, 1, 1]
        ]

    paths = find_paths(maze)
    if not paths:
        print("No path found")
    else:
        for path in paths:
            print(path)