# Make all html files from .ht

# $Id: Makefile,v 1.5 2007/03/07 22:32:06 colin Exp $

all: install

GENERATOR := ShsnyGenerator

%.html: %.ht $(GENERATOR).py links.h pique/links.h
	$(HT2HTML) $<

FTP_USER := u36370209
FTP_PASS := Yfp6pwKm
FTP_HOST := shsny.org
FTP_DIR  := /

INSTALL_DIRECTORY := /Library/WebServer/Documents

$(INSTALL_DIRECTORY)/%: %
	install -p -m 0644 $< $@

HT2HTML := python ./ht2html-2.0/ht2html.py -r '' -s $(GENERATOR)

HT_FILES := $(shell find . -name '*.ht' | sed 's|\./||g')
HTML_FILES := $(HT_FILES:.ht=.html)
DOC_FILES := $(shell find . -name '*.doc' | sed 's|\./||g')

WANTED_FILES := $(HTML_FILES) $(DOC_FILES)
INSTALLED_FILES := $(patsubst %,$(INSTALL_DIRECTORY)/%,$(WANTED_FILES))

install: $(INSTALLED_FILES)

build: $(WANTED_FILES)

dist: $(INSTALLED_FILES)
	./ftpsync -n -p $(INSTALL_DIRECTORY) ftp://$(FTP_USER):$(FTP_PASS)@$(FTP_HOST)/$(FTP_DIR)

show_ht:
	@echo $(HT_FILES)

show_html:
	@echo $(HTML_FILES)

show_wanted:
	@echo $(WANTED_FILES)

show_installed:
	@echo $(INSTALLED_FILES)

# end Makefile
