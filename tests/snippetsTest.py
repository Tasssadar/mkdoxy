import argparse
import sys
import os
from mkdoxy.doxygen import Doxygen
from mkdoxy.generatorBase import GeneratorBase
from mkdoxy.generatorAuto import GeneratorAuto
from mkdoxy.generatorSnippets import GeneratorSnippets
from mkdoxy.xml_parser import XmlParser
from mkdoxy.cache import Cache
from mkdoxy.constants import Kind
from mkdoxy.node import Node
from mkdoxy.finder import Finder
from mkdoxy.doxyrun import DoxygenRun
from pprint import *

if __name__ == "__main__":
	doxygenSource = "files/src-stm32"
	# doxygenSource = "files/src"
	tempDoxyDir="files/doxy"
	siteDir = "files/doxy"
	apiPath="api"
	target = "mkdocs"
	useDirectoryUrls=True
	hints = True
	ignoreErrors = False
	summary = None
	link_prefix = ""

	# Debug options
	debug = True
	debugFull = False
	fullDoc = True

	doxygenRun = DoxygenRun(doxygenSource, siteDir, {})
	doxygenRun.run()

	options = {
		'target': target,
		'link_prefix': link_prefix
	}

	cache = Cache()
	parser = XmlParser(cache=cache, debug=debug)
	doxygen = Doxygen(siteDir, parser, cache, options=options, debug=debug)

	if debugFull:
		doxygen.print()

	generatorBase = GeneratorBase(ignore_errors=ignoreErrors, options=options)
	
	generatorAuto = GeneratorAuto(generatorBase=generatorBase,
	                              tempDoxyDir=tempDoxyDir,
	                              siteDir=siteDir,
	                              apiPath=apiPath,
	                              useDirectoryUrls=useDirectoryUrls,
	                              fullDocFiles=[],
	                              debug=debug)
	if fullDoc:
		generatorAuto.fullDoc(doxygen)

	# find = Finder(doxygen, debug)
	# fc = find.doxyClass("example::Bird", "Bird (const Bird & other)= delete")

	generatorSnippets = GeneratorSnippets(markdown="", generatorBase=generatorBase, doxygen=doxygen, debug=debug)
	# func = generatorSnippets.doxyFunction("", {"name":"getRandomNumber()"})

	# func = generatorSnippets.doxyCode("", {"file":"shape.cppa"})
	func = generatorSnippets.doxyClassMethod("", {"name":"asd", "method":"as"})

	pp(func)
