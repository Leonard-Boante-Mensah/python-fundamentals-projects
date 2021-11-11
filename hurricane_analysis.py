# names of final_dictionary_hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
#print(len(damages))
def updated_damages(damages):
  new_list = [x if x == 'Damages not recorded' 
                  else (float(x[:-1]) * float(conversion.get(x[-1]))) 
                    for x in damages]
  return new_list

  # for damage in damages:
  #   if damage == "Damages not recorded":
  #     new_list.append(damage)
  #   else:
  #     new_list.append(float(damage[:-1]) * float(conversion.get(damage[-1])))
  # return new_list

updated_damages = updated_damages(damages)
print("\n ********** UPDATE DAMAGES ************** \n")
print(updated_damages)
# name_month_dic = {key:value for key, value in list(zip(names, months))}

def construct_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  final_dictionary = dict()
  for hurricane in range(len(names)):
    final_dictionary[names[hurricane]] = {"Name": names[hurricane],
                                          "Month": months[hurricane],
                                          "Year": years[hurricane],
                                          "Max Sustained Wind": max_sustained_winds[hurricane],
                                          "Areas Affected": areas_affected[hurricane],
                                          "Damage": damages[hurricane],
                                          "Deaths": deaths[hurricane]}
  return final_dictionary

final_dictionary_hurricanes = construct_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print("\n ************ NAME AS KEY DICTIONARY ************** \n")
print(final_dictionary_hurricanes)
# print(final_dictionary_hurricanes.get("San Felipe II Okeechobee"))
# 2
def year_key_dictionary(input_dictionary):
  year_key_dictionary= {}
  for index in input_dictionary:
    year = input_dictionary[index]['Year']
    new_dictionary = input_dictionary[index]
    if year in year_key_dictionary:
      year_key_dictionary[year].append(new_dictionary)
    else:
      year_key_dictionary[year] = [new_dictionary]
  return year_key_dictionary
  
print("\n *********** YEAR AS KEY DICTIONARY ******************* \n")
print(year_key_dictionary(final_dictionary_hurricanes))


# Create a Table
# 3
def affected_area_dictionary(input_dictionary):  
  areas_affected = {}
  for dict_key in input_dictionary:
    for affected_area in input_dictionary[dict_key]["Areas Affected"]:
      if affected_area in areas_affected:
        areas_affected[affected_area] += 1
      else:
        areas_affected[affected_area] = 1
  return areas_affected

print("\n ******* NUMBER OF TIMES AREA HAS BEEN AFFECTED ******* \n")
# 4
# Counting Damaged Areas
areas_affected = affected_area_dictionary(final_dictionary_hurricanes)
print(areas_affected)

# 5 
# Calculating Maximum Hurricane Count
def most_affected_hurricane_area(dictionary):
  key, max_value = max(dictionary.items(), key = lambda k : k[1])
  return f"The most affected area is {key} with {max_value} counts"


most_affected_area_counts = most_affected_hurricane_area(areas_affected)
print("\n *** MOST AFFECTED AREA AND COUNT *** \n")
print(most_affected_area_counts)

# find highest mortality hurricane and the number of deaths
def greatest_num_deaths(final_dictionary_hurricanes):
  deaths = {}
  greatest_deaths = 0
  for hurricane in final_dictionary_hurricanes:
    if final_dictionary_hurricanes[hurricane]["Deaths"] > greatest_deaths:
      greatest_deaths = final_dictionary_hurricanes[hurricane]["Deaths"]
      deadliest = hurricane
  return f"{deadliest} had the greatest number of deaths with {greatest_deaths} counts"

print("\n **** HURRICANE WITH THE GREATEST NUMBER OF DEATHS ******* \n")
print(greatest_num_deaths(final_dictionary_hurricanes))
# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricane_dictionary):
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for index in hurricane_dictionary:
    num_deaths = hurricane_dictionary[index]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricane_dictionary[index])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricane_dictionary[index])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricane_dictionary[index])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricane_dictionary[index])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricane_dictionary[index])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricane_dictionary[index])
  return hurricanes_by_mortality

print("******** HURRICANE'S RATINGS ***********")
print(categorize_by_mortality(final_dictionary_hurricanes))

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(hurricane_dictionary):
  damage = {}
  greatest_damage = 0
  for hurricane in final_dictionary_hurricanes.keys():
    if final_dictionary_hurricanes[hurricane]["Damage"] != "Damages not recorded":
      if final_dictionary_hurricanes[hurricane]["Damage"] > greatest_damage:
        greatest_damage = final_dictionary_hurricanes[hurricane]["Damage"]
        priciest = hurricane
  return {priciest: greatest_damage}

print("\n ***** PRINT HURRICANE WITH THE GREATEST DAMAGE ***** \n")
print(greatest_damage(final_dictionary_hurricanes))

# 9
# Rating final_dictionary_hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize final_dictionary_hurricanes in new dictionary with damage severity as key
def categorize_by_damage(hurricane_dictionary):
  mortality_scale = {0: 0,
                 1: 100000000,
                 2: 1000000000,
                 3: 10000000000,
                 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for index in hurricane_dictionary:
    num_of_damage = hurricane_dictionary[index]['Damage']
    if type(num_of_damage) == str:
      pass
    elif num_of_damage == mortality_scale[0]:
      hurricanes_by_damage[0].append(hurricane_dictionary[index])
    elif num_of_damage > mortality_scale[0] and num_of_damage <= mortality_scale[1]:
      hurricanes_by_damage[1].append(hurricane_dictionary[index])
    elif num_of_damage > mortality_scale[1] and num_of_damage <= mortality_scale[2]:
      hurricanes_by_damage[2].append(hurricane_dictionary[index])
    elif num_of_damage > mortality_scale[2] and num_of_damage <= mortality_scale[3]:
      hurricanes_by_damage[3].append(hurricane_dictionary[index])
    elif num_of_damage > mortality_scale[3] and num_of_damage <= mortality_scale[4]:
      hurricanes_by_damage[4].append(hurricane_dictionary[index])
    elif num_of_damage > mortality_scale[4]:
      hurricanes_by_damage[5].append(hurricane_dictionary[index])
  return hurricanes_by_damage

print("\n ***** CATEGORIZE HURRICANES BASED ON DAMAGES ****** \n")
print(categorize_by_damage(final_dictionary_hurricanes))