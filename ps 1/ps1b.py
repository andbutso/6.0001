# Problem Set 1b
# Name: George Mu
# Collaborators: None
# Time Spent: 00:10


# Get user inputs
annual_salary = int(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = int(input('Enter the cost of your dream home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

# Initialize starting variables
r = 0.05 # Annual interest rate of savings
portion_down_payment = 0.20 # Share to total_cost that is needed for the down payment
current_savings = 0 # Starting savings amount
months = 0 # Months required to save up

# Convert everything to a monthly basis
required_savings = total_cost * portion_down_payment
monthly_savings_contribution = (annual_salary / 12) * portion_saved
monthly_r = r / 12

# Run the calculation
while current_savings < required_savings:
    current_savings = current_savings * (1 + monthly_r) # Deposit interest
    current_savings += monthly_savings_contribution # Deposit savings from paycheck
    months += 1
    if months % 6 == 0 and months > 0:
        monthly_savings_contribution = monthly_savings_contribution * (1 + semi_annual_raise)



print("Number of Months:",months)
