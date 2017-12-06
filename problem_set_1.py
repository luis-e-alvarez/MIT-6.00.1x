#Problem 1
s = 'dupqkcheffhcazakezp'
count = 0
for letter in s:
  if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    count += 1
print('Number of vowels: ' + str(count))

#Problem 2: Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

bobCount = 0
for i in range(len(s) - 2):
    if s[i] + s[i+1] + s[i+2] == 'bob':
        bobCount += 1
print('Number of times bob occurs is: ' + str(bobCount))

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

longestStr = ''
for n in range(len(s)):
  currentStr = s[n]
  for j in range (n+1, len(s)):
    if s[j] >= currentStr[len(currentStr) - 1]:
        currentStr += s[j]
    else:
        break
  if len(longestStr) < len(currentStr):
      longestStr = currentStr

print('Longest substring in alphabetical order is: ' + longestStr)

