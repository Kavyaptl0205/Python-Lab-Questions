text = input("Enter a sentence or paragraph: ")

# Word frequency counter
words = text.lower().split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

print("\n--- WORD FREQUENCY ---")
for word in word_freq:
    print(word, ":", word_freq[word])

# Character frequency counter
char_freq = {}

for ch in text.lower():
    if ch != " ":
        if ch in char_freq:
            char_freq[ch] = char_freq[ch] + 1
        else:
            char_freq[ch] = 1

print("\n--- CHARACTER FREQUENCY ---")
for ch in char_freq:
    print(ch, ":", char_freq[ch])