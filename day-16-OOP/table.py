from prettytable import PrettyTable

table = PrettyTable()

print(table)


table.add_column("Pokemon", ["Pikachu", "Squirtle"])                   #tapping into a method
table.add_column("Type", ["Electric", "Water"])

table.align = "l"                                                                        #changing an attribute


print(table)
