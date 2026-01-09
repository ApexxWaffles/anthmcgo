# create the initial variables below
# sex = 0 for female, 1 for male
# smoker = 0 for non-smoker, 1 for smoker
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's new insurance cost after a 4 year increase in age is " + str(new_insurance_cost) + " dollars.")


# change_in_insurance_cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
age -= 4
# changes age back to 28 by subtracting 4 
bmi += 3.1
# adds 3.1 to the bmi from above. 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost 

print("The change in cost of insurance after increasing the BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor
bmi -= 3.1
sex = 1
# sex = 0 for female, 1 for male
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost 
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

# Extra Practice

# Smoker change  
smoker = 1
sex = 0 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost 
print("The change in estimated cost for being a smoker is " + str(change_in_insurance_cost) + " dollars.")


# num of childern change 
num_of_children = 5 
sex = 0 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost 

print("The change in estimated cost for having " + str(num_of_children) + " kids is " + str(change_in_insurance_cost) + " dollars.")
