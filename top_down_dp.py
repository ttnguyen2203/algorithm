
"""
    The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
    The dungeon consists of M x N rooms laid out in a 2D grid.
    Our valiant knight (K) was initially positioned in the top-left room and must fight his way through 
        the dungeon to rescue the princess.

    The knight has an initial health point represented by a positive integer. If at any point his health 
        point drops to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering 
        these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health 
        (positive integers).

    In order to reach the princess as quickly as possible, the knight decides to move only rightward or 
        downward in each step.

"""

 def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        
        ##https://leetcode.com/problems/dungeon-game/ 
        def inbound(tup):
            if tup[0] >= 0 and tup[0] < len(dungeon) and tup[1] >= 0 and tup[1] < len(dungeon[0]):
                return True
            else:
                return False
        
        last_room = (len(dungeon)-1, len(dungeon[0])-1)
                
        cache = {}
        
        cache[last_room] = max(dungeon[last_room[0]][last_room[1]] * -1 + 1, 1)

        
        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                room = (i, j)

                top, left = (i - 1, j), (i, j - 1)
                bottom, right = (i + 1, j), (i, j + 1)

                if room in cache.keys():
                    continue

                valid = []
                for r in [bottom, right]:
                    if inbound(r):
                        new_val = cache[r] - dungeon[i][j]
                        if new_val > 0:
                            valid.append(new_val)
                        else:
                            valid.append(1)
                cache[room] = min(valid)

            
        return cache[(0,0)]