from django.db import models

from SignUp.models import User


# Create your models here.

class Board(models.Model):
    boardID = models.AutoField(primary_key = True) # 게시물 고유번호
    userID = models.ForeignKey(User,on_delete=models.CASCADE) # 유저 정보 불러오는 외래키 (유저 프로필사진, 유저 닉네임)
    boardType = models.SmallIntegerField() # 게시글 타입(자유,패션,거래)
    title = models.TextField(max_length=25) # 게시글 제목
    content = models.TextField() # 게시글 본문
    image = models.TextField() # 게시글 사진
    datetime = models.DateTimeField(auto_now=True) # 글 작성 날짜
    like_num = models.PositiveSmallIntegerField(default= 0) # 좋아요 수
    price = models.BigIntegerField(default=0) # 판매 가격
    state = models.BooleanField(default=True) # 판매중 상태
