from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('F', 'Forklore'),
        ('N', 'Nonfiction'),
        ('FA', 'Fantasy'),
        ('S', 'Biography'),
        ('P', 'Poetry')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers")
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    pub_year = models.PositiveSmallIntegerField("Publication Year", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    class Meta:
        ordering = ["-author"]

    def image_tag(self):
        if self.cover:
            return mark_safe('<img src="%s" style="width: 200px; height:200px;" />' % self.cover.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

class ReviewManager(models.Manager):
    def review_validator(self, postData):
            errors = {}
            if (len(postData['review']) < 1):
                errors["blank"] = "Review should not be empty!"
            return errors
class Review(models.Model):
    review_text= models.TextField()
    user = models.ForeignKey(User, related_name= "reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    objects=ReviewManager()
    
    def __str__(self):
        return '{} {} {}'.format(self.book, self.user, self.rating)