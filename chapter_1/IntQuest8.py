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
 * Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
 * column are set to O.
 * Hints: # 17, #74, #102
 * - If you just cleared the rows and columns as you found Os, you'd likely wind up clearing
 * the whole matrix.Try finding the cells with zeros first before making any changes to the
 * matrix.
 * - Can you use 0 (N) additional space instead of 0 (N 2 )? What information do you really
 * need from the list of cells that are zero?
 * - You probably need some data storage to maintain a list of the rows and columns that
 * need to be zeroed. Can you reduce the additional space usage to a(1) by using the
 * matrix itself for data storage?
 */
"""

def zerofy(matrix = []):
    skipX = set()
    skipY = set()
    for i in range(0, len(matrix)):
        if i not in skipX:
            for j in range(0, len(matrix)):
                if matrix[i][j] == 0 && j not in skipY:
                    skipX.add(i)
                    skipY.add(j)
                    del matrix[i]
                    matrix[i].insert(i, [0 for k in range(0, len(matrix))])
                    for k in range(0, len(matrix)):
                        matrix[k][j] = 0
                    break
    return matrix



