from django.db import models

from SignUp.models import User


# Create your models here.

class Board(models.Model):
    boardID = models.AutoField(primary_key=True)  # 게시물 고유번호
    userID = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 정보 불러오는 외래키 (유저 프로필사진, 유저 닉네임)
    boardType = models.SmallIntegerField()  # 게시글 타입(자유,패션,거래)
    title = models.TextField(max_length=25)  # 게시글 제목
    content = models.TextField()  # 게시글 본문
    image = models.TextField()  # 게시글 사진
    datetime = models.DateTimeField(auto_now=True)  # 글 작성 날짜
    like_num = models.PositiveSmallIntegerField(default=0)  # 좋아요 수
    price = models.BigIntegerField(default=0)  # 판매 가격
    state = models.BooleanField(default=True)  # 판매중 상태


class Comment(models.Model):
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE, db_column='boardID')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userID')
    comment = models.TextField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)
    nickname = models.TextField()


class Like(models.Model):
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE, db_column='boardID')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userID')


class Message(models.Model):
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE, db_column='boardID')
    sendID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sendID')
    receiveID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiveID')
    message = models.TextField(max_length=100)


class ReportBoardList(models.Model):
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE, db_column='boardID')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userID')


class Tag(models.Model):
    tagID = models.AutoField(primary_key=True)
    tagName = models.TextField(max_length=15)


class TagBoard(models.Model):
    boardID = models.ForeignKey(Board, on_delete=models.CASCADE, db_column='boardID')
    tagID = models.ForeignKey(Tag, on_delete=models.CASCADE, db_column='tagID')


class StyleRank(models.Model):
    datetime = models.DateField(auto_now_add=True)
    boardID_1 = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boardID_1')
    boardID_2 = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boardID_2')
    boardID_3 = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boardID_3')






