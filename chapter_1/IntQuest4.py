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
 * Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A
 * palindrome is a word or phrase that is the same forwards and backwards. A permutation
 * is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
 * EXAMPLE
 * Input: Tact Coa
 * Output: True (permutations: "taco cat". "atco cta". etc.)
 * Hints: #106, #121, #134, #136
 * -You do not have to-and should not-generate all permutations. This would be very
 * inefficient.
 * -What characteristics would a string that is a permutation of a palindrome have?
 * -Have you tried a hash table? You should be able to get this down to 0 (N) time.
 * -Can you reduce the space usage by using a bit vector?
 */
"""


def isPalindrome(str):
    length = len(str)
    mySet = set()

    for char in str:
        if char in mySet:
            mySet.remove(char)
        else:
            mySet.add(char)

    if length % 2 == 0 and len(mySet) == 0:
        return True
    elif length % 2 != 0 and len(mySet) == 1:
        return True
    return False


if __name__ == "__main__":
    s1 = "thisisacccthisisa"
    s2 = "thisisaacccthisisa"
    s3 = "thisadfvadsvas;df"
    print(isPalindrome(s1))
    print(isPalindrome(s2))
    print(isPalindrome(s3))

