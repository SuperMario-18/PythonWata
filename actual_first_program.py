word = list(input())
vowel = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for ch in word:
   if ch in vowel:
      print('vowel')
   elif ch in consonant:
      print('consonant')
   else:
      break