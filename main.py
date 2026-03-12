from custom_classes import MediaItem
from custom_classes import Book
from custom_classes import DVD
from custom_classes import LibraryCollection

library_collection = LibraryCollection()
book = Book("1984","George Orwell","250")
movie = DVD("Inception", "Christopher Nolan", "2.5 hours")
book1 = Book("Nutuk", "Mustafa Kemal Atatürk", "300")
book2 = Book("Harry Potter", "J.K.Rowling", "400")
book3 = Book("Küçük Prens", "Antoine de Saint-Exupery", "150")

#print(book)
#print(movie)

#book.checkout()
#print(book)

#print(movie.checkout())
#print(movie)

library_collection.add_item(book1)
library_collection.add_item(book2)
library_collection.add_item(book3)

library_collection.list_available()