import sys
import json

class Room:
    def __init__(self, name, desc, exits):
        self.name = name
        self.desc = desc
        self.exits = exits
    
    def __str__(self) -> str:
        return f"{self.name}\n{self.desc}\n{self.exits}\n"
    
    def __repr__(self) -> str:
        return f"{self.name}\n{self.desc}\n{self.exits}\n"

class Map:
    def __init__(self, mapfile):
        self.rooms = {}
        self.count = 0
        self.parse_map(mapfile)
        

    def parse_map(self, mapfile):
        with open(mapfile) as f:
            try:
                data = json.load(f)
                for room_data in data:
                    name = room_data.get("name")
                    desc = room_data.get("desc")
                    exits = room_data.get("exits")
                    if name is None or desc is None or exits is None:
                        raise ValueError("Invalid room data")
                    for direction, room_id in exits.items():
                        if not isinstance(room_id, int):
                            raise ValueError("Invalid exit data")
                    self.rooms[self.count] = Room(name, desc, exits)
                    self.count += 1
                Game(self.rooms)
                return self.rooms
            except:
                raise ValueError("Invalid map file")
    
    def __str__(self):
        return f"Map: {self.rooms}"
    
    def __repr__(self):
        return f"Map: {self.rooms}"
    
class Game:
    def __init__(self, rooms):
        self.rooms = rooms
        self.player_location = 0
        self.inventory = []
        self.start()

    def start(self):
        room = self.rooms[self.player_location]
        print(f"> {room.name}\n\n{room.desc}\n")
        print(f"Exits: {' '.join(room.exits.keys())}")
        print()
        self.prompt()
    
    def prompt(self):
        while True:
            action = input("What would you like to do? ")
            verb = action.lower().split(" ")
            
            if verb[0] == "go":
                if len(verb) == 2 :
                    self.go(verb[1])
                else:
                    print("Sorry, you need to 'go' somewhere.")
    

    def go(self, direction):
        room = self.rooms[self.player_location]
        
        if direction not in room.exits:
            print(f"There's no way to go {direction}.")
        else:
            print(f"You go {direction}.\n")
            self.player_location = room.exits[direction]
            self.start()


    

    


if __name__ == "__main__":
    if len(sys.argv) == 2:
          map_file = sys.argv[1]
          game = Map(map_file)
          print(game)
    else:
        map_file = "loop.map"
        game = Map(map_file)
        print(game)
       
