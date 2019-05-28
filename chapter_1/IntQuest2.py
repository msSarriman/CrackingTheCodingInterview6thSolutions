"""
/*
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
*/
/**
 * Check Permutation: Given _02two strings, write a method to decide if _01one is a permutation of the other
 * O(N)
 */
"""
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return "not a match"

    myDict = {}

    # Count the chars in str1
    for char in str1:
        if char in myDict:
            myDict[char] = myDict[char] + 1
        else:
            myDict[char] = 1

    # compare with the chars in str2
    for char in str2:
        if char in myDict:
            myDict[char] = myDict[char] - 1
        else:
            return False

    # check if all the values are zero
    for v in myDict.values():
        if v is not 0:
            return False

    return True


if __name__ == "__main__":
    s1 = "absolute"
    s2 = "luabsote"
    s3 = "luubsote"
    s4 = "absolutee"

    a = "abcdefghijklmnopqrstuvwxyz"
    b = "zyxwvutsrqponmlkjihgfedcba"

    print(checkPermutation(s1, s2))
    print(checkPermutation(s1, s3))
    print(checkPermutation(s1, s4))
    print(checkPermutation(a, b))