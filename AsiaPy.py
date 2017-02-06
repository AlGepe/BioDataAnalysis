

# Performance check
#import time
#t0 = time.time()

from Functions import allImports, file2dict, dict4all, getMatches, dictCutOff, sumDict, helpInfoMolec, infoMolec
from os import listdir
from copy import deepcopy as dcopy
from collections import Counter as Counter



#allImports()
allThemFiles = listdir('ExampleFiles')
allThemDicts = []
allThemDicts = dict4all(allThemFiles)
allReact = allThemDicts[0]
#infoMolec('M_hmgcoa_c', allReact)
infoMolec('M_hmgcoa_c', allReact)

# Performance check
#t2 = time.time()
#print "Execution time: {0}".format(t1-t2)

