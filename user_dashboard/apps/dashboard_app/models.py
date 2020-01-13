from django.db import models
from apps.login_app.models import User
from datetime import datetime, timedelta, timezone, date

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
        hours = int(minutes[0] / 60)
        days = divmod(test_time.seconds, 86400)
        # less than an hour return just the minutes
        print("minutes", minutes[0])
        print("hours", hours)
        print("days", days[0])
        print("test_time", test_time.days)
        # Over a week, return the date
        if test_time.days > 7:
            return(self.created_at.date())
        # Between 1 and 7 days - say 'X days ago'
        elif test_time.days >= 2:
            return str(test_time.days) + " days ago"
        elif test_time.days > 0:
            return str(test_time.days) + " day ago"
        elif hours > 0:
            return str(hours) + " hours ago "
        elif minutes[0] >= 1:
            return str(minutes[0]) + " minutes ago"
        else:
            return str(test_time.seconds) + " seconds ago"

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
        hours = int(minutes[0] / 60)
        days = divmod(test_time.seconds, 86400)
        # less than an hour return just the minutes
        print("minutes", minutes[0])
        print("hours", hours)
        print("days", days[0])
        print("test_time", test_time.days)
        # Over a week, return the date
        if test_time.days > 7:
            return(self.created_at.date())
        # Between 1 and 7 days - say 'X days ago'
        elif test_time.days >= 2:
            return str(test_time.days) + " days ago"
        elif test_time.days > 0:
            return str(test_time.days) + " day ago"
        elif hours > 0:
            return str(hours) + " hours ago "
        elif minutes[0] >= 1:
            return str(minutes[0]) + " minutes ago"
        else:
            return str(test_time.seconds) + " seconds ago"