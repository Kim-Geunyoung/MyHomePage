from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=100, null=False)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now = True)
    
class Answer(models.Model):
    answer = models.TextField()
    create_date = models.DateTimeField(auto_now = True)
        