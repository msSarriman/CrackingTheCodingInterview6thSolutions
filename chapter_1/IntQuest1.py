"""
MIT License

Copyright (c) 2019 Emmanouil Sarris

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
/**
 * 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
 * What if you cannot use additional data structures?
 * Hints: #44, #777, #732
 */
"""
def checkUnique(str):
    print("Using an integer as an array")
    num = 0
    for char in str:
        tempChar = ord(char) - ord('a')
        if (num & (1 << tempChar) > 1):
            return False
        num |= (1 << tempChar)
    return True


def checkUniqueDic(str):
    print("Using a dictionary")
    myDic = {}
    for char in str:
        if char in myDic:
            myDic[char] = myDic[char] + 1
        else:
            myDic[char] = 1
    for v in myDic.values():
        if v > 1:
            return "There are duplicates"
    return "All chars are unique"


def checkUniqueArr(str):
    print("Using a Boolean array")
    if len(str) > 128:
        return False
    charSet = [False for i in range(127)]
    for char in str:
        if charSet[ord(char) - ord('a')]:
            return False
        charSet[ord(char) - ord('a')] = True
    return True



if __name__ == "__main__":
    str = 'abcdefg'
    str1 = 'abccdef'

    # Using a Dictionary
    print(checkUniqueDic(str))
    print(checkUniqueDic(str1))

    # Using an array
    print(checkUniqueArr(str))
    print(checkUniqueArr(str1))

    # Without using a data structure
    print(checkUnique(str))
    print(checkUnique(str1))


