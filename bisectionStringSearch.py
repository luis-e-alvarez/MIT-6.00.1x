def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    max = len(aStr)
    min = 0
    mid = int((max + min) / 2)
    if(aStr[mid] == char):
      print(True)
      return True
    if(len(aStr) == 1):
      print(False)
      return False
    else:
      if(char > aStr[mid]):
        isIn(char, aStr[mid:max])
      else:
        isIn(char, aStr[min: mid])