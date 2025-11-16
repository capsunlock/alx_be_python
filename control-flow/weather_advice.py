# --- User Input ---
# Prompt the user for the weather condition and convert the input to lowercase
# to ensure the conditional checks are case-insensitive (e.g., 'Sunny' vs 'sunny').
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# --- Conditional Logic (if/elif/else) ---

# 1. Check for the 'sunny' condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

# 2. Check for the 'rainy' condition
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

# 3. Check for the 'cold' condition
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

# 4. Handle all other unexpected inputs
else:
    print("Sorry, I don't have recommendations for this weather.")