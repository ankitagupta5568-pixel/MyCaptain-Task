# Function to print positive numbers from a list
def print_positive_numbers(num_list):
    positive_nums = []

    for num in num_list:
        if num > 0:
            positive_nums.append(num)

    return positive_nums


# Example inputs
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Outputs
print("Output for list1:", print_positive_numbers(list1))
print("Output for list2:", print_positive_numbers(list2))
