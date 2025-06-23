class MultidimensionalArray:

    # Take the number of rows from the user
    rows = int(input("Enter the number of rows: "))

    # Take the number of columns from the user
    clos = int(input("Enter the number of columns: "))

    # Initialize an empty list to store the 2D array
    array = []

    # Loop to read elements for each row
    for i in range(rows):
        row = []  # Temporary list to store one row
        for j in range(clos):
            # Take input for each element and convert it to integer
            value = input(f"Enter the element at position [{i}][{j}]: ")
            row.append(int(value))  # Add the element to the row
        array.append(row)  # Add the completed row to the 2D array

    # Display the 2D array
    print("Printing the 2D array:")
    for i in range(rows):
        for j in range(clos):
            # Print each element in the same row with a space
            print(array[i][j], end=" ")
        print()  # Newline after each row
