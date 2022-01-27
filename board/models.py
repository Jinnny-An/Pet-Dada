from pickle import TRUE
<<<<<<< HEAD
#from typing_extensions import Required
=======
# from typing_extensions import Required
>>>>>>> 0f6f996096df881789e261c8ea3f4da83d7a8ea7
from django.db import models


class Review(models.Model):
    #author = models.ForeignKey(user_name, on_delete=models.CASCADE,related_name='author_review')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    file=models.FileField(upload_to='%Y/%m/%d',null=True,blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    #author = models.ForeignKey(user_name, on_delete=models.CASCADE, related_name='author_comment')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title