from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profilepictures')
    profile_link = models.URLField(blank=True, null=True)
    profile_number = models.CharField(max_length=11, null=True, blank=True)
    profile_created = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    category_img = models.ImageField(blank=True, null=True, upload_to='categoryimages')

    def __str__(self):
        return self.category

class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    post_img = models.ImageField(upload_to='posts')
    post_name = models.CharField(max_length=200)
    post_alt = models.CharField(max_length=200, blank=True, null=True)
    post_description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_created_at = models.DateTimeField(auto_now_add=True, editable=False)
    post_modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    class Meta:
        ordering = ['-post_created_at']
    
    def get_absolute_url(self):
        return reverse_lazy("app:detail-post", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.post_name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment
