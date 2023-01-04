from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .models import WatchList, StreamPlatform, Review

# Create your views here.


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    # Validation error를 반환하기 위해 get_query를 정의해주어야 함(-> get 요청 수행)
    # qeuryset을 정의하면 내부적으로 get_query 메소드를 생성하므로,queryset 객체를 만듦
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        # 제출 폼에 현재 pk값을 사전에 저장해둠
        # 2번 영화에 대한 리뷰를 작성한다면
        # 영화 항목이 자동으로 2로 부여됨
        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=movie,
            review_user=review_user)
        # request에서 post 요청자를 식별함(-> user)
        # post가 요청된 user, movie를 식별함
        #   queryset이 없다면 -> None 반환(=False) -> if 통과
        #   queryset이 있다면 -> True 반환 -> raise 발생

        if review_queryset.exists():
            raise ValidationError("You're review already exists")

        serializer.save(watchlist=movie, review_user=review_user)


class ReviewList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        # url에서 입력받은 pk를 kwargs에서 불러옴
        # url에서 입력받은 key에 해당하는 콘텐츠를 가져옴
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class StreamPlatformListAV(APIView):

    def get(self, request):

        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            platform, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):

        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Message": "Not Exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(
            platform)
        return Response(serializer.data)

    def put(self, request, pk):

        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(
            instance=platform, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(
            movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message": "Not Exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#### legacy code ####

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"Error" : "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    # class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    #     queryset = Review.objects.all()
    #     serializer_class = ReviewSerializer

    #     def get(self, request, *args, **kwargs):
    #         return self.retrieve(request, *args, **kwargs)

    # class ReviewList(mixins.ListModelMixin,
    #                  mixins.CreateModelMixin,
    #                  generics.GenericAPIView):
    #     queryset = Review.objects.all()
    #     serializer_class = ReviewSerializer

    #     def get(self, request, *args, **kwargs):
    #         return self.list(request, *args, **kwargs)

    #     def post(self, request, *args, **kwargs):
    #         return self.create(request, *args, **kwargs)

    # class StreamPlatformVS(viewsets.ViewSet):

    #     def list(self, request):
    #         queryset = StreamPlatform.objects.all()
    #         serializer = StreamPlatformSerializer(queryset, many=True)
    #         return Response(serializer.data)

    #     def retrieve(self, request, pk=None):
    #         queryset = StreamPlatform.objects.all()
    #         user = get_object_or_404(queryset, pk=pk)
    #         serializer = StreamPlatformSerializer(user)
    #         return Response(serializer.data)

    #     def create(self, request):
    #         serializer = StreamPlatformSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
