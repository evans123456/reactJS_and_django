from rest_framework import serializers
from articles.models import Article


#serializers are just a way of converting json data into a model


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')