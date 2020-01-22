def foot_traffic(filename):
    with open(filename, 'r') as f_object:
        data = [line.split() for line in f_object]

    #Find how many rooms there are and assume that there exists room 1 to room num_of_rooms
    num_of_rooms = 0
    for line in data:
        if int(line[1]) > num_of_rooms:
            num_of_rooms = int(line[1])

    #Create statistics for each room
    room_stat = dict()
    for i in range(1,num_of_rooms+1):
        room_stat[str(i)] = {"number of visitors" : 0 , "average time spent" : 0, "time spent per visitor" : {}}

    #Find how many people went into each room  
    for line in data:
        if line[2] == "I":
            room_stat[line[1]]["number of visitors"] += 1
    
    #Find time each person staying in a room
    for line in data:
        if line[2] == "I":
            room_stat[line[1]]["time spent per visitor"][line[0]] = -(int(line[3])) #if person if going in add them to the list
        room_stat[line[1]]["time spent per visitor"][line[0]] += int(line[3]) #if the person if going out find the difference between the in time and out time

    #Find average time spent per room
    for value in range(1, num_of_rooms + 1):
        times = room_stat[str(value)]["time spent per visitor"].values()
        if len(list(times)) > 0:
            average_times = sum(list(times))/len(list(times)) 
            room_stat[str(value)]["average time spent"] = average_times
        print(f"Room {value},", room_stat[str(value)]["average time spent"], "minute average visit", room_stat[str(value)]["number of visitors"], "visitor(s) total")

foot_traffic('traffic.txt')