
# BK-tree

## Description

The project deals with string matching using BK-tree. 
BK-tree can be either build on the basis of Levenshtein distance (Edit distance) or Jaccard distance.

Edit distance counts the minimum number of operations required to transform one string into the other. In these case each of the operations 
(deletion, insertion, replacement) cost 1 unit.
After the tree is built,
user can type a word and the maximum distance a string can be from this word 
and still be returned. 
 Then the program will change into an interactive mode.

 Jaccard distance measures dissimilarity between sample sets.
 In case of string matching Jaccard distance is based on letter bigrams that strings have in common.
The distance is obtained by subtracting Jaccard coefficient
 (intersection of two strings divided through sum of their cardinalities) from 1.  
 I decided to use Jaccard distance  and not Jaccard coefficient 
 to make trees based on different metrics and search in them more coherent.
 Then the described tree follows the same logic as a tree built based on Edit distance. 
 Jaccard distance can range from 0 to 1 because 
 it's a normalized value and is in this sense logically different from Edit distance.
Strings are viewed as sets, so letter bigrams of the word "banane" would be {"ba", "an", "na", "ne"}, 
where bigram "an" occurs only once. 


## Structure
File `derewo_words` is responsible for filtering words and saving them in a txt file.

 File `small_derewo.txt` contains words used for demo.
 
 Folder `bk_program` contains files that constitute main logic of the program: 
 construction and visualisation of a tree, interactive mode for conducting  searches in the tree.

 Folder `metrics` contains files responsible for calculating distance between words.
 
  Subfolder of  `metrics` folder `tests` contains test files that check calculation of distance.


# Requirements
`python3.7`

`graphviz` (see https://graphviz.readthedocs.io/en/stable/manual.html)

  
# Demo
To run demo version of the program use  `small_derewo.txt`.
 It contains 10 already cleaned words. 
    
    Call: `python -m bk_program.program --file small_derewo.txt`

The first parameter is the file with the words, the other parameter defines type of metrics 
that must be used to build the tree and make searches in it. It's a default parameter and is set to
 `edit` (to use Edit distance for calcualtions)
 
 You can make it explicit: `python -m bk_program.program --file small_derewo.txt --metric edit`

To use Jaccard distance:  `python -m bk_program.program --file small_derewo.txt --metric jaccard`
 
 You will see the visualisation of a tree and 
 status information such as depth of the tree and number of nodes in it.
  Then the program will change into an interactive mode. 
The program will always wait for input from user
 after the result for the previous query  (if there was one) was already returned. 
 Empty input stops the program.
 
 
    Call: `sein 2`
 
There must be a word followed by a number, indicating the biggest distance allowed.

# Usage
1. Download DeReWo list of words from 
https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
The list's name is derewo-v-ww-bll-250000g-2011-12-31-0.1  and it contains 250.000 words.

2. In console call derewo_words.py.
The program will extract filtered words from the downloaded text file 
that must pe provided as a parameter and save them in a new txt file named  `filtered_words`.
 
        Call: `python derewo_words.py --file derewo-v-ww-bll-250000g-2011-12-31-0.1.txt`

3. If no visualisation is desired, open  bk_program.program.py and comment code in the "Visualisation" part.
4. Running programm is the same as in demo:

    `python -m bk_program.program --file filtered_words`

    `python -m bk_program.program --file filtered_words --metric jaccard `

5. Interactive mode is the same



## Tests
Test lie in `metrics/tests`

Call:  `python -m unittest discover metrics.tests`

## Contact
Olha Svezhentseva <olha.svezhentseva@uni-potsdam.de>

