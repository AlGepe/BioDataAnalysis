
# coding: utf-8

# In[2]:

#import time

# Performance check
#t0 = time.time()

from Functions import allImports, file2dict, dict4all, getMatches, dictCutOff, sumDict, helpInfoMolec, infoMolec, matchAndCut     
from os import listdir
#import copy as copy #import deepcopy
from collections import Counter as Counter



#allImports()
allThemFiles = listdir('ExampleFiles')
allThemDicts = []
allThemDicts = dict4all(allThemFiles)
allReact = allThemDicts[0]
#infoMolec('M_hmgcoa_c', allReact)
#infoMolec('M_glygn4_e', allReact)

# Performance check
#t2 = time.time()
#print "Execution time: {0}".format(t0-t2)


# In[3]:

#import copy as copy #as copia #import deepcopy as deepcopy
#from copy import deepcopy as deepcopy#as dcopia
from Functions import allImports, file2dict, dict4all, getMatches, dictCutOff, sumDict, helpInfoMolec, infoMolec

humanCuts = [40.,20.]
bacteriaCuts = [600., 20.]

matchAndCut(allReact, humanCuts, bacteriaCuts)

#trimDictionary = dictCutOff(allReact['humans'], 40, 20)

#allReact['humans'] = trimDictionary

#match20_40 = getMatches(allReact)

#print "{0:20}: {1:5} {2:5}".format("Molecule", 'Humans', 'Bacterias')

#for molecule in match20_40 :
    
#    print "{0:20}: {1:5} {2:5}".format(molecule, trimDictionary[molecule], match20_40[molecule])


# In[ ]:



