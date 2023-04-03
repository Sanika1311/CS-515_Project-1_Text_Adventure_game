# CS-515_Project-1_Text_Adventure_game
NAME : SANIKA RAMCHANDRA CHAVAN
CWID : 20016632
GITHUB REPOSITORY NAME : https://github.com/Sanika1311/CS-515_Project-1_Text_Adventure_game.git

I spent approximately 15 hours on the project. 

Question : A description of how you tested your code.
I wrote doctest for some of the functions to check where is the error. My error inputs consisted of verbs different from the verbs given in the  specs. Also tested the .map file input to check if the map is valid or not.  

Question : Any bugs or issues you could not resolve.
No


Question : An example of a difficult issue or bug and how you resolved.
While doing the extension 1 where i had to let the text adventure game accept abbreviated forms of commands I had a difficulty while writing the while loop and functions for the commands. The while loop was not terminating even after adding the quit and EOFerror line. I had to add some functions and format the code in the proper way.

Question : A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map).
I have created 3 classes Room, Game and Map class.
The Map class validates the map and checks if the there are exits to the room or not. After validating the room class is called which formats the rooms in the map. A dictionary of rooms has name,exits,items and description. The dictionary is passed as a parameter to Game class. The game class initializes the game and player is dropped to room 0(start method in Game class). There are 5 verbs implemented. Go, get look inventory, quit(baseline commmands). Player chooses the given command which he wants to proceed. The prompt method has a while loop which keeps on executing until the player decides to end the game. The go method is used to exit the room. The look method tells us about the current room state of the player. Get method is used to pick up items from the room and add them to the inventory. The inventory verb tells you about the items in the inventory of the player. The quit verb lets you quit the game.
Additional 3 extensions implemented:
1) A drop verb :
The drop method lets you drop the item from the inventory in the current room. If the item is not avaialable in the inventory then it will print that there is no such item in the inventory.
2) Abbreviation :
If we want to access the inventory, we dont have to type the whole word. We can just type 'in' or 'inv' and the inventory will be displayed.
Such abbreviation can be use for look get and go. We cannot use 'g' command as there are 2 words of starting with 'g'
3)Direction become verbs :
If we type 's' instead of go 'south' the prgram will understand that the player wants to go south. If the player has no exits in theparticular direction then it will print "There is no way to go ..."

