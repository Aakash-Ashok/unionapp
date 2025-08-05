from django.db import models
from django.contrib.auth.models import User


# 1. Announcements & Notices
class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('notice', 'Notice'),
        ('circular', 'Circular'),
        ('exam', 'Exam'),
        ('holiday', 'Holiday'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


# 2. Clubs & Committees
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


# 3. Club Members
class ClubMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.role} ({self.club.name})"


# 4. Union Members
class UnionMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo_url = models.URLField()
    contact = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


# 5. Media Gallery (Image or Video)
class MediaGallery(models.Model):
    title = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    image = models.ImageField()  
    thumbnail_url = models.URLField(blank=True, null=True)  
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.event_name})"


# 6. Admin User Profile
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_union_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

from django.utils.timezone import now

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"