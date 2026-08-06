"""The procedural minecart track generator - the project's Maze class, kept
verbatim. The randomizer business logic that turns a solved maze into Moleville
Mountain Mode7 rail tiles lives in randomizer.logic.shufflers.minigames.
"""

import random
from collections import deque as queue


class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.start = (0, 0)
        self.end = (w-1, h-1)

        self.critical_points = []

        for i in range(3):
            for j in range(3):
                self.critical_points.append((random.randrange(int(w*i/3), int(w*(i+1)/3)), random.randrange(int(h*j/3), int(h*(j+1)/3))))

        #self.critical_points = [(random.randrange(w), random.randrange(h)) for i in range(16)]
        #self.critical_points.sort()

        self.cells = [[0 for i in range(h)] for j in range(w)]
        for p in self.critical_points:
            self.cells[p[0]][p[1]] = 1

        self.cells[self.end[0]][self.end[1]] = 1

    def isInBounds(self, x, y):
        return x >= 0 and x < self.w and y >= 0 and y < self.h

    def bfs(self, start, end, vis):
        q = queue()
        vis[start[0]][start[1]] = True
        q.append((start, [start]))

        while (len(q)):
            c = q.popleft()
            if c[0] == end:
                return c

            dirs = [(0, 1, '>'), (1, 0, 'v'), (0, -1, '<'), (-1, 0, '^')]
            random.shuffle(dirs)

            for i in range(len(dirs)):
                x = c[0][0] + dirs[i][0]
                y = c[0][1] + dirs[i][1]

                if self.isInBounds(x, y) and not vis[x][y]:
                    p = c[1] + [(c[0][0], c[0][1], dirs[i][2])]
                    q.append(((x, y), p))
                    vis[x][y] = True

        # unreachable point!
        return None

    def solve(self):
        t_p = []
        curr_node = self.start
        crit_points = self.critical_points[:]
        random.shuffle(crit_points)
        crit_points.append(self.end)
        for n in range(len(crit_points)):
            vis = [[False for i in range(self.h)] for j in range(self.w)]
            for point in t_p:
                vis[point[0]][point[1]] = True

            if curr_node == self.end:
                break

            crit_node = crit_points[n]

            # print(curr_node, crit_node, t_p)
            #self.show( [t for t in t_p if len(t) > 2])

            already_visited = False
            for step in t_p:
                if (step[0], step[1]) == crit_node:
                    already_visited = True

            if already_visited:
                continue

            c_p = self.bfs(curr_node, crit_node, vis)

            # if the path is not reachable, error gracefully
            if c_p is None:
                return None

            t_p = t_p + c_p[1]

            curr_node = crit_node

        return [t for t in t_p if len(t) > 2]

    def show(self, path):
        m_c = self.cells

        for point in path:
            m_c[point[0]][point[1]] = point[2]

        for i in m_c:
            print(*i)
