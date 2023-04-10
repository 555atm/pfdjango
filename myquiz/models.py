from django.db import models



# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        # default="カテゴリーなし",
        blank=False,
        null=False,
        unique=True
        )
    created_at = models.DateTimeField('投稿日', auto_now_add=True, null=False)
    updated_at = models.DateTimeField('更新日', auto_now=True, null=False)

    #このカテゴリの自分自身の名前
    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField('タイトル', max_length=255,blank=False,null=False)
    # genre = models.ForeignKey(Genre,verbose_name='ジャンル',on_delete=models.CASCADE, related_name='genre')
    genre = models.ForeignKey(Genre,verbose_name='ジャンル', on_delete=models.CASCADE, related_name='genre')
    question = models.TextField('問題', blank=True,null=False)
    choice_a = models.TextField('選択肢a', blank=True,null=False)
    choice_b = models.TextField('選択肢b', blank=True,null=False)
    choice_c = models.TextField('選択肢c', blank=True,null=False)
    answer = models.TextField('答え', blank=True,null=False)
    # commentary = models.TextField('解説', blank=True,null=True)
    # member_id = models.ForeignKey(User,verbose_name='出題者')
    created_at = models.DateTimeField('投稿日', auto_now_add=True, null=False)
    updated_at = models.DateTimeField('更新日', auto_now=True, null=False)

    #このカテゴリの自分自身の名前
    def __str__(self):
        return self.title


# INSERT INTO `quiz_book` (`id`, `question`, `choice_a`, `choice_b`, `choice_c`, `answer`, `commentary`, `genre`, `member_id`, `created`, `modified`) VALUES
# (1, '1+1は？', '1', '2', '3', '2', '特になし', '足し算', NULL, NULL, '2022-04-10 13:20:30'),
# (2, '2+2は？', '1', '2', '4', '4', 'ないよ', '足し算', NULL, NULL, '2022-04-10 13:20:57'),
# (3, 'サッカーワールドカップ第一回は1930年に開催された。優勝国はどこ？', 'ブラジル', 'イタリア', 'ウルグアイ', 'ウルグアイ', '第一回優勝国はウルグアイ。ちなみに開催地もウルグアイだった。', 'スポーツ', NULL, '2022-04-09 20:42:59', '2022-04-20 09:18:49'),
# (4, '9-4は？', '4', '5', '6', '5', '特になし', '引き算', NULL, '2022-04-09 21:31:04', '2022-04-10 13:22:01'),
# (5, '17-9は？', '8', '7', '10', '8', '特になし', '引き算', NULL, '2022-04-09 21:31:04', '2022-04-10 13:23:25'),
# (6, '2022年サッカーワールドカップの開催地はどこ？', 'フランス', 'カタール', 'ダカール', 'カタール', 'カタールです。', 'スポーツ', NULL, '2022-04-09 22:08:01', '2022-04-19 07:30:33'),
# (7, 'サッカーワールドカップ第二回は1934年に開催された。優勝国はどこ？', 'ウルグアイ', 'イタリア', 'ブラジル', 'イタリア', '第二回優勝国はイタリア。ちなみに、開催地もイタリア。', 'スポーツ', NULL, '2022-04-10 20:17:36', '2022-04-20 09:19:15'),
# (8, '本は英語で？', 'book', 'boot', 'textbook', 'book', 'いやいやいや。', '英語', NULL, '2022-04-13 22:13:42', '2022-04-20 09:20:16'),
# (9, '11 x  11 は？', '120', '121', '1111', '121', 'なし', 'かけ算', NULL, '2022-04-25 20:09:16', '2022-04-25 11:09:16'),
# (10, '9 足す　12　は？', '20', '22', '21', '21', '正解は21です', '足し算', NULL, '2022-04-30 10:21:38', '2022-04-30 01:21:38'),
# (11, '日本の都道府県で2番目に人口が多いのは？（2022年時点）', '埼玉県', '大阪府', '神奈川県', '神奈川県', '2位は神奈川県です。大阪府は3位です。2位と3位は殆ど差がありませんケドね。', '地理', NULL, '2022-04-30 21:47:37', '2022-04-30 12:48:29'),
# (12, '大型犬といえば？\r\n', 'ブルドッグ', 'プードル', 'ピットブル', 'ピットブル', '', 'アニマル', NULL, '2022-05-03 15:08:51', '2022-05-03 06:08:51'),
# (13, 'a', 'a', 'a', 'a', 'a', 'a', 'a', NULL, '2022-05-07 00:00:03', '2022-05-06 15:00:03');

