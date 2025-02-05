s = "she is eating"
s = s.split()  # Split the string into words
longest = max(s, key=len)  # Find the word with the maximum length
print("Longest word:", longest)