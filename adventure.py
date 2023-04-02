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
        game_play = True
        while game_play:
            try:
                action = input("What would you like to do? ")
                half_verb = action.lower().split(" ")
                matches = [cmd for cmd in valid_commands if cmd.startswith(half_verb[0])]
                if len(matches) == 1:
                    verb = matches
        
                
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
        
        if direction not in room.exits:
            print(f"There's no way to go {direction}.")
        else:
            print(f"You go {direction}.\n")
            self.player_location = room.exits[direction]
            self.look()

    def look(self):
        room = self.rooms[self.player_location]
        print(f"> {room.name}\n\n{room.desc}\n")
        if(len(room.items) != 0):
            print(f"Items: {', '.join(room.items)}\n")
        print(f"Exits: {' '.join(room.exits.keys())}")
        print()
    
    def get(self, noun):
        room = self.rooms[self.player_location]
        if noun not in room.items:
            print(f"There's no {noun} anywhere.")
        else:
            self.inventory.append(noun)
            print(f"You pick up the {noun}.")
            room.items.remove(noun)
    
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
        
        