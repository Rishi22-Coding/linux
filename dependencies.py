# First of all i was trying to save the json file in python dictionary inorder
# to get started with the initial work. I modified this .py file a lot of times.

#import json
import json

# Opening JSON file
f = open('depend.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
for i in data['Dependencies']:
    print(i)

# Closing file
f.close()
