family = {
    'grandpa': ('Alex', 76),
    'grandma': ('Nona', 74),
    'dad': ('Greg', 48),
    'mom': ('July', 45),
    'son_older': ('Bob', 18),
    'son_middle': ('Alex', 15),
    'son_young': ('Mark', 10)
}

age = []

for key in family.keys():
    age.append(family[key][1])
age_diff = max(age) - min(age)

print(age_diff)
