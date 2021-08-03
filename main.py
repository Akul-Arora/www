import csv
rows=[]
with open("main.csv","r") as ssname:
    csvr=csv.reader(ssname)
    for i in csvr:
        rows.append(i)
    
header=rows[0]
planet=rows[1:]
print(header)
print(planet[0])
header[0]="Row Number"
solar_system_planet_count={}
for pds in planet:
    if solar_system_planet_count.get(pds[11]):
        solar_system_planet_count[pds[11]]+=1
    else:
        solar_system_planet_count[pds[11]]=1

maxsolar=max(solar_system_planet_count,key=solar_system_planet_count.get)
print("solar system {} maximum planets {} we have discovered".format(maxsolar,solar_system_planet_count[maxsolar]))

solar_system_planet_mass=list(planet)

for pds in solar_system_planet_mass:
planet_mass=pds[3]
    if solar_system_planet_mass.get(pds[3]):
        solar_system_planet_mass[pds[3]]+=1
    else:
        solar_system_planet_mass[pds[3]]=1

maxsolar=max(solar_system_planet_count,key=solar_system_planet_mass.get)
print("solar system {} planets with mass {} we have discovered".format(maxsolar,solar_system_planet_mass[maxsolar]))