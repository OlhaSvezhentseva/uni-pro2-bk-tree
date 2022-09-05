
# BK-tree

## Description

The project deals with approximate string matching using BK-tree data structure. 
Another application of BK trees is spell checking.
BK-tree can be either built on the basis of Levenshtein distance (Edit distance) or Jaccard distance, 
in both cases the program is case-sensitive.
 
Edit distance counts the minimum number of operations required to transform one string into the other. 
In these case each of the operations 
(deletion, insertion, replacement) costs 1 unit.
After the tree is built,
user can type a word and the maximum distance a string can be from this word 
and still be returned. 
 Then the program will change into an interactive mode.

 Jaccard distance measures dissimilarity between sample sets.
 In case of string matching Jaccard distance is based on letter bigrams that strings have in common.
The distance is obtained by subtracting Jaccard coefficient
 (intersection of two strings divided through sum of their cardinalities minus their intersection) from 1. I decided to use Jaccard distance and not Jaccard coefficient 
 to make trees based on different metrics and search in them more coherent.
 Then the described tree follows the same logic as a tree built based on Edit distance. 
 The only difference ist that Jaccard distance can range from 0 to 1 because 
 it's a normalized value.
Strings are viewed as sets, so letter bigrams of the word "banane" would be {"ba", "an", "na", "ne"}, 
where bigram "an" occurs only once. 


## Structure
File `derewo_words.py` is responsible for filtering words and saving them in a txt file.

 File `small_derewo.txt` contains words used for demo.
 
 File `main.py` calls the program.
 
 Folder `bk_program` contains files that constitute main logic of the program: 
 construction and visualisation of a tree, conducting  searches in the tree.

Its subfolder `metrics` contains files responsible for calculating distance between words.

Folder `tests` contains test files that check calculation of distance.


# Requirements
`python3.7`

`graphviz` (see https://graphviz.readthedocs.io/en/stable/manual.html)

The only dependency is a working installation of Graphviz (also see 
https://graphviz.readthedocs.io/en/stable/manual.html )

`nltk` (see https://www.nltk.org/)

`pytest` (see https://pypi.org/project/pytest/)

  
# Demo
To run demo version of the program use  `small_derewo.txt`.
 It contains 10 already cleaned words. 
Call the program from the root folder (so that bk_program is a subfolder then)
    
   `python -m main --file small_derewo.txt`

The first parameter is the file with the words, the other parameter defines type of metrics 
that must be used to build the tree and make searches in it. It's a default parameter and is set to
 `edit` (to use Edit distance for calculations)
 
 You can make it explicit: `python -m main --file small_derewo.txt --metric edit`

To use Jaccard distance:  `python -m main --file small_derewo.txt --metric jaccard`
 
 You will see the visualisation of a tree (as the tree was built on fewer then 50 words), 
 status information such as height of the tree and number of nodes in it.
  Then the program will change into an interactive mode. 
The program will always wait for input from user
 after the result for the previous query  (if there was one) was already returned. 
 Empty input stops the program.
 Example of input:
 
 
   `sein 2`
 
There must be a word followed by a number, indicating the biggest distance allowed. 
It may be an integer or a float.

# Usage
1. Download DeReWo list of words from 
https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/

    The list's name is "derewo-v-ww-bll-250000g-2011-12-31-0.1"  and it contains 250.000 words.

2. In console call derewo_words.py from the root folder.
The program will extract filtered words from the downloaded text file 
that must pe provided as a parameter and save them in a new txt file named  `filtered_words`.
 
    `python derewo_words.py --file derewo-v-ww-bll-250000g-2011-12-31-0.1.txt`

3. Text file with the source text for visualisation will be saved, 
visualisation itself will not be generated, as the number of words exceeds 50.
4. Running program is the same as in demo:

    `python -m main --file filtered_words`

    `python -m main --file filtered_words  --metric jaccard`


## Tests
Test lie in the root folder.

`python -m unittest discover tests`

## Contact
Olha Svezhentseva <olha.svezhentseva@uni-potsdam.de>

