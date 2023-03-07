"""
In this code, I have made the keys argument as a *keys which means it will take multiple keys and convert it 
into a tuple. I have also added a check to see if the key is present in the dictionary before printing its 
value, and added an error message if the key is not found.
"""
def print_values_of(dictionary, *keys):
    for key in keys:
        if key in dictionary:
            print(dictionary[key])
        else:
            print(f"Key '{key}' not found in the dictionary")

simpson_catch_phrases = {
    "lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", 
    "maggie": "(Pacifier Suck)"

}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')
