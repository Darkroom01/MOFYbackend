# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.views import APIView

from community.models import Board


# Create your views here.

class Main(APIView):
    def get(self, request):
        return render(request, "community/main.html")


class CommunityForm(APIView):
    def get(self, request):
        return render(request, "community/communityForm.html")

    def post(self, request):
        if request.method == "POST":
            title = request.data.get('title')
            content = request.data.get('content')
            image = request.data.get('image')
            datetime = timezone.now()
            board_type = 1
            Board.objects.create(title=title, boardType=board_type,
                                 content=content, image=image,
                                 datetime=datetime)
            return redirect('community')


class FashionForm(APIView):
    def get(self, request):
        return render(request, "community/FashionForm.html")

    def post(self, request):
        if request.method == "POST":
            title = request.data.get('title')
            content = request.data.get('content')
            image = request.data.get('image')
            datetime = timezone.localtime()
            board_type = 2
            Board.objects.create(title=title, boardType=board_type,
                                 content=content, image=image,
                                 datetime=datetime)
            return redirect('fashion')


class SellForm(APIView):
    def get(self, request):
        return render(request, "community/SellForm.html")

    def post(self, request):
        if request.method == "POST":
            title = request.data.get('title')
            content = request.data.get('content')
            image = request.data.get('image')
            price = request.data.get('price')
            state = True
            datetime = timezone.localtime()
            board_type = 3
            Board.objects.create(title=title, boardType=board_type, state=state,
                                 content=content, image=image, price=price,
                                 datetime=datetime)
            return redirect('sell')


class Community(APIView):
    def get(self, request):
        postList = Board.objects.filter(boardType=1)
        return render(request, "community/community.html", {'postList': postList})


class Fashion(APIView):
    def get(self, request):
        fashionList = Board.objects.filter(boardType=2)
        return render(request, "community/fashion.html", {'fashionList': fashionList})


class Sell(APIView):
    def get(self, request):
        productList = Board.objects.filter(boardType=3)
        return render(request, "community/sell.html", {'productList': productList})


class CommunityDetail(APIView):
    def get(self, request, boardID):
        post = Board.objects.get(pk=boardID)
        context = {
            'post': post
        }
        return render(request, 'community/communityDetail.html', context)


class FashionDetail(APIView):
    def get(self, request, boardID):
        post = Board.objects.get(pk=boardID)
        context = {
            'post': post
        }
        return render(request, 'community/fashionDetail.html', context)


class SellDetail(APIView):
    def get(self, request, boardID):
        post = Board.objects.get(pk=boardID)
        context = {
            'post': post
        }
        return render(request, 'community/sellDetail.html', context)


def delete(request, boardID):
    post = Board.objects.get(boardID=boardID)
    boardType = post.boardType
    post.delete()
    if boardType == 1:
        return redirect('community')
    elif boardType == 2:
        return redirect('fashion')
    elif boardType == 3:
        return redirect('sell')


def community_update(request, boardID):
    post = Board.objects.get(boardID=boardID)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.POST['image']
        post.datetime = timezone.localtime()
        post.save()
        return redirect('detail', boardID=post.boardID)
    else:
        post = Board()
        return render(request, 'community/communityUpdate.html', {'post': post})

def fashion_update(request, boardID):
    post = Board.objects.get(boardID=boardID)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.POST['image']
        post.datetime = timezone.localtime()
        post.save()
        return redirect('detail', boardID=post.boardID)
    else:
        post = Board()
        return render(request, 'community/fashionUpdate.html', {'post': post})



def sell_update(request, boardID):
    post = Board.objects.get(boardID=boardID)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.POST['image']
        post.datetime = timezone.localtime()
        post.save()
        return redirect('detail', boardID=post.boardID)
    else:
        post = Board()
        return render(request, 'community/fashionUpdate.html', {'post': post})



def sell_update(request, boardID):
    post = Board.objects.get(boardID=boardID)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.POST['image']
        post.price = request.POST['price']
        post.state = request.POST['state']
        post.datetime = timezone.localtime()
        post.save()
        return redirect('detail', boardID=post.boardID)
    else:
        post = Board()
        return render(request, 'community/sellUpdate.html', {'post': post})
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.POST['image']
        post.price = request.POST['price']
        post.state = request.POST['state']
        post.datetime = timezone.localtime()
        post.save()
        return redirect('detail', boardID=post.boardID)
