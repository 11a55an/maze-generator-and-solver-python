from pyamaze import maze,agent,COLOR, textLabel
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath

def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath


m=maze(5,5)
m.CreateMaze(loopPercent=30, loadMaze="Python/AI Assignment/maze--2022-12-26--00-28-57.csv")
pathA=DFS(m)
pathB=BFS(m)
a=agent(m,footprints=True,filled=True)
b=agent(m,footprints=True,filled=True, color=COLOR.red)
m.tracePath({a:pathA})
m.tracePath({b:pathB})
l3=textLabel(m, 'Total Cells:', m.rows*m.cols)
l4=textLabel(m,'DFS Path = Blue',COLOR.blue)
l4=textLabel(m,'BFS Path = Red',COLOR.red)
l1=textLabel(m,'Length of DFS Path',len(pathA)+1)
l2=textLabel(m,'Length of BFS Path',len(pathB)+1)

m.run()