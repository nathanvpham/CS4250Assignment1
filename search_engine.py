#-------------------------------------------------------------------------
# AUTHOR: Nathan Pham
# FILENAME: search_engine.py
# SPECIFICATION: Practice calculating tf-idf, document score, and precision/recall on a .csv file
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1hr and 20min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math

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
print("Stemming:")
print(documents)
print()

#Identify the index terms.
#--> add your Python code here
terms = []
for doc in documents:
    splitDoc = doc.split()
    for word in splitDoc:
        if word not in terms:
            terms.append(word)
print("Index Terms")
print(terms)
print()

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []
tfMatrix = []
dfMatrix = []
for doc in documents:
    tfRow = []
    for term in terms:
        tf = doc.count(term)/len(doc.split())
        tfRow.append(tf)
    tfMatrix.append(tfRow)

for term in terms:
    df = 0
    for doc in documents:
        if term in doc:
            df = df + 1
    dfMatrix.append(df)

for tfRow in tfMatrix:
    tfidfRow = []
    for x in range(len(tfRow)):
        tfidf = (tfRow[x]) * (math.log(3.0/dfMatrix[x], 10))
        tfidfRow.append(tfidf)
    docMatrix.append(tfidfRow)
print("tf-idf Matrix:")
print(docMatrix)
print()



#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []
queryMatrix = []
for tfRow in tfMatrix:
    queryRow = []
    for tf in tfRow:
        if tf > 0.0:
            queryRow.append(1.0)
        else:
            queryRow.append(0.0)
    queryMatrix.append(queryRow)

for x in range(len(docMatrix)):
    tfidfRow = docMatrix[x]
    queryRow = queryMatrix[x]
    docScore = 0.0
    for y in range(len(tfidfRow)):
        docScore = docScore + (tfidfRow[y] * queryRow[y])
    docScores.append(docScore)
print("Document Scores:")
print(docScores)
print()


#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here
docRelevance = []
for docScore in docScores:
    if docScore >= 0.1:
        docRelevance.append(' R')
    else:
        docRelevance.append(' I')

truePositive = 0.0
falsePositive = 0.0
for x in range(len(docRelevance)):
    if docRelevance[x] == labels[x]:
        truePositive = truePositive + 1.0
    else:
        falsePositive = falsePositive + 1.0
print("Number of True Positives:", truePositive)
print("Number of False Positives:", falsePositive)
# we retrieved all documents therefore true neg and false neg are 0
print("Number of True Negatives: 0.0")
print("Number of False Negatives: 0.0")
print()

precision = truePositive/(truePositive+falsePositive)
print("Precision: " + f"{precision:.2%}")
recall =truePositive/(truePositive+0.0) # we added true negative(0.0) to denominator
print("Recall: " + f"{recall:.2%}")
