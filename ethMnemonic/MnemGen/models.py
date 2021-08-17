from django.db import models
# Defines the db table for the wordlist used in the project.
class WordListEntry(models.Model):
    # Defining paramaters of each word
    word = models.CharField(max_length=50)
    # String representation of a word entry.
    def __str__(self):
        return self.word
