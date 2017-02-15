# BioDataAnalysis - All Functions

Simple analysis software for BioInformatics project that takes \*.xml files containing information about the reactions inside given bacteria and is able to provide the user with comprehensible information about the reactants and products in bacteria and humans.

## **file2dict**

Function that looks for compounds (reactants and products) in a \*.xml file with a given format and returns lists (python dictionaries) containing name and number of appearances in chemicals reactions within the file. The function separates products and reactants

### Input
- Filename _(string)_: Name of the file from which to take the molecules present in reactions.

### Output
- List of 2 dictionaries: 0th dictionary is the list of pairs {reactant names : # appearances in file}
													1st dictionary is the list of paits {product names  : # appearances in file}



## dict4all

This function takes a list of strings (names of files) as input and returns a list of two (reactants and products) dictionaries of dictionaries. Each dictionary in the list has as key the name of the bacteria to which the file refers (which is the name of the file minus the extension) and as value a dictionary of the compounds present and number of ocurrencies of such compound in the same format as output from _file1string_. This function calls _file2string_ internally after correcting filename to the correct path.

### Input
- list of filenames (as _string)_: Name of the file from which to take the molecules present in reactions.

### Output
- List of 2 dictionaries (2-D): 0th dictionary is the list of pairs {bacteria names : {reactant names : # appearances in file}
																1st dictionary is the list of paits {bacteria names : {product names  : # appearances in file}



## getMatches

Given a 2-D dictionary the function analyses the matching elements(molecules) of the dictionary under key _humans_ and all the rest returning a dictionary of the matching molecules and number of matches

### Input
- Dictionary of dictionaries: should be in the form =>  {bacteria names : {product names  : # appearances in file}. Input is required to have numbers as deepest dictionary value

### Output
- Dictionary of Matches: Dictionary containing the matching molecules between humans file and rest of molecules in the form: {molecule name : # matches}



## dictCutOff

Reduces the input dictionary to one who only contains keys which values are in the threshold interval set by user.

### Input
- Dictionary: In the form of {key : numericalValue}
- Maximum Value allowed: all key whose value is above this value will be deleted
- Minimum Value allowed: all key whose value is below this value will be deleted

### Output
- Trimmed Dictionary: Dictionary containing only those elements whose values lay in the given interval (i.e.: MaxValue > value > MinValue).



## sumDict

Calculates the sum off all values in a dictionary 


### Input

- Dictionary with numerical values

### Output

- Sum of all values in dictionary as a double type



## infoMolec

Functions that gives useful information of a molecule in a given dicitonary.  

### Input
- Molecule Name (_string_): Name of the molecule as written in the files or dictionaries
- Dictionary of dictionaries: Data in a 2-D dictionary form similar to any of the output items from *_dict4all_* function

### Output
- Dictionary of information:
	- Keyword: _allBacteria_ || Value: List of bacteria names in which the molecule appears.
	- Keyword: _humans_ || Value : [number of appearances of the molecule in humans, % of the total number of reactions in humans]
	- Keyword: _appearancesBacteria_ || Value : Number of total appearances in all Bacterias
	- Keyword: _bacterias_ || Value : dictionary {name of bacteria : [number of appareances of molecule in bacteria, % of total appareances of the molecule in all bacterias]}



## helpInfoMolec

Prints on screen interactive help for function _infoMolec_

### Input
- NONE

### Output
- NONE



## matchAndCut

Function takes a dictionary of all reactants/products in bateria+human and returns a dictionary with the matching molecules that appear in humans and baterias at the same time and also meet the criteria given by the intervals provided by the user. The intervals specify the allowed number of appearances in human reactions and the number of bacterias in which they also appear.

### Input
- Dictionary of dictionaries: Data in a 2-D dictionary form similar to any of the output items from *_dict4all_* function
- Interval limits for number appearances in human reactions: list = [maxValue, minValue]
- Interval limits for number of bacterias in which the molecule appears: list = [maxValue, minValue]

### Output
- Dictionary of molecules present in humans and bacteria at the same time and matching the given criteria.  It is presented in the form of {molecule : [# appearances in humans, # bacterias in which it is present]}

## REQUIRED FILES

All the required files are contained in the archive "ExampleFiles.zip". It should be unzipped and all the files in it should be placed in a folder named: ExampleFiles (Otherwise modification to the source code must be done for the program to run correctly)
