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
 *  Compression: Implement a method to perform basic string compression using the counts
 * of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
 * "compressed" string would not become smaller than the original string, your method should return
 * the original string. You can assume the string has only uppercase and lowercase letters (a - z).
 * Hints: #92, # 110
 * - Do the easy thing first. Compress the string, then compare the lengths
 * - Be careful that you aren't repeatedly concatenating strings together. This can be very
 * inefficient.
 */
"""


def compress(str1):
    if len(str1) == 0:
        return False
    sb = []
    occurrencesCounter = 0
    tempChar = str1[0]
    for char in str1:
        if tempChar == char:
            occurrencesCounter += 1
        else:
            sb.append(tempChar)
            sb.append(str(occurrencesCounter))
            occurrencesCounter = 0
            tempChar = char
    sb.append(tempChar)
    sb.append(str(occurrencesCounter))
    return ''.join(sb) if len(sb) < len(str1) else str1


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "aaabbbbccccdeeeeeeeeee"
    s3 = "abcdeeeeeee"

    print(compress(s1))
    print(compress(s2))
    print(compress(s3))