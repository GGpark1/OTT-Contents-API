from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    # nested serializer
    # 영화가 가지고 있는 review들을 출력함(1:N)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # nested serializer
    # 플랫폼이 가지고 있는 영화들을 출력함(1:N)
    watchlist = WatchListSerializer(
        many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
