# create the initial variables below
age = 28
sex = 0
smoker = 1
num_of_children = 3
bmi = 26.2

# Add insurance estimate formula below
insurance_cost = (250 * age )- (128 * sex) + (370 * bmi )+ (425 * num_of_children) + (2400 * smoker) - 12500

print("This person's insurance cost is " + str(insurance_cost) +" dollars")

# Age Factor
age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost)+ " dollars." )



# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = (250 * age )- (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance after increasing the BMI by 3.1 years is " + str(change_in_insurance_cost)+ " dollars." )

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a male instead of female is " + str(change_in_insurance_cost)+ " dollars." )


# Extra Practice
sex = 0
smoker = 0

new_insurance_cost = (250 * age) - (128 * sex )+ (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being a smoker instead of non smoker is " + str(change_in_insurance_cost)+ " dollars." )



smoker = 1
num_of_children = 5
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for having 5 children instead of 3 children is " + str(change_in_insurance_cost)+ " dollars." )