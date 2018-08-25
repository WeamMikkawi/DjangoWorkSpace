from django.db import models
from django.urls import reverse

# Create your models here.
class Language(models.Model):
    """
    Model represent Langauge of a book
    """
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Genre(models.Model):
    """
     Model represent a genre of a book
    """
    name = models.CharField(max_length=50, help_text='Enter a book genre')
    def __str__(self):
        return self.name

class Author(models.Model):
    """
    Model represents Authors.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    def get_absulote_url(self):
        """
        :return: the url of accessing author insctance
        """
        return reverse('author-detail', args=[str(self.id)])
class Book(models.Model):
    """
    Model represent a Book in catalog
    """
    title = models.CharField(max_length=200)
    # each book has one auhor, but author can write multiple of books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summery = models.CharField(max_length=500, blank=True, null=True)
    imprint = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=13)
    # each book can have mutible of Genres, and each genre can be descriped in more than one book
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

    def get_absulote_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return [gen.name for gen in self.genre.all()]

class BookInstance(models.Model):
    """
    Model represent a copy of a book
    """
    import uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    bookStatus = (
        ('A', 'Available'),
        ('B', 'Borrowed'),
        ('N', 'Not Exists'),
    )
    status = models.CharField(max_length=1, choices=bookStatus, default='N')
    def __str__(self):
        return "%s - %s" % (self.id, self.book.title)
