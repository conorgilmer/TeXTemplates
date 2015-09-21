# Make file to compile LaTex using pdflatex\
change the project name to the latex filename \
if you use a bibtex file uncomment the bibtex line
PROJECT=balsheet
TEX=pdflatex
BIBTEX=bibtex
BUILDTEX=$(TEX) $(PROJECT).tex

all:
	$(BUILDTEX)
#	$(BIBTEX) $(PROJECT)
	$(BUILDTEX)
	$(BUILDTEX)
clean-all:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~
clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~
