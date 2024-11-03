# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

num = 1

for integer in range(1, rows + 1):
    for inner in range(integer):
        print(num, end=" ")
        num += 1
    print()  
