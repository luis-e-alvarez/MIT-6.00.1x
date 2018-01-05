class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
      result = ''
      for x in range (s.length-1, -1, -1):
        result = result + s[x]
      return result