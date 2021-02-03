from functions import *
from PLP import *

if __name__ == "__main__":
    while(1):
        query = input().split()
        if query[0] == "quit":
            break
        if not handle_PLP(query) or \
           not handle_functions(query):
           print("Query not recognized")
