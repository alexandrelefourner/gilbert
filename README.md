

# gilbert

Generalized Hilbert ("gilbert") space-filling curve for rectangular domains of
arbitrary (non-power of two) sizes.

The discrete [Hilbert curve](https://en.wikipedia.org/wiki/Hilbert_curve) is a
widely used space-filling curve to map between N-dimensional and 1-D spaces
while preserving locality. However, classical algorithms only work for domains
whose sides are powers of two.

We present a simple recursive algorithm that generalizes the Hilbert curve
to rectangles of arbitrary sizes in 2D, and cuboids of even sizes in 3D.

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/55x31.png)

This algorithm was previously developed by [Jakub Červený](https://github.com/jakubcerveny/gilbert)
the purpose of this fork was to develop an adaptation for numpy management.

A notebook proposes to extract indexes in a single line of code for both 2d and 3d.

```indexes = numpy_gilbert3d(size,size,depth)```

### Examples

Running `numpy_gilbert2d` with two arguments (width, height) return a numpy array of
a space-filling curve with orthogonal steps only, as long as the width is even (100x63 shown):

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/100x63.png)

If the sizes are powers of two, a standard Hilbert curve is generated.
The algorithm extends naturally to 3D (8x6x4):

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/8x6x4.png)

40x30x20:

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/40x30x20.png)

Very flat is OK too (20x12x2):

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/20x12x2.png)


### Odd Sizes

In 2D, if the larger dimension is odd and the smaller is even, a single diagonal
step cannot be avoided (15x12):

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/15x12.png)

In 3D this is much worse, so odd dimensions should not be used (7x6x4):

![](https://raw.githubusercontent.com/jakubcerveny/gilbert/master/img/7x6x4.png)



---

Author: Jakub Červený. This [code](https://github.com/jakubcerveny/gilbert) is released under the 2-clause BSD license.
Modified by Alexandre LE FOURNER for easier numpy management

