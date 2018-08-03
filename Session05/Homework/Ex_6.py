map_size = {
    "size_x" : 6,
    "size_y" : 6
}

boxes = [
    {"x" : 0, "y" : 2},
    {"x" : 1, "y" : 2},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 2}
]

destinations = [
    {"x" : 0, "y" : 3},
    {"x" : 1, "y" : 4},
    {"x" : 0, "y" : 5},
    {"x" : 3, "y" : 5}
]

obstacles = [
    {"x" : 1, "y" : 3},
    {"x" : 4, "y" : 5}
]

player = {"x" : 1, "y" : 1}

loop = True

while loop:

#Ve hinh
    for y in range (map_size["size_y"]):
        for x in range (map_size["size_x"]):

            player_is_here = False
            if y == player["y"] and x == player["x"]:
                player_is_here = True
            
            box_is_here = False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True

            obstacle_is_here = False
            for obstacle in obstacles:
                if y == obstacle["y"] and x == obstacle["x"]:
                    obstacle_is_here = True

            destination_is_here = False
            for destination in destinations:
                if y == destination["y"] and x == destination["x"]:
                    destination_is_here = True
            
            if player_is_here:
                print ("P ", end=" ")
            elif box_is_here:
                print ("B ", end=" ")
            elif obstacle_is_here:
                print ("O ", end=" ")
            elif destination_is_here:
                print ("D ", end=" ")
            else:
                print ("- ", end=" ")
        print ("")
#Het ve hinh
#win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win:
        print ("You win!!!")
        break
#Het win
#move
    move = input ("Your move? ")
    dx = 0
    dy = 0

    if move.lower() == "w":
        dy = -1
    elif move.lower() == "d":
        dx = 1
    elif move.lower() == "a":
        dx = -1
    elif move.lower() == "s":
        dy = 1
    else:
        print ("Shit!!!")
#het move
#lap
    if 0 <= player["x"] + dx < map_size["size_x"] and 0 <= player["y"] + dy < map_size["size_y"]:
        player["x"] += dx
        player["y"] += dy
        for box in boxes:
            for obs in obstacles:
                if player["x"] == obs["x"] and player["y"] == obs["y"]:
                    print ("Invalid move!!!")
                    player["x"] -= dx
                    player["y"] -= dy
                elif player["x"] == box["x"] and player["y"] == box["y"]:

                    if 0<= box["x"] + dx < map_size["size_x"] and 0 <= box["y"] + dy < map_size["size_y"]:
                        box["x"] += dx
                        box["y"] += dy
                        duplicate = False
                        for i in range (len(boxes)):
                            for j in range (len(boxes)):
                                if boxes[i] == boxes[j] and i != j:
                                    duplicate = True

                        if duplicate:
                            print ("Invalid move!!!")
                            player["x"] -= dx
                            player["y"] -= dy
                            box["x"] -= dx
                            box["y"] -= dy
                            
                        elif box["x"] == obs["x"] and box["y"]== obs["y"]:
                            print ("Invalid move!!!")
                            player["x"] -= dx
                            player["y"] -= dy
                            box["x"] -= dx
                            box["y"] -= dy
                        break