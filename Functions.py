
# coding: utf-8

# In[8]:

def allImports():
    from collections import Counter
    from os import listdir
    from copy import deepcopy as dcopy
    print 'All Packages Imported'


# In[9]:

#############################################
#       Read File and get dictionary        #
#############################################
#
#  *INPUT:  Name of file
#
#  *OUTPUT: 2-D list of dictionaries
#           0th => Reactants : Occurrencies
#           1st => Products  : Occurrencies
#
#
############################################
#        Read File and get dictionary      #
############################################

def file2dict(nameString) :

    from collections import Counter
    
    thaFile = open(nameString, 'rU')
    log = open("log.out",'w')
    allLines = thaFile.readlines()
    noLines = len(allLines)
    isReact = False
    prodOrReact = False
    isProd = False
    isGood = False
    reactants = []
    compound = ""
    products = []
    i = 0
    
    for line in allLines: # Read all file

        if not prodOrReact : # line is not part of list of prods/react
            
            if line.find('<listOfProducts>') > 0:
                
                prodOrReact = True
                log.write("in")
                isProd = True
                
            if line.find('<listOfReactants>') > 0:
                
                prodOrReact = True
                log.write("in")
                isReact = True

        # Look for Compounds if its time for that
        if prodOrReact : # inside list of prod/react
            
            # Check is list has ended here
            if line.find('</listOfReactants>') > 0:
                
                prodOrReact = False
                log.write("out"+'\n')
                isReact = False
                
            elif line.find('</listOfProducts>') > 0:
                
                prodOrReact = False
                log.write("out"+'\n')
                isProd = False
                
            else : # we are in list
                
                isGood = line.find('speciesReference species=')
                
                if isGood > -1:
                    
                    endProd = line.find('"',isGood+27)
                    compound = line[isGood+26:endProd]
                    
                    if isReact :
                        reactants.append(compound)#Add to reactantsList
                    elif isProd :
                        products.append(compound)#Add to products:ist               
    
    # Convert list into dictionary of occurences
    dictReactants = Counter(reactants)
    dictProducts = Counter(products)
    compounds = [dictReactants, dictProducts]
    thaFile.close()
    return compounds


# In[19]:

############################################
#   Get all Dictionaries from Filenames    #
############################################
#
#  *INPUT: 1-D list of filenames
#
#  *OUTPUT: 2-D list of dictionaries
#           0th => Reactants
#           1st => Products
#  Info: Dictionaries are 2-D with 
#        Key == Name of Bacteria
#        Value == Dict of comp : #appear
#
#
############################################
#   Get all Dictionaries from Filenames    #
############################################

def dict4all(allFiles) :
    
    allProds = {}
    allReact = {}
    allInDict = []
    
    for currentFile in allFiles :
        
        absPath = 'ExampleFiles/'+currentFile
        simpDict = file2dict(absPath)
        allReact[currentFile[:-4]] = simpDict[0]
        allProds[currentFile[:-4]] = simpDict[1]
        
        
    allInDict.append(allReact)
    allInDict.append(allProds)
    return allInDict


# In[20]:

############################################
#       Get Matches Human-Bateria          #
############################################
#
#  *INPUT: Dictionary of dictionaries
#          Key == Name of Bacteria
#          Value == Name comp : #appear
#
#  *OUTPUT: Dictionary of Compounds in 
#           humansANDbacteria 
#           Compound name: # bacterias
#
#  Info: Humans is an entry in dictionary of
#        the input list (INPUT['humans'])
#
############################################
#       Get Matches Human-Bateria          #
############################################

def getMatches(everyCompDict) :
    
    from collections import Counter
    matches = []
    humans = everyCompDict['humans']
    del everyCompDict['humans']
    
    for compound in humans :
        for bacteria in everyCompDict : 
            if compound in everyCompDict[bacteria] : # Compounds appears in bacteria and humans
                matches.append(compound)
                
    everyCompDict['humans'] = humans
    dictMatches = Counter(matches)
    return dictMatches


# In[21]:

############################################
#       Apply cuts on Dictionaries         #
############################################
#
#  *INPUT: -Dictionary of type:
#            dict[Key] == Value   
#          - Maximum Value allowed
#          - Minimum Value allowed
#
#  *OUTPUT: Trimmed-down dictionary
#
#  Info: -It is required that: 
#         value == [Number]
#        -Remaining entries satisfy:
#         value < maxVal
#         value > minVal
#
#
############################################
#       Apply cuts on Dictionaries         #
############################################

def dictCutOff(thisDict, maxVal, minVal) :#
    
    dictTrim = copy.deepcopy(thisDict)
    
    if maxVal < minVal :
        temp = copy.deepcopy(maxVal)
        maxVal = minVal
        minVal = temp
    elif maxVal == minVal :
        print "Error: Invalid input limits [They are the same you moron]"
        return
    for compound in thisDict : 
        if any ([dictTrim[compound] >= maxVal, dictTrim[compound] <= minVal]) :
            del dictTrim[compound]
    
    return dictTrim


# In[22]:

############################################
#        Sum All Dictionary Entries        #
############################################
#
#  *INPUT: -Dictionary (key : [number])
#
#  *OUTPUT: Sum of values [number]
#
#
############################################
#        Sum All Dictionary Entries        #
############################################

def sumDict(dict2Sum) :
    
    total = 0
    for molec in dict2Sum:
        total += dict2Sum[molec]
    return total*1.0


# In[32]:

############################################
#        Help-printing for infoMolec       #
############################################
#
#  *INPUT: -None
#
#  *OUTPUT: -None
#
#  Info: -Prints information about usage and
#         inner workings of infoMolec
#        -Information is sorted in 3 topics:
#           *input
#           *output
#           *inner_workings
#
#
############################################
#        Help-printing for infoMolec       #
############################################
def helpInfoMolec():
    
    print "############################################"
    print "#        Info-Getter for molecules         #"
    print "#                                          #"
    print "#  HELP Section: Information about inner   #"
    print "# working and usage of infoMolec function  #"
    print "############################################"
    print "#"
    print "#-------------------------------------------"
    print "#          BASIC INFORMATION"
    print "#-------------------------------------------"
    print "#"
    print "#  *INPUT: -Name of molecule"
    print "#          -Dictionary of dictionaries "
    print "#           for reactants OR products"
    print "#"
    print "#  *OUTPUT: Dictionary of molecule info"
    print "#           such as:"
    print "#           _list of bacterias in which "
    print "#             it appears"
    print "#             appearances : list[]"
    print "#           _appearances in humans"
    print "#            humans : [#, %]"
    print "#           _appearances in each bacteria"
    print "#            bacteriaName : [#, %]"
    print "#           _total appearances in bacteria"
    print "#            bacterias : #"
    print "#"
    print "#  Extra: Input list of dict of dict in the "
    print "#        form of list[0] or list[1] from"
    print "#        OUTPUT in dict4all function"
    print "#"
    print "#"
    print "############################################"
    print "#        Info-Getter for molecules         #"
    print "############################################"
    print ""
    print ""
    print " For extra information please select the topic by typing one of the following keywords: "
    print " Keywords:  input \t output \t inner_workings"
    topic = raw_input('Select topic: ')
    topicSelected = False
    while not topicSelected :
        if topic == 'input' :
            topicSelected = True
            print topic
        elif topic == 'output':
            topicSelected = True
            print topic
        elif topic == 'inner_workings':
            topicSelected = True
            print topic
        else :
            print "Topic could not be selected, please try again:"
            topic = raw_input('Select topic: ')



# In[35]:

############################################
#        Info-Getter for molecules         #
############################################
#
#  *INPUT: -Name of molecule
#          -Dictionary of dictionaries 
#           for reactants OR products
#
#  *OUTPUT: Dictionary of molecule info
#           such as:
#           _list of bacterias in which 
#             it appears
#             appearances : list[]
#           _appearances in humans
#            humans : [#, %]
#           _appearances in each bacteria
#            bacteriaName : [#, %]
#           _total appearances in bacteria
#            bacterias : #
#
#  Info: Input list of dict of dict in the 
#        form of list[0] or list[1] from
#        OUTPUT in dict4all function
#
#
############################################
#        Info-Getter for molecules         #
############################################

def infoMolec(molecule = 0, dictioData = 0):
    if all([dictioData != 0, molecule != 0]):

        manyStats = {}
        listOfBact = []
        humanStats = []
        bactStats = {}
        tempBactDict = {}
        allBactStats = {}  
        nameLen = 0

        '''
            List of Bacterias 
        '''
        for bacteria in dictioData :
            if molecule in dictioData[bacteria] :
                listOfBact.append(bacteria)
                if nameLen < len(bacteria) :
                    nameLen = len(bacteria)

        manyStats['allBacteria'] = listOfBact

        '''
         Appearances in humans
        '''
        humanStats.append(dictioData['humans'][molecule])
        sumHumans = sumDict(dictioData['humans'])

        humanStats.append(1.0 * humanStats[0]/sumHumans)

        manyStats['humans'] = humanStats

        print "Molecule "+molecule+" appears {0} times in human reaction".format(humanStats[0])
        print "Represents {0:3f}% of total in humans".format(humanStats[1]*100)
        print "=================================="

        '''
            Total Appearances in all Bacteria
        '''

        for bacteria in listOfBact :

                tempBactDict[bacteria] = dictioData[bacteria][molecule]

        totalAppear = sumDict(tempBactDict)

        manyStats['appearancesBacteria'] = totalAppear

        '''
            Appearances in bacterias 
        '''

        for bacteria in tempBactDict :
            bactStats[bacteria] = [tempBactDict[bacteria], tempBactDict[bacteria]/totalAppear]


        manyStats['bacterias'] = bactStats
        #print nameLen

        print "Molecule ' "+molecule+" ' appears in: "
        print "{0:59} \t Appearances "+'\t'+"Percetange ".format('Bacteria')
        for bacteria in bactStats :
            print "{0:59} : {1:3} times => {2:3f}% of total appearences".format(bacteria, bactStats[bacteria][0], bactStats[bacteria][1]*100)

        print "=================================="


        '''
            Work done, lay back and enjoy results
        '''
        return manyStats
    
    '''
        On-screen help / manual
    '''
    if any([molecule == 0, dictioData == 0]):
        helpInfoMolec()
        return