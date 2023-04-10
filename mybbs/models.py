# from django.conf import settings
from django.db import models
from django.utils import timezone

#組み込みユーザー用　（フィールドのカスタマイズ（追加・変更・削除）ができないということ？）
from django.contrib.auth.models import User

# #カスタムユーザーを使うために組み込みユーザーを継承する用
# from django.contrib.auth.models import AbstractUser

#カスタムユーザーを使うために組み込みユーザーを継承する用
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


#以下は必要？
from django.conf import settings

# 定数的なもの
PUBLIC_RANGE = (
    (1, "全体"),
    (2, "会員限定"),
    (3, "完全限定（利用しない）"),
)



# Create your models here.


# class User(models.Model):
# class User(AbstractUser):
#     #
#     name = models.CharField('ユーザーネーム', max_length=255,blank=False,null=False)
#     content = models.TextField('内容', blank=True,null=False)
#     level = models.IntegerField('レベル', blank=True,null=False)
#     experience = models.IntegerField('経験値', blank=True,null=False)

#     #このカテゴリの自分自身の名前
#     def __str__(self):
#         return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        # default="カテゴリーなし",
        blank=True,
        null=True,
        unique=True)

    #このカテゴリの自分自身の名前
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        # default="タグなし",
        blank=True,
        null=True,
        unique=True)

    #自分自身の名前
    def __str__(self):
        return self.name


class Post(models.Model):

    MEDIA_TYPE = (
        (1, "写真"),
        (2, "動画"),
        (3, "音声"),
    )

    title = models.CharField('タイトル', max_length=255,blank=False,null=False)
    content = models.TextField('内容', blank=True,null=False)
    created_at = models.DateTimeField('投稿日', auto_now_add=True, null=False)
    updated_at = models.DateTimeField('更新日', auto_now=True, null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,blank=True,related_name="post")
    # media              = models.ImageField(verbose_name='メディアファイル', upload_to=path_and_rename)
    # media_type         = models.SmallIntegerField(verbose_name='メディアタイプ', choices=MEDIA_TYPE, default=1)
    comment_count      = models.BigIntegerField(verbose_name='コメント数', default=0)
    like_count         = models.BigIntegerField(verbose_name='Like数', default=0)
    public_range       = models.SmallIntegerField(verbose_name='公開範囲', choices=PUBLIC_RANGE, default=1)

    #自分自身の名前
    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = '01_投稿内容'
        # db_table = 'post'


class Quiz(models.Model):
    title = models.CharField('タイトル', max_length=128)
    content = models.TextField('内容', blank=True)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now_add=True)
    created_at = models.DateTimeField('投稿日', null=True ,auto_now_add=True)
    updated_at = models.DateTimeField('更新日', null=True ,auto_now_add=True)



class Seiseki(models.Model):
    pass


