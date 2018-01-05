class Solution:
  def polysum(self, n, s):
    """
    n: is int
    s: is int
    returns: float rounded to 4 decimal places
    """
    import math
    perimeter = s * n
    area = (0.25 * n * math.pow(s, 2)) / (math.tan(math.pi/n))
    result = math.pow(perimeter, 2) + area
    return(round(result,4))
solution = Solution()
