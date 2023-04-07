from django.db import models
# from ..user.models import User
from user.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/post')
    publish_date = models.DateTimeField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=[('pe', 'pending'), ('pu', 'published'), ('re', 'reject'), ('dr', 'draft')], max_length=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     self.publish_date


class Comment(models.Model):
    content = models.CharField(max_length=200)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey('self', on_delete=models.CASCADE)
    status = models.CharField(choices=[('pe', 'pending'), ('pu', 'published'), ('re', 'reject'), ('dr', 'draft')], max_length=2)
    publish_date = models.DateTimeField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
