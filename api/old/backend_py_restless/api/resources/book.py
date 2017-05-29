from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from ..schemas import Book


class BookResource(FlaskResource):
    preparer = FieldsPreparer(
        fields = {
            'uid': 'uid',
            'title': 'title',
            'body': 'content',
        }
    )

    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

    # GET /api/books/
    def list(self):
        return Book.nodes.all()

    # GET /api/books/<pk>/
    def detail(self, pk):
        return Book.nodes.get(uid=pk)

    # POST /api/books/
    def create(self):
        book = Book(
            # uid=self.data['uid'],
            title=self.data['title'],
            content=self.data['body'],
        ).save()
        return book

    # PUT /api/books/<pk>/
    def update(self, pk):
        try:
            book = Book.nodes.get(uid=pk)
        except Book.DoesNotExist:
            book = Book()

        book.title = self.data['title']
        book.content = self.data['body']
        book.uid = pk
        book.save()
        return book

    # DELETE /api/books/<pk>/
    def delete(self, pk):
        Book.nodes.get(uid=pk).delete()
