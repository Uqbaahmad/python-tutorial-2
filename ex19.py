




print("Lets practice everything")
print("You\'d need to know \'bout escape with \\ that do:")
print("\n newline and \t tabs")

poem = """
Because I could not stop for Death,\n
He kindly stopped for me;\n
The carriage held but just ourselves\n
And Immortality."""

print("-" * 20)
print(poem)
print("-" * 20)

five = 10 - 2 + 3 - 6
print("f This should be five: {five}")

def formula(started):
    jelly_beans = started * 5
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates 

start_point = 10000
beans, jars, crates = formula(start_point)

# remember that this is another way to format a string
print("f With a starting point of: {}".format(start_point))

# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, {cartes} cartes.")

start_point = start_point / 10

print("We can also do that this way")
secret_formula = formula(start_point)

# this is an easy way to apply a list to a format string
print("f We'd have {} beans, {} jars, {} crates".format(*secret_formula))
