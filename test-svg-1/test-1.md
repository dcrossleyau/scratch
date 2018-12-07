# Test SVG in GitHub Markdown - examples

SVG in Markdown.

Using html img with no height or width attribute:

<img src="https://cdn.jsdelivr.net/gh/dcrossleyau/scratch/test-svg-1/test-1.svg" alt="test SVG">

Using html img height and width attribute:

<img src="https://cdn.jsdelivr.net/gh/dcrossleyau/scratch/test-svg-1/test-1.svg" alt="test SVG" width="250" height="250">

Using html img width="100%" to place the image in the centre:

<img src="https://cdn.jsdelivr.net/gh/dcrossleyau/scratch/test-svg-1/test-1.svg" alt="test SVG" width="100%" height="150">

Using Markdown link syntax:

![test SVG](https://cdn.jsdelivr.net/gh/dcrossleyau/scratch/test-svg-1/test-1.svg "the test SVG")

Using relative source will work with local doc conversion with 'pandoc' (but not via GitHub):

![test SVG](test-1.svg "the test SVG")

<img src="test-1.svg" alt="test SVG">
