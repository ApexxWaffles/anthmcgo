names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
# for cost in actual_insurance_costs:
#     total_cost += cost
# Converted to while loop by using an index counter to iterate through the list
i = 0
while i < len(actual_insurance_costs):
    total_cost += actual_insurance_costs[i]
    i += 1

average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

for i in range(len(names)):
    name = names[i]
    insurance_cost= actual_insurance_costs[i]
    cost_difference = estimated_insurance_costs[i] - actual_insurance_costs[i]
    print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
    if insurance_cost > average_cost:
        print("The insurance cost for "+ name + " is above average.")
        print("The cost difference for "+ name + " is " + str(cost_difference))
    elif insurance_cost < average_cost:
        print("The insurance cost for "+ name + " is below average.")
        print("The cost difference for "+ name + " is " + str(cost_difference))
    else:
        print("The insurance cost for "+ name + " is equal to the average.")
        print("The cost difference for "+ name + " is " + str(cost_difference))
  
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]
print(updated_estimated_costs)

secret_keys = [["Amy", "Amy123"], ["Zara", "abcde"], ["Donald", "321"]]

for pair in secret_keys:
  for item in pair:
    print(item)