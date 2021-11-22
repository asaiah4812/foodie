from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body

class Comment(models.Model):
    body = models.TextField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body

class UpVote(models.Model):
    voted_by = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"User={self.voted_by} : Post = {self.post}"

class DownVote(models.Model):
    down_voted_by = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    down_voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"User={self.down_voted_by} : Post = {self.post}"