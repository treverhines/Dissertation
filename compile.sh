#!/bin/bash
pdflatex -synctex=1 -interaction=nonstopmode dissertation.tex
bibtex ch4/ch4.aux
bibtex ch5/ch5.aux
pdflatex -synctex=1 -interaction=nonstopmode dissertation.tex