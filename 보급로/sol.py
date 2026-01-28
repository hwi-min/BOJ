T = int(input())
for t in range(1, T+1):
    N, D = map(int, input().split())
    pos_dict = {}
    for _ in range(N):
        pos, time = map(int, input().split())
        pos_dict[pos] = time

    front_pos, rear_pos = 0, D

    while True:
        if front_pos == rear_pos:
            break

        front_next, rear_next = front_pos + 1, rear_pos - 1

        if front_next in pos_dict.keys() and pos_dict[front_next] != 0:
            pos_dict[front_next] -= 1
        else:
            front_pos = front_next 
        
        if rear_next in pos_dict.keys() and pos_dict[rear_next] != 0:
            pos_dict[rear_next] -= 1
        else:
            rear_pos = rear_next

    print(f"#{t} {front_pos}")
