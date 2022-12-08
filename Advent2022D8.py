from collections import defaultdict, deque

#def directions function

###### def visible
def seeMe(i, j, imax, jmax, grid):
     h = grid[i,j]

     for line in directions(i, j, imax, jmax):
          for tree in line:
               if grid[tree] >= h:
                    break
          else:
               return True
               
     return False

###### directions
def directions(i, j, imax, jmax):
     yield [(r, j) for r in range(i+1, imax+1)]
     yield [(r, j) for r in range(i-1, -1, -1)]
     yield [(i, c) for c in range(j+1, jmax+1)]
     yield [(i, c) for c in range(j-1, -1, -1)]

###### Scenic
def scenic(i, j, imax, jmax, grid):
     h = grid[i,j]
     s = 1
     for line in directions(i, j, imax, jmax):
          d = 0
          for tree in line:
               d += 1
               if grid[tree] >= h:
                    break
          
          s *= d

     return s

# MAIN FILE # PART 1

#2D Array of heights using dictionary
Tgrid = {}
imax = 0
jmax = 0
counter = 0

slist = []

# load the text file
with open("inputday8.txt") as text_file:
     rowlist = text_file.read().split('\n')

     for i, line in enumerate(rowlist):
          for j, val in enumerate(line):
               Tgrid[i,j] = int(val)
               imax = i
               jmax = j

     for i, j in Tgrid:
           boo = seeMe(i,j,imax,jmax,Tgrid)
           slist.append(scenic(i,j,imax,jmax,Tgrid))
           if boo:
               counter += 1

print(counter)
print(max(slist))

