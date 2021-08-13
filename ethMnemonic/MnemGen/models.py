from django.db import models

class WordListEntry(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word
