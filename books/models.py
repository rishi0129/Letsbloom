from django.db import models


# Create your models here.
class Books(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('sp', 'Spanish'),
        ('fr', 'French'),
        ('ge', 'German'),
        ('hi', 'Hindi'),
    )
    title = models.CharField(max_length=256, null=False, blank=False)
    author_name = models.CharField(max_length=256, null=False, blank=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Books"
        unique_together = ['title', 'author_name', 'language']
        
    def save(self, *args, **kwargs):
        # Convert fields to lowercase before saving
        self.title = self.title.lower()
        self.author_name = self.author_name.lower()
        self.language = self.language.lower()

        super().save(*args, **kwargs)