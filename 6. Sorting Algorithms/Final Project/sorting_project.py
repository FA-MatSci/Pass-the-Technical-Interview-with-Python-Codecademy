import utils    #to import other python scripts
import sorts

bookshelf = utils.load_books('books_small.csv')

long_bookshelf = utils.load_books('books_large.csv')
#print(bookshelf)

bookshelf_v1 = bookshelf.copy()   #if you have without copy(), then everything that you would change in bookshelf_v1 would also be changed in bookshelf itself

bookshelf_v2 = bookshelf.copy()



#for book in bookshelf:
#  print(book['title_lower'])

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_a['author_lower'])

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
#for i in sort_1:
#  print(i['title_lower'])

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
#for i2 in sort_2:
#  print(i2['author'])

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for i3 in bookshelf_v2:
  print(i3['author_lower'])

#sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

