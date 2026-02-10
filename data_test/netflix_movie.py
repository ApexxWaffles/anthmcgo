import pandas

films = pandas.read_csv('data_test/NetflixOriginals.csv', encoding='cp1252')    
print(films.columns)

films.rename(columns={'Genre': 'Genre', 'IMDB Score': 'IMDB_Rating', 'Title': 'Title', 'Premiere': 'Premiere', 'Runtime': 'Runtime', 'Language': 'Language'}, inplace=True)

print(films.Genre.count())

def genre_count(genre):
    return films[films.Genre == genre].Genre.count()
print(genre_count("Documentary"))
print(genre_count("Comedy"))
print(genre_count("Drama"))
print(genre_count("Action & Adventure"))
print(genre_count("Horror"))
print(genre_count("Kids' TV"))


def imbd_rating(genre):
    return films[films.Genre == genre].IMDB_Rating.mean()
print(imbd_rating("Documentary"))
print(imbd_rating("Comedy"))
print(imbd_rating("Drama"))
print(imbd_rating("Action & Adventure"))
print(imbd_rating("Horror"))
print(imbd_rating("Kids' TV"))  

