#!/bin/bash
pdflatex -synctex=1 -interaction=nonstopmode dissertation.tex
bibtex ch1/ch1.aux
bibtex ch2/ch2.aux
bibtex ch3/ch3.aux
bibtex ch4/ch4.aux
bibtex ch5/ch5.aux
bibtex ch5_appendix/ch5_appendix.aux
pdflatex -synctex=1 -interaction=nonstopmode dissertation.tex
