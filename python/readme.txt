Stappen om een index te bouwen

1. run test programma in java
workspaces/auk/aggregator/src/main/java/nl/cosmos/auk/aggregator/Test.java
- dit programma stopt alle artikelen
  van drie kranten (nrc, volkskrant en trouw) 
  in database
  
2. bouw de woordlijst en index op
$ cd workspaces/auk/python
$ python vktrouw_generatewordindex.py 1000

3.bouw de harde rubrieken combinatie op
$ cd workspaces/auk/python
$ python vktrouw_generatekrantweight.py


4. bouw de zachte rubrieken combinatie op
$ cd workspaces/auk/python
$ python vktrouw_generatecalculatedweight.py
$ python vktrouw_generatecloudweight.py



  