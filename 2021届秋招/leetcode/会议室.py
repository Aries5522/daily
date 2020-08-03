def minMeetingRooms(starts,ends):
    starts.sort()
    ends.sort()
    s, e = 0, 0
    min_rooms, cnt_rooms = 0, 0
    while s < len(starts):
        if starts[s] < ends[e]:
            cnt_rooms += 1  # Acquire a room.
            # Update the min number of rooms.
            min_rooms = max(min_rooms, cnt_rooms)
            s += 1
        else:
            cnt_rooms -= 1  # Release a room.
            e += 1
    return min_rooms


print(minMeetingRooms(starts=[1,1,2,3],ends=[4,2,3,4]))