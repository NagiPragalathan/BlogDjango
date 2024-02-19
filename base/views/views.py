from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from base.models import blog, Comments, SaveBlog
from ..Tools import get_images,reguler_datas,get_blog
import uuid 
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def admin(request):
    item = get_images()
    return render(request,"pages/empty.html",reguler_datas({"categories":item[0],"images":item[1]}))

#...............Blog........................................
def blog_edit(request):
    return render(request,"pages/blog_edit.html")

def save_blog(request):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3], 'Common')
    Thumbnail = request.POST.get(ids[4])

    obj = blog(id=uuid.uuid1(),title=title,description=description,content=content,categories=Category,blog_profile_img=Thumbnail)
    obj.save()
    ob = blog.objects.all()
    for i in ob:
        print(i.blog_profile_img,i.title,i.content)

    return render(request,"pages/blog_edit.html")

def save_edit_blog(request,pk):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = blog.objects.get(id=pk)
    obj.content = content
    obj.title = title
    obj.description = description
    obj.categories = Category
    obj.blog_profile_img = Thumbnail
    obj.save()

    print("Saved...........")

    return render(request,"pages/blog_edit.html")


def list_blog(request):
    items = get_blog()
    print(items)
    return render(request,"home/blog.html",{'blogs':items})

def blogs(request):
    user = request.user
    items = get_blog()
    saved_posts = SaveBlog.objects.filter(User=user).values_list('Post_id', flat=True)
    
    for group in items:
        for blog_item in group:
            if blog_item.id in saved_posts:
                blog_item.is_saved = True
            else:
                blog_item.is_saved = False
    for i in items:
        for j in i:
            print(j.is_saved)
    print(items[0][0].is_saved)
    
    return render(request, "New_Blog/index.html", {'blogs': items})

def view_blog(request,pk): 
    page = blog.objects.get(id=pk)
    items = get_blog()
    print(items)
    random.shuffle(items)
    print(items)
    try:
        comments = Comments.objects.filter(Post_id=pk)
        for i in comments:
            formatted_datetime = i.last_updated_date.strftime("%b. %d, %Y")
            i.last_updated_date = formatted_datetime
            i.first = i.user_id.username[0]
        print(comments)
    except Exception as e:
        print(e)
        comments = False
    
    return render(request,"New_Blog/post.html",{'blog':page,'item':items, "comments":comments, "post_id":pk})

def delete_blog(request):
    bl_id = request.GET.get("id")
    page = blog.objects.get(id=bl_id)
    page.delete()
    return render(request,"home/view_blog.html",{'blog':page})


def list_edit_blog(request):
    items = get_blog()
    return render(request,"home/edit_blog_list.html",{'blogs':items})

def edit_blog(request,pk):
    obj = blog.objects.get(id=pk)
    return render(request,"pages/blog_re_edit.html",{'obj':obj})


def home(request):
    return render(request,"home/index.html")

def new_page(request):
    return  render(request,"New_Blog/post.html")
#............................................................


def comments(request, id):
    if request.method == 'POST':
        try:
            comments = Comments.objects.filter(Post_id=id)
            for i in comments:
                formatted_datetime = i.last_updated_date.strftime("%b. %d, %Y")
                i.last_updated_date = formatted_datetime
                i.first = i.user_id.username[0]
        except Exception as e:
            comments = False
            print(e)
        return  render(request,"home/comments.html", {'comments':comments, "post_id":id})
    return  render(request,"home/comments.html", {"post_id":id})


def create_comment(request, path):
    try:
        comments = Comments.objects.filter(Post_id=path)
        for i in comments:
            formatted_datetime = i.last_updated_date.strftime("%b. %d, %Y")
            i.last_updated_date = formatted_datetime
            i.first = i.user_id.username[0]
        print(comments)
    except Exception as e:
        print(e)
        comments = False
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            user = request.user
            comment = Comments(user_id=user, comment=comment_text, Post_id=path)
            comment.save()
            print("saved..!")
            return redirect('create_comment', path=path)
        else:
            return HttpResponseNotFound("User ID and Comment are required.")
    return  render(request,"home/comments.html", {"post_id":path,"comments":comments})
    


def save_blog1(request, post_id):
    if request.method == 'POST':
        user = request.user
        # post_id = request.POST.get('post_id')
        if post_id:
            # Create a new SaveBlog object and save it to the database
            save_blog = SaveBlog(Post_id=post_id, User=user)
            save_blog.save()
            print("saved..!")
            # Return a JSON response indicating success
            return JsonResponse({'success': True, 'message': 'Blog saved successfully.'})
        else:
            # Return a JSON response indicating failure
            return JsonResponse({'success': False, 'error_message': 'Post ID is required.'})
    else:
        # Return a JSON response for invalid request method
        return JsonResponse({'success': False, 'error_message': 'Invalid request method.'})