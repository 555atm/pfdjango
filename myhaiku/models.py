from django.db import models

# Create your models here.


class Haiku(models.Model):
    kaminoku = models.CharField('上の句', max_length=64, blank=False,null=False)
    nakanoku = models.CharField('中の句', max_length=64,blank=False,null=False)
    shimonoku = models.CharField('下の句', max_length=64,blank=False,null=False)
    kami_random = models.TextField('上ランダム文字', max_length=64,blank=False,null=False)
    naka_random = models.TextField('中ランダム文字', max_length=64,blank=False,null=False)
    shimo_random = models.TextField('下ランダム文字', max_length=64,blank=False,null=False)
    # member_id = models.ForeignKey(User,verbose_name='メンバー')
    created_at = models.DateTimeField('投稿日', auto_now_add=True, null=False)
    updated_at = models.DateTimeField('更新日', auto_now=True, null=False)

    #このカテゴリの自分自身の名前
    def __str__(self):
        return self.kaminoku
