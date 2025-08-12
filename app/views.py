from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .models import Announcement, Club, ClubMember, UnionMember, MediaGallery, LoginHistory
from .serializers import (
    AnnouncementSerializer, ClubSerializer,
    ClubMemberSerializer, UnionMemberSerializer,
    MediaGallerySerializer, AdminLoginSerializer
)

# ------------------- Announcement Views -------------------

class ClubMemberListCreateAPIView(APIView):
    def get(self, request):
        club_id = request.query_params.get('club')
        if club_id:
            members = ClubMember.objects.filter(club_id=club_id)
        else:
            members = ClubMember.objects.all()
        serializer = ClubMemberSerializer(members, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnnouncementDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Announcement, pk=pk)

    def get(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

 

    def put(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        announcement = self.get_object(pk)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- Club Views -------------------

class ClubListCreateAPIView(APIView):
    def get(self, request):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    

    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClubDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Club, pk=pk)

    def get(self, request, pk):
        club = self.get_object(pk)
        serializer = ClubSerializer(club)
        return Response(serializer.data)

    
    def put(self, request, pk):
        club = self.get_object(pk)
        serializer = ClubSerializer(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- Club Member Views -------------------

class ClubMemberListCreateAPIView(APIView):
    def get(self, request):
        members = ClubMember.objects.all()
        serializer = ClubMemberSerializer(members, many=True)
        return Response(serializer.data)

    

    def post(self, request):
        serializer = ClubMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClubMemberDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(ClubMember, pk=pk)

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = ClubMemberSerializer(member)
        return Response(serializer.data)

    

    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = ClubMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- Union Member Views -------------------

class UnionMemberListCreateAPIView(APIView):
    def get(self, request):
        members = UnionMember.objects.all()
        serializer = UnionMemberSerializer(members, many=True)
        return Response(serializer.data)

   

    def post(self, request):
        serializer = UnionMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnionMemberDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(UnionMember, pk=pk)

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = UnionMemberSerializer(member)
        return Response(serializer.data)

    
    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = UnionMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- Media Gallery Views -------------------

class MediaGalleryListCreateAPIView(APIView):
    def get(self, request):
        media = MediaGallery.objects.all().order_by('-uploaded_on')
        serializer = MediaGallerySerializer(media, many=True)
        return Response(serializer.data)

    

    def post(self, request):
        serializer = MediaGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaGalleryDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(MediaGallery, pk=pk)

    def get(self, request, pk):
        media = self.get_object(pk)
        serializer = MediaGallerySerializer(media)
        return Response(serializer.data)

    

    def put(self, request, pk):
        media = self.get_object(pk)
        serializer = MediaGallerySerializer(media, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        media = self.get_object(pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- Admin Login & Logout -------------------

class AdminLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)

            # Save login history
            LoginHistory.objects.create(
                user=user,
                ip_address=self.get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )

            return Response({
                'token': token.key,
                'username': user.username,
                'is_superuser': user.is_superuser,
                'user_id': user.id,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


class AdminLogoutView(APIView):
    

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
