
#import time

# Performance check
#t0 = time.time()

from Functions import allImports, file2dict, dict4all, getMatches, dictCutOff, sumDict, helpInfoMolec, infoMolec, matchAndCut     
from os import listdir
from collections import Counter as Counter



allThemFiles = listdir('ExampleFiles')
allThemDicts = []
allThemDicts = dict4all(allThemFiles)
allReact = allThemDicts[0]

# Performance check
#t2 = time.time()
#print "Execution time: {0}".format(t0-t2)



from Functions import allImports, file2dict, dict4all, getMatches, dictCutOff, sumDict, helpInfoMolec, infoMolec

humanCuts = [40.,20.]
bacteriaCuts = [600., 20.]

matchAndCut(allReact, humanCuts, bacteriaCuts)

