from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..upload.models import Song
from ..loginandreg.models import User
from .models import Comment
from .forms import CommentForm

def index(request):
    users=User.objects.all()
    context = {
        'users':users,
        'all_songs': Song.objects.all(),
        'comments': Comment.objects.all(),
        'commentForm': CommentForm()

    }
    return render(request, 'soundcloud/index.html', context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))

def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        print user.id
        if len(request.POST['name']) >1:
            user.name= request.POST['name']
            request.session['username'] = user.name
            print user.name
        if len(request.POST['gender']) >1:
            user.gender= request.POST['gender']
        if len(request.POST['email']) >1:
            user.email=request.POST['email']
        if len(request.POST['newpassword']) >1:
            user.password=request.POST['newpassword']
        if len(request.POST['age']) >1:
            user.age=request.POST['age']
        if len(request.POST['description'])>1:
            user.description=request.POST['description']
        try:
            user.image=request.FILES['image']
        except:
            pass
        user.save()
        return redirect(reverse('soundspace:stream'))
    user = User.objects.get(id=id)
    context={
        'user':user
    }

    return render(request, 'soundcloud/user.html', context)

def user(request, id):
    user = User.objects.get(id=id)
    context={
        'user':user
    }
    return render(request, 'soundcloud/userinfo.html', context)

def create_comment(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        song = Song.objects.get(id=request.POST['song_id'])
        Comment.objects.create(user=user, song=song, comment=request.POST['comment'])
        return redirect(reverse('soundspace:stream'))

def delete_comment(request):
    if request.method == 'POST':
        Comment.objects.get(id=request.POST['comment_id']).delete()
        return redirect(reverse('soundspace:stream'))
