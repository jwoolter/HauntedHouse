NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"
UP = "UP"
DOWN = "DOWN"
NORTHWEST = "NORTH WEST"
key = True
torch = True

ROOMS = {0: ["PORCH", "you stand", True],
         1: ["ENTRANCE HALL", "entrance", True],
         2: ["DINING HALL", "eat", True],
         3: ["KITCHEN", "smell", True],
         4: ["LIVING ROOM", "comfy", True],
         5: ["PANTRY", "food", True],
         6: ["STAIRS GF", "climb", True],
         7: ["CELLAR", "spooky", False],
         8: ["STAIR 1F", "climb", True],
         9: ["LANDING 1F", "you stand", True],
         10:["MASTER BEDROOM", "sleep", True],
         11:["DRESSING ROOM", "dress", True],
         12:["BATHROOM", "wash", False],
         13:["STUDY", "work", True],
         14:["STAIR 2F", "climb", True],
         15:["LANDING 2F", "you stand", True],
         16:["CHILD BEDROOM", "sleep", True],
         17:["PLAYROOM", "play", True],
         18:["CHILD BATHROOM", "wash", True],
         19:["STAIR 3F", "climb", True],
         20:["ATTIC", "dust", False],
         21:["TRAPDOOR", "trapped", True],
         22:["STAIR BF", "climb", True],
         23:["LANDING BF", "you stand", False],
         24:["DUNGEON", "scary", False],
         25:["WINE CELLAR", "drink", True],
         26:["CELL", "lock", True],



         999: ["you win", "you win", True]}

CONNECTIONS = {0: {NORTH: [1, False]},
               1: {NORTH: [6, False], EAST: [2, False], SOUTH: [0, False], WEST: [4, False]},
               2: {NORTH: [3, False], WEST: [1, False]},
               3: {SOUTH: [2, False], WEST: [5, True]},
               4: {EAST: [1, False]},
               5: {EAST: [3, False]},
               6: {SOUTH: [1, False], UP: [8, False], DOWN: [22, False]},
               8: {SOUTH: [9, False], UP: [14, False], DOWN: [6, False]},
               9: {NORTH: [8, False], EAST: [10, False], WEST: [13, True]},
               10:{NORTH: [11, False], WEST: [9, False]},
               11:{SOUTH: [10,False], WEST: [12, True]},
               12:{EAST: [11, True]},
               13:{EAST: [9, True]},
               14:{SOUTH: [15, False], UP: [19, False], DOWN: [8, False]},
               15:{NORTH: [14, False], EAST: [16, True], WEST: [17, False]},
               16:{NORTHWEST: [18, False], WEST: [15, True]},
               17:{EAST: [15, False]},
               18:{EAST: [16, False]},
               19:{SOUTH: [20, False], DOWN: [14, False]},
               20:{NORTH: [19, False], WEST: [21, True]},
               21:{DOWN: [26, False]},
               22:{SOUTH: [23, False], UP: [6, False]},
               23:{NORTH: [22, False], EAST: [25, False], WEST: [24, True]},
               24:{NORTH: [26, True], EAST: [23, True]},
               25:{EAST: [23, False]},
               26:{SOUTH: [24, True]}


               }
OBJECTS = {0:  ["Torch", 10, 2],
           1:  ["Key", 3, 1]}

OBJECT_LOCATIONS = {0: 17,
                    1: 11}

INVENTORY_LOCATION = 7

def objectsAtLocation(roomID):
    found = []
    for k,v in OBJECT_LOCATIONS.items():
        if v == roomID:
            found.append(k)
    return (found)

def prtRoom(roomID):
    name, description, isLit = ROOMS[roomID]
    directions = CONNECTIONS.get(roomID)









def inventory():
    objects = objectsAtLocation(INVENTORY_LOCATION)
    if len(objects) >= 1:
        print("This is your stuff")
        for i, k in enumerate(objects):
            name, size, weight = OBJECTS[k]
            print(f"{i + 1}) {name}: {size} unit(s) big, {weight} unit(s) heavy")
            x=input()
    else:
        print("you have no stuff!")
        x=input()

def objects(roomID):
    objects = objectsAtLocation(roomID)
    if len(objects) >= 1:
        print("what object would you like to pick up?")
        for i, k in enumerate(objects):
            name,size,weight = OBJECTS[k]
            print(f"{i+1}) {name}")
        ans = int(input(""))
        selectedObject = objects[ans-1]
        name,size,weight = OBJECTS[selectedObject]
        print(f"you pick up {name}")
        OBJECT_LOCATIONS[selectedObject] = INVENTORY_LOCATION
        x=input()
    else:
        print("there are no object you can see at the moment")
        x=input()

def move(roomID):
    name, description, isLit = ROOMS[roomID]
    directions = CONNECTIONS.get(roomID)
    if directions is not None and isLit is True or torch is True:
        choices = list(directions.keys())
        print("Where would you like to go?")
        for i, k in enumerate(choices):
            destinationID, isLocked = directions[k]
            name,description, isLit = ROOMS[destinationID]
            if isLocked is False or key is True:
                print(f"{i+1}) {k}: {name}")
            elif isLocked is True:
                print(f"{i+1}) {k}: LOCKED")

        valid = False
        while valid is False:
            ans = int(input(""))
            if ans <=len(choices) and ans >= 1:
                valid = True
            elif torch is False and isLit is True:
                print("that room is dark and scary")
            else:
                print("that is not the answer you are looking for")
        chosenDirection = choices[ans-1]
        destination, isLocked = directions[chosenDirection]
        if isLocked is False or key is True:
            return destination
        else:
            print("the door is locked")
            x=input()
            return(roomID)

    else:
        x = input()
        return (roomID)

def main():
    currentRoomID = 0
    while True:
        prtRoom(currentRoomID)
        valid = False
        while valid is False:
            ans = int(input("What woud you like to do?\n1) Move\n2) Objects\n3) Bag\n"))
            if ans == 1:
                valid = True

                nextRoomID = move(currentRoomID)
                name, description, isLit = ROOMS[nextRoomID]
                if isLit is True or torch is True:
                    currentRoomID = nextRoomID
                else:
                    print("this room is dark and scary")
                    x = input()
            elif ans == 2:
                valid = True
                objects(currentRoomID)
            elif ans == 3:
                valid = True
                inventory()





main()
