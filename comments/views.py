from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentListSerializer


class CommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(tags=['Comments'], summary='Comments listing', parameters=[
    OpenApiParameter(
        name='post_id',
        location=OpenApiParameter.QUERY,
        type=int,
        required=False,
        description='ID of the post to filter comments'
    )
])
class CommentListView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = Comment.objects.filter(post_id=post_id)
        else:
            queryset = Comment.objects.all()
        return queryset
