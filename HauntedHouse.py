import random

NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"
UP = "UP"
DOWN = "DOWN"
NORTHWEST = "NORTH WEST"

FIRE = 0
DEATH = False

# name, description, isLit

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
         10: ["MASTER BEDROOM", "sleep", True],
         11: ["DRESSING ROOM", "dress", True],
         12: ["BATHROOM", "wash", False],
         13: ["STUDY", "work", True],
         14: ["STAIR 2F", "climb", True],
         15: ["LANDING 2F", "you stand", True],
         16: ["CHILD BEDROOM", "sleep", True],
         17: ["PLAYROOM", "play", True],
         18: ["CHILD BATHROOM", "wash", True],
         19: ["STAIR 3F", "climb", True],
         20: ["ATTIC", "dust", False],
         21: ["TRAPDOOR", "trapped", True],
         22: ["STAIR BF", "climb", False],
         23: ["LANDING BF", "you stand", False],
         24: ["DUNGEON", "scary", False],
         25: ["WINE CELLAR", "drink", False],
         26: ["CELL", "lock", False],

         101: ["Maze", "lost in a maze", True],
         102: ["Maze", "lost in a maze", True],
         103: ["Maze", "lost in a maze", True],
         104: ["Maze", "lost in a maze", True],
         105: ["Maze", "lost in a maze", True],
         106: ["Maze", "lost in a maze", True],
         107: ["Maze", "lost in a maze", True],
         108: ["Maze", "you found the end", True],

         999: ["you win", "you win", True]}
# direction, newLocation, isLocked?
CONNECTIONS = {0: {NORTH: [1, False], DOWN: [101, False]},
               1: {NORTH: [6, False], EAST: [2, False], SOUTH: [0, False], WEST: [4, False]},
               2: {NORTH: [3, False], WEST: [1, False]},
               3: {SOUTH: [2, False], WEST: [5, True]},
               4: {EAST: [1, False]},
               5: {EAST: [3, False]},
               6: {SOUTH: [1, False], UP: [8, False], DOWN: [22, False]},
               8: {SOUTH: [9, False], UP: [14, False], DOWN: [6, False]},
               9: {NORTH: [8, False], EAST: [10, False], WEST: [13, True]},
               10: {NORTH: [11, False], WEST: [9, False]},
               11: {SOUTH: [10, False], WEST: [12, True]},
               12: {EAST: [11, True]},
               13: {EAST: [9, True]},
               14: {SOUTH: [15, False], UP: [19, False], DOWN: [8, False]},
               15: {NORTH: [14, False], EAST: [16, True], WEST: [17, False]},
               16: {NORTHWEST: [18, False], WEST: [15, True]},
               17: {EAST: [15, False]},
               18: {EAST: [16, False]},
               19: {SOUTH: [20, False], DOWN: [14, False]},
               20: {NORTH: [19, False], WEST: [21, True]},
               21: {DOWN: [26, False]},
               22: {SOUTH: [23, False], UP: [6, False]},
               23: {NORTH: [22, False], EAST: [25, False], WEST: [24, True]},
               24: {NORTH: [26, True], EAST: [23, True]},
               25: {EAST: [23, False]},
               26: {SOUTH: [24, True]},
               101: {NORTH: [105, False], EAST: [102, False], SOUTH: [104, False]},
               102: {NORTH: [105, False], SOUTH: [104, False], WEST: [103, False]},
               103: {EAST: [101, False], NORTH: [104, False]},
               104: {SOUTH: [101, False], WEST: [102, False]},
               105: {NORTH: [101, False], WEST: [106, False]},
               106: {NORTH: [107, False], SOUTH: [102, False]},
               107: {EAST: [108, False], SOUTH: [101, False]}
               }

# name, size, weight, value
OBJECTS = {0: ["Lit Torch", 10, 2, 1],
           1: ["Key", 3, 1, 5],
           2: ["Unlit Torch", 10, 2, 1],
           3: ["Matches", 1, 1, 1],
           4: ["Bronze Coin", 1, 1, 5],
           5: ["Silver Coin", 1, 1, 10],
           6: ["Gold Coin", 1, 1, 25],
           7: ["Chalice", 5, 3, 50],
           8: ["Matches", 1, 1, 1],
           9: ["Matches", 1, 1, 1],
           10: ["Matches", 1, 1, 1],
           11: ["random", 1, 1, 999],
           12: ["old chair", 100, 100, 0],

           }

INVENTORY_LOCATION = 1103
VOID_LOCATION = 2006

OBJECT_LOCATIONS = {0: VOID_LOCATION,

                    1: 11,
                    2: 17,
                    3: 4,
                    4: 2,
                    5: 8,
                    6: 18,
                    7: INVENTORY_LOCATION,
                    8: 14,
                    9: 20,
                    10: 3,
                    11: random.choice([0, 1, 2]),
                    12: 0,
                    }


# OBJECT_LOCATIONS[2] = 0
# OBJECT_LOCATIONS[3] = 0


def objectsAtLocation(roomID):
    found = []
    for k, v in OBJECT_LOCATIONS.items():
        if v == roomID:
            found.append(k)
    return found


def prtRoom(roomID):
    name, description, isLit = ROOMS[roomID]
    directions = CONNECTIONS.get(roomID)
    print(f"{name}\n{description}")


def bag():
    totalSize = 0
    totalWeight = 0
    totalValue = 0
    inventory = objectsAtLocation(INVENTORY_LOCATION)
    for objectID in inventory:
        name, size, weight, value = OBJECTS[objectID]
        totalSize += size
        totalWeight += weight
        totalValue += value

    return totalSize, totalWeight, totalValue


totalSize, totalWeight, totalValue = bag()
SIZECAPACITY = 100
WEIGHTCAPACITY = 100
SPACE = SIZECAPACITY - totalSize
WEIGHT = WEIGHTCAPACITY - totalWeight


def use(objectID, currentRoomID):
    global FIRE
    inventory = objectsAtLocation(INVENTORY_LOCATION)
    success = False
    name, size, weight, value = OBJECTS[objectID]
    print(f"you try to use {name}")

    if name == "UnLit Torch":
        print("you wave an un lit torch")
        x = input()
        print("it does nothing")
        success = True
    elif name == "Matches":
        print("you light a match")
        OBJECT_LOCATIONS[objectID] = VOID_LOCATION
        if OBJECT_LOCATIONS[2] == INVENTORY_LOCATION:
            OBJECT_LOCATIONS[2] = VOID_LOCATION
            OBJECT_LOCATIONS[0] = INVENTORY_LOCATION
            print("the match lit your torch!")
            FIRE = 5
            success = True

    if success is False:
        x = input()
        print("nothing happend")


def fire(currentRoomID):
    global FIRE, DEATH
    hasTorch = OBJECT_LOCATIONS[0] == INVENTORY_LOCATION
    FIRE -= 1
    if FIRE < -1:
        FIRE = -1

    if FIRE < 0:
        if hasTorch is True:
            OBJECT_LOCATIONS[0] = VOID_LOCATION
            OBJECT_LOCATIONS[2] = INVENTORY_LOCATION
    else:
        OBJECT_LOCATIONS[0] = INVENTORY_LOCATION
        OBJECT_LOCATIONS[2] = VOID_LOCATION
    name, description, isLit = ROOMS[currentRoomID]
    if FIRE <= 0 and isLit is False:
        print("your torch extingushed and the ghosts of the dark killed you")
        x = input()
        print("YOU DIED")
        DEATH = True


def inventory(currentRoomID):
    global FIRE

    valid = False
    while valid is False:
        objects = objectsAtLocation(INVENTORY_LOCATION)
        print("What would you like to do with your items?\n1) USE\n2) DROP\n3) VIEW\n4) EXIT")
        ans = input("")
        try:
            ans = int(ans)
        except:
            print(f"{ans} is not a number please type the numbers not their answers")
        if ans == 1:
            if len(objects) >= 1:
                valid = False
                while valid is False:
                    print("What would you like to use?")
                    for i, k in enumerate(objects):
                        name, size, weight, value = OBJECTS[k]
                        print(f"{i + 1}) {name}: {size} unit(s) big, {weight} unit(s) heavy, worth £{value}")
                    ans = input("")
                    try:
                        ans = int(ans)

                        if ans > 0 and ans <= len(objects):
                            selectedObject = objects[ans - 1]
                            use(selectedObject, currentRoomID)

                            x = input()
                            valid = True
                    except:
                        print(f"{ans} is not a number plaese type the numbers not their answers")
            else:
                print("you have no stuff!")
        elif ans == 2:
            if len(objects) >= 1:
                valid = False
                while valid is False:
                    print("What would you like to drop?")
                    for i, k in enumerate(objects):
                        name, size, weight, value = OBJECTS[k]
                        print(f"{i + 1}) {name}: {size} unit(s) big, {weight} unit(s) heavy, worth £{value}")
                    ans = input("")
                    try:
                        ans = int(ans)

                        if ans > 0 and ans <= len(objects):
                            selectedObject = objects[ans - 1]
                            name, size, weight, value = OBJECTS[selectedObject]
                            OBJECT_LOCATIONS[selectedObject] = currentRoomID
                            print(f"you dropped {name}")
                            x = input()
                            valid = True
                        else:
                            print("that is not the answer you are looking for")
                            x = input()
                    except:
                        print(f"{ans} is not a number please type the numbers not their answers")
                        x = input()


            else:
                print("you have no stuff!")
        elif ans == 3:
            if len(objects) >= 1:
                print("This is your stuff")
                for i, k in enumerate(objects):
                    name, size, weight, value = OBJECTS[k]
                    print(f"{i + 1}) {name}: {size} unit(s) big, {weight} unit(s) heavy, worth £{value}")

                totalSize, totalWeight, totalValue = bag()
                print(
                    f"Space Left: {SIZECAPACITY - totalSize}\nWeight Spare: {WEIGHTCAPACITY - totalWeight}\nTotal Value: £{totalValue}")
                x = input()

            else:
                print("you have no stuff!")
                x = input()
        elif ans == 4:
            valid = True


def objects(roomID):
    objects = objectsAtLocation(roomID)
    if len(objects) >= 1:
        valid = False
        while valid is False:
            print("what object would you like to pick up?")
            for i, k in enumerate(objects):
                name, size, weight, value = OBJECTS[k]
                print(f"{i + 1}) {name}")
            print(f"{len(objects) + 1}) Cancel")
            ans = input("")
            try:
                ans = int(ans)
                if ans == len(objects) + 1:
                    valid = True

                else:
                    valid = True
                    selectedObject = objects[ans - 1]
                    name, size, weight, value = OBJECTS[selectedObject]
                    totalSize, totalWeight, totalValue = bag()

                    if totalSize + size > SIZECAPACITY:
                        print("you don't have enough space to carry this")
                        valid = False
                    elif totalWeight + weight > WEIGHTCAPACITY:
                        print("you aren't strong enough to carry this")
                        valid = False
                    else:
                        print(f"you pick up {name}")
                        OBJECT_LOCATIONS[selectedObject] = INVENTORY_LOCATION
                    x = input()
            except:
                print(f"{ans} is not a number please type the numbers not their answers")

    else:
        print("there are no object you can see at the moment")
        x = input()


def move(roomID):
    name, description, isLit = ROOMS[roomID]
    hasKey = OBJECT_LOCATIONS[1] == INVENTORY_LOCATION
    hasTorch = OBJECT_LOCATIONS[0] == INVENTORY_LOCATION
    directions = CONNECTIONS.get(roomID)
    if directions is not None and isLit is True or hasTorch is True:
        choices = list(directions.keys())

        valid = False
        while valid is False:
            print("Where would you like to go?")
            for i, k in enumerate(choices):
                destinationID, isLocked = directions[k]
                name, description, isLit = ROOMS[destinationID]
                if isLocked is False or hasKey is True:
                    print(f"{i + 1}) {k}: {name}")
                elif isLocked is True:
                    print(f"{i + 1}) {k}: LOCKED")
            print(f"{len(directions) + 1}) Cancel")
            ans = input("")

            try:
                ans = int(ans)
                if ans == len(directions) + 1:
                    valid = True

                else:
                    if ans <= len(choices) and ans >= 1:
                        valid = True
                    elif hasTorch is False and isLit is False:
                        print("that room is dark and scary")
                    else:
                        print("that is not the answer you are looking for")
            except:
                print(f"{ans} is not a number please type the numbers not their answers")
        if ans == len(directions) + 1:
            return roomID
        chosenDirection = choices[ans - 1]
        destination, isLocked = directions[chosenDirection]
        if isLocked is False or hasKey is True:
            return destination
        else:
            print("the door is locked")
            x = input()
            return roomID

    else:
        x = input()
        return roomID


def end():
    totalSize, totalWeight, totalValue = bag()
    print(f'you sold the items you found in the house for {totalValue}skulls')


def main():
    currentRoomID = 0
    turns = 0
    moves = 0
    while DEATH is False:
        prtRoom(currentRoomID)
        valid = False
        while valid is False:
            fire(currentRoomID)
            bag()
            if DEATH is True:
                break
            print(moves)
            ans = input("What would you like to do?\n1) Move\n2) Objects\n3) Bag\n")
            try:
                ans = int(ans)
            except:
                print(f"{ans} is not a number please type the numbers not their answers")
            if ans == 1:
                valid = True

                nextRoomID = move(currentRoomID)
                name, description, isLit = ROOMS[nextRoomID]
                hasTorch = OBJECT_LOCATIONS[0] == INVENTORY_LOCATION
                if isLit is True or hasTorch is True:
                    currentRoomID = nextRoomID
                    moves += 1
                else:
                    print("this room is dark and scary")
                    x = input()

            elif ans == 2:
                valid = True
                objects(currentRoomID)
            elif ans == 3:
                valid = True
                inventory(currentRoomID)
        if currentRoomID == 0 and moves > 0:
            ans = int(input("do you want to leave the house?"))
            if ans == 1:
                print(f'you left the house after {turns + 1} turns')
                x = input()
                break
        turns += 1
    end()


main()
