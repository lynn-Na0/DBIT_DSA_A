def count_frequency(text):
   
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1 
    return frequency

text = "data structures and algorithms"
char_frequencies = count_frequency(text)

for char, count in char_frequencies.items():
    print(f"'{char}': {count}")