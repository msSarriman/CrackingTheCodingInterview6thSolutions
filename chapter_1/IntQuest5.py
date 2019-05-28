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
*/
/**
 * One Away: There are _03three types of edits that can be performed on strings: insert a character,
 * remove a character, or replace a character. Given _02two strings, write a function to check if they are
 * _01one edit (or zero edits) away.
 * EXAMPLE
 * pale, pIe -> true
 * pales. pale -> true
 * pale. bale -> true
 * pale. bake -> false
 * Hints: #23, #97, #130
 * - Start with the easy thing. Can you check each of the conditions separately?
 * - What is the relationship between the "insert character" option and the "remove character" option?
 * Do these need to be _02two separate checks?
 * - Can you do all _03three checks in a single pass?
 */
 """


def oneWay(str1, str2):
    """Finds if str1 and str2 are one edit away

    Args:
        str1:
        str2:

    Returns:
        Boolean if the condition is met
    """
    #get shorter and longer string
    s1 = str1 if len(str1) > len(str2) else str2
    s2 = str1 if len(str1) < len(str2) else str2

    index1, index2 = 0, 0
    bombFlag = False
    while index1 < len(str1) and index2 < len(str2):
        if s1[index1] != s2[index2]:
            if bombFlag:
                return False
            bombFlag = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True


if __name__ == "__main__":
    s1 = "thisisok"
    s2 = "thisiqok"
    s3 = "thisisokna"
    s4 = "thsisok"
    s5 = "thisisokn"

    print(oneWay(s1, s2))
    print(oneWay(s1, s4))
