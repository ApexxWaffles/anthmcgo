# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here;
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = "Here is the actual insurance cost data: " + str(list(zip(names, insurance_costs)))
print(insurance_data)

estimated_insurance_data =[]
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

maria_insurance_cost_difference = maria_insurance_cost - insurance_costs[0]
rohan_insurance_cost_difference = rohan_insurance_cost - insurance_costs[1]
valentina_insurance_cost_difference = valentina_insurance_cost - insurance_costs[2]
print("The difference between the estimated and actual insurance cost for Maria is " + str(maria_insurance_cost_difference) + " dollars.")
print("The difference between the estimated and actual insurance cost for Rohan is " + str(rohan_insurance_cost_difference) + " dollars.")
print("The difference between the estimated and actual insurance cost for Valentina is " + str(valentina_insurance_cost_difference) + " dollars.")  
# bouns part - estimate Akira's insurance cost and update the lists
Akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 1)
names.append("Akira")
insurance_costs.append(29310.0)
estimated_insurance_data.append(("Akira", Akira_insurance_cost))
print("Here is the updated estimated insurance cost data: " + str(estimated_insurance_data))
Akira_insurance_cost_difference = Akira_insurance_cost - insurance_costs[3]
print("The difference between the estimated and actual insurance cost for Akira is " + str(Akira_insurance_cost_difference) + " dollars.")  
