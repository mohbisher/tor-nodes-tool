import os
from termcolor import colored
from time import sleep


class Nodes:
    def change_nodes(self, path, entryNode, middleNode, exitNode):
        #Defalt path in MacOS
        #~/Library/Application Support/TorBrowser-Data/Tor/

        # checking if the user inserted a custom path or not
        while True:
            if path=="":
                path="~/Library/Application Support/TorBrowser-Data/Tor/"

            # try catch in case the path is incorrect, which means that the folder was not found
            try:
                torrc_file = open(os.path.expanduser(path+"/torrc"), "r") # opening the torrc file to read its lines
                nodesList = ['EntryNodes', 'ExitNodes', 'MiddleNodes']
                linesList = [] # the lines of the file will be insterted into this list to be used for overwriting the file later
                file_data = torrc_file.readlines() # reading the lines of the file
                for line in file_data: #1
                    for word in nodesList:
                        if (line.startswith(word)): # checking if a line starts with one of the list's words
                            line = line.replace(line, '') # if yes, we delete it so we can add the line again with the new country node when the tool is launched again
                    linesList.append(line) # appending the rest of the lines to this list
                torrc_file.close()
                torrc_file = open(os.path.expanduser(path+"/torrc"), 'w') # opening the same file again in writing mode
                for line in linesList:
                    torrc_file.write(line) # overwriting the old content with the new content

                # writing the node countries inserted by the user
                torrc_file.write("\nEntryNodes {" + entryNode + "} StrictNodes 0")
                torrc_file.write("\nMiddleNodes {" + middleNode + "} StrictNodes 0")
                torrc_file.write("\nExitNodes {" + exitNode + "} StrictNodes 0")
                torrc_file.close()
                break # breaking the loop bcz we're done

            # an exception in case the file was not found
            except FileNotFoundError:
                print(colored("The meant destination was not found, the path is incorrect", "red"))
                sleep(1)
                # setting a new value for the path to be checked at the beginning of the loop
                path = input(colored("Re-insert your custom path, or press 'Enter' to use the default path:", "blue"))
