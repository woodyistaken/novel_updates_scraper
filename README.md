## Usage
Request a particular list of courses and retrieve all of their data.

Example:
```python
from Search import Search
from Book import Book
from genre_constants import *

search=Search(included_genres=[GENRES["GENRE_COMEDY"]])
titles=search.get_titles(5)
Book.make_book(titles[0])
```