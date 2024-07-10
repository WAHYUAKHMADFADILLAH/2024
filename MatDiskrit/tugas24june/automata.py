from collections import deque
def is_reachable(grid):
    N = len(grid)
    if grid[0][0] == 1 or grid[N-1][N-1] == 1:
        return False
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0)])
    visited = set((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (N-1, N-1):
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

# Contoh grid 3x3
grid = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

if is_reachable(grid):
    print("Robot dapat mencapai koordinat (N-1, N-1)")
else:
    print("Robot tidak dapat mencapai koordinat (N-1, N-1)")
