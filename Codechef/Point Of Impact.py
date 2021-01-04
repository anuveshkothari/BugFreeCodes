
test_cases = int(input())
for test in range(test_cases):
    n,k,x,y = map(int, list(input().split()))
    corner_points =[(0,0), (0,n), (n,0), (n,n)]
    previous_point = [x,y]
    list_of_collision_points =[]
    number_of_collision = 0

    if x == y:
        print(n,n)
    else:
        if x > y:
            list_of_collision_points = [[n, y+(n-x)], [y+(n-x), n], [0, x-y], [x-y, 0]]
        else:
            list_of_collision_points = [[x + (n-y), n], [n, x+(n-y)], [y-x, 0], [0, y-x]]

        # print(list_of_collision_points)
        if k%4  == 0:
            print(list_of_collision_points[3][0],list_of_collision_points[3][1])
        elif k%4  == 1:
            print(list_of_collision_points[0][0], list_of_collision_points[0][1])
        elif k%4  == 2:
            print(list_of_collision_points[1][0], list_of_collision_points[1][1])
        elif k%4  == 3:
            print(list_of_collision_points[2][0], list_of_collision_points[2][1])