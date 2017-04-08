planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

print('All planets, plus pluto: ' + str(planet_list))

rocky_planets = planet_list[:4]

print('The rocky planets are: ' + str(rocky_planets))

planet_list.pop()

# gas_planets = planet_list

# print(gas_planets)

# for planet in gas_planets:
#     if gas_planets.index(planet) < 4:
#         gas_planets.remove(planet)

# print('The gas giants are: ' + str(gas_planets))

missions = [('USS Adelphi', "Mercury", "Mars"),
('USS Ambassador', "Uranus", "Neptune"),
('USS Enterprise', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
('USS Excalibur', 'Mercury', 'Venus', 'Earth', 'Mars'),
('USS Exeter', 'Venus', 'Mars', 'Saturn', 'Neptune'),
('USS Gandhi', 'Uranus', 'Neptune'),
('USS Horatio', 'Venus', 'Earth'),
('USS Valdemar', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'),
('USS Yamaguchi', 'Mercury', 'Venus', 'Earth', 'Mars'),
('USS Zhukov', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
]

for planet in planet_list:
    print('######## ' + planet + ' ########')
    for mission in missions:
        if planet in mission:
            print(mission[0])


