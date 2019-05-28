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
 * URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
 * has sufficient space at the end to hold the additional characters, and that you are given the "true"
 * length of the string. (Note: If implementing in Java, please use a character array so that you can
 * perform this operation in place.)
 * EXAMPLE
 * Input: "Mr John Smith"
 * Output: "Mr%20John%20Smith"
 * Hints:
 * - It's often easiest to modify strings by going from the end of the string to the beginning.
 * - You might find you need to know the number of spaces. Can you just count them?
 */
"""
def urlify(str):
    myResult = []
    for char in str:
        if char == " ":
            myResult.append('%')
            myResult.append('2')
            myResult.append('0')
        else:
            myResult.append(char)
    return ''.join(myResult)


if __name__ == "__main__":
    s1 = "This is a sample string to edit"
    s2 = urlify(s1)
    print(s1)
    print(s2)