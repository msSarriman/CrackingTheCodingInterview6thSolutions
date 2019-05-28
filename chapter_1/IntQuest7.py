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
 * Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
 * bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
 * Hints: #51, #100
 * - Try thinking about it layer by layer. Can you rotate a specific layer?
 * - Rotating a specific layer would just mean swapping the values in four arrays. Ifyou were
 * asked to swap the values in _02two arrays, could you do this? Can you then extend it to four
 * arrays?
 */
"""
from random import randint


xDim, yDim = 0, 0
rotated = [[]]


def rotate(matrix):
    global rotated
    rotated = [[0 for i in range(0, len(matrix))] for i in range(0, len(matrix))]
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix) - 1, -1, -1):
            print(matrix[j][i])
            addElement(matrix[j][i])


def addElement(element):
    global xDim, yDim
    xDim
    yDim
    rotated[xDim][yDim] = element
    yDim += 1
    if yDim == len(rotated):
        yDim = 0
        xDim += 1


if __name__ == "__main__":
    size = int(input("Please enter matrix size:"))
    matrix = [[0 for i in range(0, size)] for i in range(0, size)]

    # initialize the matrix
    for i in range(size):
        for j in range(size):
            matrix[i][j] = randint(0, 20)

    # rotate it
    rotate(matrix)

    size = size
    # print the original
    print("original:")
    for i in range(0, size):
        for j in range(0, size):
            print(matrix[i][j], end="|")
        print("")

    # print the rotated
    print("reversed:")
    for i in range(0, size):
        for j in range(0, size):
            print(rotated[i][j], end="|")
        print("")
