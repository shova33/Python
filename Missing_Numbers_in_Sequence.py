sequence = input("Enter the sequence of numbers separated by spaces: ")
seq_list = list(map(int, sequence.split()))
n = max(seq_list)
missing = [i for i in range(1, n + 1) if i not in seq_list]
print("Missing numbers:", missing)
