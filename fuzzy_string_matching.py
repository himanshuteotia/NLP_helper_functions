# install package

# !pip install fuzzywuzzy

with open("cities.txt") as f:
    cities = f.read().split("\n")

len(cities)


from fuzzywuzzy import process
def get_matches(query, choices, limit=3):
    result = process.extract(query, choices, limit=limit)
    return result

print(get_matches("merrut",cities))