from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Admin Login/Logout
    path('admin-login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('admin-logout/', views.AdminLogoutView.as_view(), name='admin-logout'),

    # Announcements
    path('announcements/', views.AnnouncementListCreateAPIView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', views.AnnouncementDetailAPIView.as_view(), name='announcement-detail'),

    # Clubs
    path('clubs/', views.ClubListCreateAPIView.as_view(), name='club-list-create'),
    path('clubs/<int:pk>/', views.ClubDetailAPIView.as_view(), name='club-detail'),

    # Club Members
    path('club-members/', views.ClubMemberListCreateAPIView.as_view(), name='club-member-list-create'),
    path('club-members/<int:pk>/', views.ClubMemberDetailAPIView.as_view(), name='club-member-detail'),

    # Union Members
    path('union-members/', views.UnionMemberListCreateAPIView.as_view(), name='union-member-list-create'),
    path('union-members/<int:pk>/', views.UnionMemberDetailAPIView.as_view(), name='union-member-detail'),

    # Media Gallery
    path('media-gallery/', views.MediaGalleryListCreateAPIView.as_view(), name='media-gallery-list-create'),
    path('media-gallery/<int:pk>/', views.MediaGalleryDetailAPIView.as_view(), name='media-gallery-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)