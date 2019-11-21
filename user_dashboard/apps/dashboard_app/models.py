from django.db import models
from apps.login_app.models import User
from datetime import datetime, timedelta, timezone

# Create Validators here

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def time_posted(self):
        now = datetime.now(timezone.utc)
        test_time = now - self.created_at
        minutes = divmod(test_time.seconds,60)
        hours = divmod(test_time.seconds, 3600)
        days = divmod(test_time.seconds, 86400)
        # less than an hour return just the minutes
        print("minutes", minutes[0])
        print("hours", hours[0])
        print("days", days[0])
        if minutes[0] < 1:
            return str(test_time.seconds) + " seconds ago"
        if minutes[0] < 60:
            return str(minutes[0]) + " minutes ago"
        # less than a day return just the hours
        elif hours[0] < 24:
            return str(hours[0]) + " hours ago "
        # less than a week return just the days
        elif days[0] < 7:
            return str(days[0]) + " days ago"
        # over a week, return the date
        else:
            return self.created_at.date()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def time_posted(self):
        now = datetime.now(timezone.utc)
        test_time = now - self.created_at
        minutes = divmod(test_time.seconds,60)
        hours = divmod(test_time.seconds, 3600)
        days = divmod(test_time.seconds, 86400)
        # less than an hour return just the minutes
        print("minutes", minutes[0])
        print("hours", hours[0])
        print("days", days[0])
        if minutes[0] < 1:
            return str(test_time.seconds) + " seconds ago"
        if minutes[0] < 60:
            return str(minutes[0]) + " minutes ago"
        # less than a day return just the hours
        elif hours[0] < 24:
            return str(hours[0]) + " hours ago "
        # less than a week return just the days
        elif days[0] < 7:
            return str(days[0]) + " days ago"
        # over a week, return the date
        else:
            return self.created_at.date()