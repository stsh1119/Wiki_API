# Wiki_API

## Requirements
##### Wiki title has 2 fields:
 1. title
 2. text
 3. any other - additionally

##### After editing, wiki page gets it's new version. Created copy remains untouched

##### After editing, new version of the page becomes a 'current' one

##### Administration can decide, that the last version of the page hasn't passed moderation and mark any other page as 'current'

---

## API should handle the following methods:
1. Retrieve the list of all existing pages
2. Get list of versions for a specific page
3. Get any version for a specific page
4. Get 'current' page
5. Edit the page(create new version)
6. Mark any version of the page as 'current' 