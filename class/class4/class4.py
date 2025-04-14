def check_ingredients(ingredients):
    required_ingredients = {
        "flour": False,
        "eggs": False,
        "milk": False,
        "oil": False
    }
    
    missing_ingredients = []
    
    # Check what ingredients we have and what we're missing
    for item in ingredients:
        if item in required_ingredients:
            required_ingredients[item] = True
    
    # Create list of missing ingredients
    for item, available in required_ingredients.items():
        if not available:
            missing_ingredients.append(item)
    
    return required_ingredients, missing_ingredients

def check_sehri_time(current_time, ingredients):
    # Get ingredient status
    ingredients_status, missing_items = check_ingredients(ingredients)
    has_all_ingredients = all(ingredients_status.values())
    
    # Time checks
    if current_time == "3:00":
        if not has_all_ingredients:
            print("Check the ingredients")
            print("Missing ingredients:", ", ".join(missing_items))
            print("Wake up Both Male and female side")
        else:
            print("Wake up Female Side")
    
    elif current_time == "4:30":
        if has_all_ingredients:
            print("Wake up Male Side")

# Example usage:
available_ingredients = ["flour", "eggs", "oil"]
check_sehri_time("3:00", available_ingredients)