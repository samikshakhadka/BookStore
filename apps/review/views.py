from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
