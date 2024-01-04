from rest_framework import serializers

from comments.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author_id']

    def create(self, validated_data):
        validated_data['author_id'] = self.context['request'].user
        return super().create(validated_data)
