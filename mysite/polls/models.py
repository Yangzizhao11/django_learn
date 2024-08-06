import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class QuestionImage(models.Model):
    class Meta:
        # dbname
        db_table = "media_question_image"

    question = models.ForeignKey(Question, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default='')
    image = models.ImageField(verbose_name="question_image", max_length=256, upload_to="question_image/")

class TestMigration(models.Model):
    class Meta:
        db_table = "not_used"
    