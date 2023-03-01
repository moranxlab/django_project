from django.db import models
import datetime
from datetime import timezone , timedelta
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# def validateCleanLang(value):
#     CURSES = ('dumbass','moron')
#     for curse in CURSES:
#         if curse in value

#     def was_published_lately(self):
#         return self.pub_date > timezone.now() -timedelta(days=1)#from last 24 hours

#     def __str__(self) -> str:
#         return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text