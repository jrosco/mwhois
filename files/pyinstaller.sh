#!/bin/bash

/usr/local/bin/pyinstaller 	--specpath=./ \
			 	--workpath=./build/ \
				--distpath=./dist/ \
				./src/mwhois.py
