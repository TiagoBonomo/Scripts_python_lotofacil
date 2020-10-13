# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
numeros = []

# Set new_name to something other than 'quit'.
novo_n = ''

# Start a loop that will run until the user enters 'quit'.
while novo_n != 'sair':
    # Ask the user for a name.
    novo_n = input("Informe numero, ou entre 'sair': ")

    # Add the new name to our list.
    if novo_n != 'sair':
        numeros.append(novo_n)


# Show that the name has been added to the list.
print(numeros)