# 
#  * Write a function that, given a string, Finds the longest run of identical
#  * characters and returns an array containing the start and end indices of
#  * that run. If there are two runs of equal length, return the first one.
#  * For example:
#  *
#  *   longestRun("abbbcc") // [1, 3]
#  *   longestRun("aabbc")  // [0, 1]
#  *   longestRun("abcd")   // [0, 0]
#  *   longestRun("")       // None
#  *
#  * Try your function with long, random strings to make sure it handles large
#  * inputs well.
def longestRun(string):
    if(len(string) == 0):
        return None
    lengthOfCurrentRun = 0
    lengthOfLongestRun = 0
    current = ''
    longestSubIndex = []
    longestIndex = []
    longestRunResults = []
    for letter in range(len(string)):
      if string[letter] == current and letter != len(string) - 1:
        lengthOfCurrentRun += 1
        longestSubIndex.append(letter)
      else:
        if(letter == len(string) - 1 and string[letter] == current):
          lengthOfCurrentRun += 1
          longestSubIndex.append(letter)
        current = string[letter]
        if lengthOfCurrentRun > lengthOfLongestRun:
          lengthOfLongestRun = lengthOfCurrentRun
          lengthOfCurrentRun = 1
          longestIndex = longestSubIndex
          longestSubIndex = []
          longestSubIndex.append(letter)
        else:
          longestSubIndex = []
          longestSubIndex.append(letter)
          lengthOfCurrentRun = 1
    startOfRun = longestIndex[0]
    endOfRun = longestIndex[len(longestIndex) - 1]
    longestRunResults = [startOfRun, endOfRun]
    print(longestRunResults)
    return longestRunResults
