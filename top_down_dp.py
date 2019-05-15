# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        
        
        ##Key fix: dp can't solve from bottom up, must go top down
        ##https://leetcode.com/problems/dungeon-game/ 

        cache = {}
        if dungeon[0][0] < 0:
            cache[(0,0)] = (dungeon[0][0] * -1 + 1, 1)
        else:
            cache[(0,0)] = (1, 1 + dungeon[0][0])
            
        #cache stores (minimum starting life, current life)
        for i in range(0,len(dungeon)):
            for j in range(0,len(dungeon[0])):
                if i == j and i == 0:
                    continue
                room = dungeon[i][j]
                previous = []
                for prev in [(i-1, j), (i, j-1)]:
                    if prev in cache.keys():
                        previous.append(cache[prev])

                new_cost= []
                
                for prev in previous:
                    

                if best[1] + room <= 0:
                    buffer = 1 - best[1] - room

                    cache[(i,j)] = (best[0] + buffer, best[1] + buffer + room)
                else:
                    cache[(i,j)] = (best[0], best[1] + room)
        last_room = (len(dungeon)-1, len(dungeon[0])-1)
        print(cache)
        return cache[last_room][0]