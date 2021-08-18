# Add your code here
medical_costs = {}
medical_costs.update({"Marina": 6607, "Vinay": 3225.0})

medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

print(medical_costs)
medical_costs["Vinay"] = 3325.0

print(medical_costs)

total_cost = 0
for value in medical_costs.values():
  total_cost += value

print(total_cost)

average_cost = total_cost / len(medical_costs)
print("The Average Insurance Cost: {}".format(average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]

ages = [27, 24, 43, 35]

zipped_ages = list(zip(names, ages))

names_to_ages = {key:value for key, value in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get("Marina", None)

print("Marina's age is {}".format(marina_age))

medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}, "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}, "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 2, "Smoker": "Smoker", "Insurance_cost": 16444.0}, "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})

print(medical_records)

print("Connie's insurance cost is {} dollars".format(medical_records.get("Connie").get("Insurance_cost")))

medical_records.pop("Vinay")

for key, value in medical_records.items():
  print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(Name = key, Age = value.get("Age"), Sex = value.get("Sex"), Smoker = value.get("Smoker"), BMI = value.get("BMI"), Insurance_cost = value.get("Insurance_cost")))


























