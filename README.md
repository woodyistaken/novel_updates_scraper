## Usage
Get data from novel updates website 

Example:
```python
from novel_updates_scraper.Search import Search
from novel_updates_scraper.Book import Book
from novel_updates_scraper.genre_constants import *

search=Search(included_genres=[GENRES["GENRE_COMEDY"]])
titles=search.get_titles(5)
Book.make_book(titles[0])
```
## Documentation
Documentation available at https://novel-updates-scraper-docs.vercel.app/
