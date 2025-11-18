data = [10, 5, 25, 8, 15, 42, 3]
with open("numbers.txt", "w") as f:
    for number in data:
        f.write(str(number) + "\n")
print("The numbers have been successfully written to numbers.txt.")
print("*" * 30)


numbers_from_file = []
with open("numbers.txt", "r") as f:
    for line in f:
        number = int(line.strip())
        numbers_from_file.append(number)

max_number = max(numbers_from_file)
print(f"Read list: {numbers_from_file}")
print(f"Result (Max): {max_number}")
