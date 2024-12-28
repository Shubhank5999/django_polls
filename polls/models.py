import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    #def was_published_recently(self):
     #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

  

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


'''
Question = models.ForeignKey(Question, on_delete=models.CASCADE)

models.ForeignKey: This creates a foreign key relationship, linking the Choice model to another model called Question. It establishes a many-to-one relationship:
Each Choice is associated with a single Question.
A Question can have multiple Choice objects related to it.
Question: Refers to the model (table) being linked. This assumes a Question model is defined elsewhere in your code.
on_delete=models.CASCADE: Specifies the behavior when a related Question is deleted:
If a Question is deleted, all the related Choice objects are also deleted (cascade deletion).
'''