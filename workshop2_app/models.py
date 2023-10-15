from django.db import models

# Create your models here.
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)


class Movie(models.Model):
    UID = models.UUIDField  # Computer fields

    # Business fields
    movie_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=200)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.movie_id