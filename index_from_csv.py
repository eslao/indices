import csv

#initialize a list to store the records in
masterArray = []


#read the existing csv
with open('death.csv', 'r') as csvfile:
    #sniff to find the format
    fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    #create a CSV reader
    myReader = csv.reader(csvfile, dialect=fileDialect)
    #read each row
    for row in myReader:
        masterArray += [{'ingredient':row[0], 'recipe':row[1], 'page':row[2]}]

#create alphabetical ingredient list

ingredientArray = []

for item in masterArray[1:]:
    if item['ingredient'] not in ingredientArray:
        ingredientArray += [item['ingredient']]

ingredientArray.sort()        
        
#create index

formattedIngredientArray = []

for ingredient in ingredientArray:
    drinks = []
    for item in masterArray:
        if ingredient == item['ingredient']:
            drinks += [{'recipe':item['recipe'], 'page':item['page']}]
    #print ingredient
    #print drinks
    formattedIngredientArray += [{'ingredient':ingredient, 'drinks':drinks}]
    #print index

for indexEntry in formattedIngredientArray:
    print indexEntry['ingredient'] + ': '
    for drink in indexEntry['drinks']:
        print '\t' + drink['recipe'] + ', p.' + drink['page']
    print '\n'
    
#to do: write index to text file
