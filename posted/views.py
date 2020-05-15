import random
import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post, Category, Tag, Comment, Good
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView
from .forms import IdeaGenerateForm, CommentForm
from django.utils import timezone
from  django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def idea_generator(request):

    Tech_li = {'tech0': 'AR', 'tech1': 'VR', 'tech2': 'AI', 'tech3': 'IoT', 'tech4': '5G', 'tech5': '6G', 'tech6': '7G', 'tech7': 'CG', 'tech8': 'スマートスピーカー', 'tech9': '3dプリンタ', 'tech10': 'ブロックチェーン', 'tech11': '自動運転', 'tech12': '言語翻訳'}
    Agri_li = {'agri0': '水耕栽培', 'agri1': '地中海式農業', 'agri2': '畜産', 'agri3': '酪農', 'agri4': '園芸農業', 'agri5': '混合農業', 'agri6': 'プランテーション', 'agri7': '遊牧', 'agri8': '焼畑', 'agri9': '耕作', 'agri10': '有機栽培', 'agri11': '自然農法', 'agri12': '無農薬', 'agri13': 'バイオダイナミック農法', 'agri14': '植物工場'}
    Web_service_li = {'web0': '情報検索機能', 'web1': '情報自動所得', 'web2': 'EC', 'web3': 'web会議', 'web4': 'データベース', 'web5': 'クラウド', 'web6': 'SNS', 'web7': 'メディア'}
    AI_li = {'AI0': '迷惑メールフィルタ', 'AI1': '音声認識', 'AI2': 'レコメンデーション', 'AI3': '会話bot', 'AI4': '音声合成', 'AI5': '自動運転車', 'AI6': '感情推定', 'AI7': '画像認識', 'AI8': '画像変換'}
    Religion_li = {'religion0': 'ユダヤ教', 'religion1': 'キリスト教系', 'religion2': 'キリスト教', 'religion3': 'キリスト教系新宗教', 'religion4': 'イスラーム', 'religion5': 'インド宗教', 'religion6': 'ヒンドゥー教', 'religion7': 'インドの自由思想家', 'religion8': 'ジャイナ教', 'religion9': 'シク教', 'religion10': 'ゾロアスター教', 'religion11': '仏教', 'religion12': 'インド仏教', 'religion13': '南伝仏教', 'religion14': '北伝仏教'}
    Feeling_li = {'feeling0': '触覚', 'feeling1': '味覚', 'feeling2': '嗅覚', 'feeling3': '視覚', 'feeling4': '聴覚'}

    Category_li = [Tech_li, Agri_li, Web_service_li, AI_li, Religion_li, Feeling_li, ]

    Categories = {'tech': Tech_li, 'agri': Agri_li, 'web':Web_service_li,
     'AI': AI_li, 'religion': Religion_li, 'feeling': Feeling_li}
    Categories_ja = {'tech': 'テクノロジー', 'agri': '農業', 'web': 'Web', 'AI': 'AI', 'religion': '宗教', 'feeling': '五感' }


    a = request.GET.get('test1')
    b = request.GET.get('test2')
    c = request.GET.get('test3')
    number = request.GET.get('number')
    Comb = [None,None,None,None,None,None,None,None,None,None]
    idea1 = [None,None,None,None,None,None,None,None,None,None]
    idea2 = [None,None,None,None,None,None,None,None,None,None]
    idea3 = [None,None,None,None,None,None,None,None,None,None]
    
    #ideaを指定された数ランダム生成
    for x in range(int(number)):
        a_out = None
        b_out = None
        c_out = None
        a_category = None
        b_category = None
        c_category = None
        a_categories_ja = None
        b_categories_ja = None
        c_categories_ja = None
        

        #カテゴリーを選択されたときのランダム生成
        for category, value in Categories.items():
            if (a != b and a != c and b != c):
                if (category == a):
                    a_out = random.choice(list(value.values()))
                elif (category == b):
                    b_out = random.choice(list(value.values()))
                elif (category == c):
                    c_out = random.choice(list(value.values()))
            elif (a == b and a == c and b == c ):
                if (category == a):
                    a_out = random.choice(list(value.values()))
                    b_out = random.choice(list(value.values()))
                    c_out = random.choice(list(value.values()))
            elif (a == b and a != c):
                if (category == a):
                    a_out = random.choice(list(value.values()))
                    b_out = random.choice(list(value.values()))
                elif (category == c):
                    c_out = random.choice(list(value.values()))
            elif (a == c and a != b):
                if (category == a):
                    a_out = random.choice(list(value.values()))
                    c_out = random.choice(list(value.values()))
                elif (category == b):
                    b_out = random.choice(list(value.values()))
            elif (b == c and a != b):
                if (category == b):
                    b_out = random.choice(list(value.values()))
                    c_out = random.choice(list(value.values()))
                elif (category == a):
                    a_out = random.choice(list(value.values()))

        #listを選択されたときのアイデア生成
        for i in range(3):
            for i in range(len(Category_li)):
                for key, value in Category_li[i].items():
                    if key == a and a_out == None:
                        a_out = value
                    elif key == b and b_out == None:
                        b_out = value
                    elif key == c and c_out == None:
                        c_out = value

                    idea1[x] = a_out
                    idea2[x] = b_out
                    idea3[x] = c_out
                    
            #getから取得したのがlistのときカテゴリーを出力
            for k, v in Categories.items():
                for key, value in v.items():
                    if key == a and a_category == None:
                        a_category = k
                    elif key == b and b_category == None:
                        b_category = k
                    elif key == c and c_category == None:
                        c_category = k

            for key, value in Categories_ja.items():
                if key == a_category and a_categories_ja == None:
                    a_categories_ja = value
                elif key == b_category and b_categories_ja == None:
                    b_categories_ja = value
                elif key == c_category and c_categories_ja == None:
                    c_categories_ja = value


        if (a_out is not None) and (b_out is not None) and (c_out is not None):
            Comb[x] = a_out + "　×　" + b_out + "　×　" + c_out

    form = IdeaGenerateForm()
    if request.method == 'POST':
        form = IdeaGenerateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('posted:post')
    else:
        form = IdeaGenerateForm()

    context = {
        'idea1_0': idea1[0], 'idea2_0': idea2[0], 'idea3_0': idea3[0],
        'idea1_1': idea1[1], 'idea2_1': idea2[1], 'idea3_1': idea3[1],
        'idea1_2': idea1[2], 'idea2_2': idea2[2], 'idea3_2': idea3[2],
        'idea1_3': idea1[3], 'idea2_3': idea2[3], 'idea3_3': idea3[3],
        'idea1_4': idea1[4], 'idea2_4': idea2[4], 'idea3_4': idea3[4],
        'idea1_5': idea1[5], 'idea2_5': idea2[5], 'idea3_5': idea3[5],
        'idea1_6': idea1[6], 'idea2_6': idea2[6], 'idea3_6': idea3[6],
        'idea1_7': idea1[7], 'idea2_7': idea2[7], 'idea3_7': idea3[7],
        'idea1_8': idea1[8], 'idea2_8': idea2[8], 'idea3_8': idea3[8],
        'idea1_9': idea1[9], 'idea2_9': idea2[9], 'idea3_9': idea3[9],
        'text0': Comb[0],
        'text1': Comb[1],
        'text2': Comb[2],
        'text3': Comb[3],
        'text4': Comb[4],
        'text5': Comb[5],
        'text6': Comb[6],
        'text7': Comb[7],
        'text8': Comb[8],
        'text9': Comb[9],
        'category1': a_categories_ja,
        'category2': b_categories_ja,
        'category3': c_categories_ja,
        'form': form,
    }
    return render(request, 'posted/post_form.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("posted:post_detail", kwargs={
                'id': post.pk
            }))

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posted/post_detail.html', context)

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('../../')

    context = {}
    return render(request, 'posted/comment_delete.html', context)


@login_required(redirect_field_name='login')
def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contents = {
        'post' : Post.objects.all(),
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'posted/post_list.html', contents)


@login_required(redirect_field_name='login')
def like(request, pk):
    #いいね機能

    good_post = Post.objects.get(pk=pk)

    # 自分がpostにGoodした数を調べる
    is_good = Good.objects.filter(owner=request.user).filter(post=good_post).count()
    # ゼロより大きければ既にgood済み  is_good = 0 or 1
    if is_good % 2 == 1:
        good_post.like -= 1
        good_post.save()
        good = Good()
        good.owner = request.user
        good.post = good_post
        good.save()
        return redirect('posted:post')  # good_post.get_absolute_url()

    # Postのgood_countを１増やす
    good_post.like += 1
    good_post.save()
    # Goodを作成し、設定して保存
    good = Good()
    good.owner = request.user
    good.post = good_post
    good.save()
    return redirect('posted:post')


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class TagListView(ListView):
    # annotate()に集計関数のCount()を引数として渡す
    queryset = Tag.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class CategoryPostView(ListView):
    model = Post
    template_name = 'posted/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostView(ListView):
    model = Post
    template_name = 'posted/tag_post.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

def mypost(request):
    mypost_objs = Post.objects.filter(author=request.user)
    context = {
        'myposts': mypost_objs
    }
    return render(request, 'posted/mypost.html', context)

# create user's own tags and elements
# def list_create(request, id):
#     original = get_object_or_404(Original, pk=id)
#     # category = Original.objects.filter(category='Original')
#     form = TagElementsCreateForm()

#     if request.method == 'POST':
#         form = TagElementsCreateForm(request.POST)
#         add_tag = Tag.objects.create()
#         if form.is_valid():
#             post = form.save(commit=False) 
#             post.author = request.user
#             post.category = 'Original'   
#             post.save()

#     context ={
#         # 'category': category,
#         'form': form,
#         'original': original,
#     }
#     return render(request, 'posted/list_create.html', context)