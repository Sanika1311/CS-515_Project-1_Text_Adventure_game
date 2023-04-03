import sys
import json

class Room:
    def __init__(self, name, desc, exits, items):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items
    
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
                    if(room_data.get("items")):
                        items = room_data.get("items")
                    else:
                        items = []
                    if name is None or desc is None or exits is None:
                        raise ValueError("Invalid room data")
                    for direction, room_id in exits.items():
                        if not isinstance(room_id, int):
                            raise ValueError("Invalid exit data")
                    self.rooms[self.count] = Room(name, desc, exits, items)
                    self.count += 1
                
            except:
                raise ValueError("Invalid map file")
            Game(self.rooms)
    
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
        if(len(room.items) != 0):
            print(f"Items: {', '.join(room.items)}\n")
        print(f"Exits: {' '.join(room.exits.keys())}")
        print()
        self.prompt()
    
    def prompt(self):
        valid_commands = ["go", "look", "get", "inventory", "quit", "drop"]
        valid_directions = ["north","northeast","east","southeast","south","southwest","west","northwest"]
        game_play = True
        while game_play:
            try:
                action = input("What would you like to do? ")
                half_verb = action.lower().split(" ")
                matches = [cmd for cmd in valid_commands if cmd.startswith(half_verb[0])]
                if len(matches) == 1:
                    verb = matches
                elif len(matches) == 0:
                    dir_match = [dir for dir in valid_directions if dir.startswith(half_verb[0])]
                    if len(dir_match) >= 1:
                        verb = ["go"]
                        half_verb = ["go", half_verb[0]]
                    else:
                        print("Invalid verb")
                        continue
        
                if verb[0] == "go":
                    if len(half_verb) == 2 :

                        self.go(half_verb[1])
                    else:
                        print("Sorry, you need to 'go' somewhere.")

                elif verb[0] == "look":
                    if len(half_verb) == 1 :
                        self.look()
                    else :
                        print(f"Invalid Verb")

                elif verb[0] == "get":
                        if len(half_verb) == 2 :
                            self.get(half_verb[1])
                        else:
                            print(f"Sorry, you need to 'get' something.")

                elif verb[0] == "drop":
                        if len(half_verb) == 2 :
                            self.drop(half_verb[1])
                        else:
                            print(f"Sorry, you need to drop something.")
                    
                elif verb[0] == "inventory":
                    if len(half_verb) == 1 :
                        if(len(self.inventory) == 0):
                            print(f"You're not carrying anything.")
                        else:
                            print(f"Inventory:\n{', '.join(self.inventory)}")
                    else:
                        print("Invalid Verb")

                elif verb[0] == "quit":
                    game_play = False
                    print(f"Goodbye!")
                    break

                else:
                    print(f"Invalid verb")

            except EOFError:
                print(f"\nUse 'quit' to exit.")

    
    def go(self, direction):
        room = self.rooms[self.player_location]
        direction = [cmd for cmd in room.exits.keys() if cmd.startswith(direction)]

        if len(direction) == 1:
            print(f"You go {direction[0]}.\n")
            self.player_location = room.exits[direction[0]]
            self.look()
        elif len(direction) > 1:
            print(f"Did you want to go {' or '.join(direction)}?")
        else:
            print(f"There's no way to go {direction}.")
       

    def look(self):
        room = self.rooms[self.player_location]
        print(f"> {room.name}\n\n{room.desc}\n")
        if(len(room.items) != 0):
            print(f"Items: {', '.join(room.items)}\n")
        print(f"Exits: {' '.join(room.exits.keys())}")
        print()
    
    def get(self, noun):
        room = self.rooms[self.player_location]
        items = [cmd for cmd in room.items if cmd.startswith(noun)]

        if len(items) == 1:
            self.inventory.append(items[0])
            print(f"You pick up the {items[0]}.")
            room.items.remove(items[0])
        elif len(items) == 2:
            print(f"Did you want to get the {' or '.join(items)}?")
        elif len(items) > 2:
            print(f"Did you want to get the {' , '.join(items[:(len(items)-1)])} or {items[len(items)-1]}?")
        else:
            print(f"There's no {noun} anywhere.")
       
    
    def drop(self, noun):
        room = self.rooms[self.player_location]
        if noun not in self.inventory:
            print(f"There is no {noun} in the inventory.") 
        else:
            self.inventory.remove(noun)
            print(f"You drop the {noun}")
            room.items.append(noun)


if __name__ == "__main__":
    if len(sys.argv) == 2:
          map_file = sys.argv[1]
          Map(map_file)
       
    else:
         map_file = "loop.map"
         Map(map_file)
        
        