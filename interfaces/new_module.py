import pandas 


pdbd = pandas.DataFrame({
    'name':['Nikita', 'ivan'],
    'surname':['Kolesnikov','ledyaev'],
    'phone':['3456789', '3456789'],
    'nickname':['nik24','ivan']
})


print(pdbd.head())

pdbd.to_csv('phonebook.csv', sep=';')

#посмотреть метод place