TeX	= latex
DIRLIST := $(shell ls)
DIRLIST := $(filter-out %\# , $(DIRLIST))
DIRLIST := $(filter-out template.tex , $(DIRLIST))
SOURCES := $(filter %.tex, $(DIRLIST))
ifneq ($(strip $(SOURCES)),)
  OBJECTS := $(addsuffix .ps , $(basename $(SOURCES))) 
endif

.SUFFIXES:.tex.ps

%.ps:%.tex touch
	$(TeX) $<
	$(TeX) $<
	dvips $*.dvi -o -Ppdf -t landscape
	ps2pdf -dMaxSubsetPct=100 -dCompatibilityLevel=1.2 \
             -dSubsetFonts=true -dEmbedAllFonts=true \
             -dAutoFilterColorImages=false \
             -dAutoFilterGrayImages=false \
             -dColorImageFilter=/FlateEncode \
             -dGrayImageFilter=/FlateEncode \
             -dModoImageFilter=/FlateEncode \
	$*.ps
	rm -f *.aux *.dvi *.log *.blg *.bbl 

all: talk.ps

touch:

clean:
	rm -f *.aux *.dvi *.log *.blg *.bbl 

realclean: 
	rm -f *.aux *.dvi *.log *.ps *~ 


