from excusegen import get_excuse, get_excuses, add_excuse

print("One random excuse:")
print(get_excuse())

print("\nAll general excuses:")
print(get_excuses("class"))

print("\nAdd a new excuse:")
add_excuse("general", "Aliens deleted my code.")
print(get_excuses("general"))
