numbers = [10, -4, 0, 7, -2, 5]

positive_count = sum(1 for n in numbers if n > 0)
negative_count = sum(1 for n in numbers if n < 0)

print("Positive:", positive_count)
print("Negative:", negative_count)
