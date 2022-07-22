n,m = map(int,input().split())
#nxm의 직사각형
x,y,direction=map(int,input().split())

d = [[0]*m for _ in range(n) ]

d[x][y] = 1 #현재 좌표 처리

#전체 맵 정보를 입력받기

array =[]
for i in range(n):
    array.append(list(map(int,input().split())))
    
#북,동,남,서 좌표 지정하기
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
#시뮬시작
count=1
turn_time=0

while True:
    turn_left()
    nx =x+dx[direction]
    ny =y+dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재
    if d[]
    
    #아무리 해도 이해가 안감 나중에 다시 오기

