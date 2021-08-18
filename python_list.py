names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = zip(names, insurance_costs)
medical_records = list(medical_records)

print(medical_records)

num_medical_records = len(medical_records)
print(num_medical_records)

first_medical_record = medical_records[0]
print("Here is the first medical record ",first_medical_record)

print("Here are the medical records sorted by insurance cost: ", sorted(medical_records, key=lambda insurance_cost: insurance_cost[1]))

sorted_list = sorted(medical_records, key=lambda insurance_cost: insurance_cost[1])

cheapest_three = sorted_list[:3]

print(cheapest_three)

priciest_three = sorted_list[-3:]
print(priciest_three)

occurences_paul = names.count("Paul")
print("There are ", occurences_paul, "individuals with the name Paul in our medical records.")











