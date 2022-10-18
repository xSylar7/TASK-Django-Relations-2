## Steps

### Setup
1. Fork and clone [this repository]() or you can continue workig on your shop task.
2. Create a virtual environment.
3. Install the requirements in `requirements.txt`.

### Category and Item

1. In your models file, create a relation so that every category has multiple items and every item belongs to one category.
2. Don't forget to `makemigrations` and `migrate`.

### Items List and Form

1. In your views file, fix your context dictionary so that you're also sending the category name of every item.
2. Fix your `item-list.html` to show the item's category and image.
3. Fix your form so that the user can choose a category when creating an item.

## Comments
1. In your models file, create a relation so that every item has multiple comments and every comment belongs to one item.
2. In the `item-detail.html` page, list all the comments of this item.
