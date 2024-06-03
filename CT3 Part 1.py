def calculate_total_meal_cost():
    # Ask the user to enter the charge for the food
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculate the tip amount (18% of food charge)
    tip_amount = food_charge * 0.18

    # Calculate the sales tax amount (7% of food charge)
    tax_amount = food_charge * 0.07

    # Calculate the total price
    total_price = food_charge + tip_amount + tax_amount

    # Display each of these amounts and the total price
    print(f"\nCharge for the food: ${food_charge:.2f}")
    print(f"Tip amount (18%): ${tip_amount:.2f}")
    print(f"Sales tax amount (7%): ${tax_amount:.2f}")
    print(f"Total price: ${total_price:.2f}")

# Run the program
calculate_total_meal_cost()