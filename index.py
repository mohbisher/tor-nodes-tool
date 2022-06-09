from termcolor import colored
from time import sleep
from nodes import Nodes

# the list of countries nodes in which the user will change to
countriesNodes = ["United States - us", "Canada - ca", "Britain - gb", "Saudi Arabia - sa", "Russia - ru", "Turkey - tr", "Poland - pl", "France - fr", "China - ch", "India - in"]

print(colored("TOR Nodes Tool", "blue"))
sleep(1)
print(colored("Do you want to use default path for TOR files or do you have a custom one? ", "blue"))
sleep(1)
path = input(colored("Press 'Enter' to use the default path, or insert your custom path here:", "blue"))
print(colored("Choose the entry, middle, and exit nodes of your TOR browser from the following list: ", "blue"))
sleep(1)

# printing the content of the list
for i in range(len(countriesNodes)):
    print(i+1,". ",countriesNodes[i])

# taking the nodes from the user
entryNode = input(colored("Insert your choice of Entry Node: ", "blue"))
middleNode = input(colored("Insert your choice of Middle Node: ", "blue"))
exitNode = input(colored("Insert your choice of Exit Node: ", "blue"))

# calling the function that will open the torrc file and configure the node being passed
Nodes.change_nodes(0, path, entryNode, middleNode, exitNode)
sleep(0.5)

print(colored("Processing.... ", "yellow"))
sleep(3)
print(colored("Your nodes have been changes successfully.", "green"))
sleep(1)
print(colored(f"Your new entry node: {entryNode}. \nYour new middle node: {middleNode}. \nYour new exit node: {exitNode}.", "blue"))
sleep(1)
print(colored("You may run your TOR now.", "green"))
sleep(1)



