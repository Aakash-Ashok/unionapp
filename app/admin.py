from django.contrib import admin
from .models import (
    Announcement,
    Club,
    ClubMember,
    UnionMember,
    MediaGallery,
    AdminProfile
)

admin.site.register(Announcement)
admin.site.register(Club)
admin.site.register(ClubMember)
admin.site.register(UnionMember)
admin.site.register(MediaGallery)
admin.site.register(AdminProfile)
