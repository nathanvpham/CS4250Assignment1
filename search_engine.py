#-------------------------------------------------------------------------
# AUTHOR: Nathan Pham
# FILENAME: search_engine.py
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append(row[0])
            labels.append(row[1])

#Conduct stopword removal.
#--> add your Python code here
stopWords = ['I', 'and', 'She', 'They', 'her', 'their']
temp =[]
for doc in documents:
    for word in stopWords:
        doc = doc.replace(word, '')
    temp.append(doc)
documents = temp


#Conduct stemming.
#--> add your Python code here
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}

tempDoc = []
for doc in documents:
    splitDoc = doc.split()
    tempWord = []
    for word in splitDoc:
        if word in stemming:
            word = stemming[word]
        tempWord.append(word)
    tempDoc.append(' '.join(tempWord))
documents = tempDoc


#Identify the index terms.
#--> add your Python code here
terms = []
for doc in documents:
    splitDoc = doc.split()
    for word in splitDoc:
        if word not in terms:
            terms.append(word)
print(terms)

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here