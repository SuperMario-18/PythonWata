word1 = input()
word = word1[0].lower() + word1[1:]
for character in word:
  if character.isupper():
    word = word.replace(character,"_"+character.lower())
    word = word.lower()
print(word)