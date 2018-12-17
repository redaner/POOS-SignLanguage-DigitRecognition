def indexOfSubstring(string, substring):
    index = string.index(substring) - 2
    pictureName = string[index+2:index+14]
    return string[index] + "/" + pictureName

  
    