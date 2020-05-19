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
from  django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http.response import JsonResponse
from django.contrib import messages
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User



from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def idea_generator(request):

    Phisi_li = {'phisi0': '音', 'phisi1': '光', 'phisi2': '波', 'phisi3': '熱', 'phisi4': '電磁', 'phisi5': '天体', 'phisi6': 'ドップラー現象', 'phisi7': '地球物理学', 'phisi8': '物理気象'}
    Medi_li = {'medi0': '解剖', 'medi1': '生理', 'medi2': '薬学', 'medi3': '組織学', 'medi4': '内科', 'medi5': '外科', 'medi6': '分子生物'}
    Chemi_li = {'chemi0': '化学反応', 'chemi1': '気体', 'chemi2': '固体', 'chemi3': '液体', 'chemi4': '生化学', 'chemi5': '環境化学', 'chemi6': '有機化学', 'chemi7': '無機化学'}
    Tech1_li = {'tech1_0': 'AR', 'tech1_1': 'VR', 'tech1_2': 'AI', 'tech1_3': 'IoT', 'tech1_4': '5G', 'tech1_5': '6G', 'tech1_6': 'CG', 'tech1_7': 'ドローン', 'tech1_8': '3dプリンタ', 'tech1_9': 'ブロックチェーン', 'tech1_10': '自動運転', 'tech1_11': '言語翻訳'}
    Tech2_li = {'tech2_0': '仮想通貨', 'tech2_1': 'インターネット', 'tech2_2': 'スマホ', 'tech2_3': 'ウェアラブル', 'tech2_4': 'xR', 'tech2_5': '3Dプリンタ', 'tech2_6': 'スマートスピーカー', 'tech2_7': '培養肉', 'tech2_8': '自動化', 'tech2_9': 'ロボット', 'tech2_10': 'オンライン'}
    Energy_li = {'energy0': '風力', 'energy1': '火力', 'energy2': '石炭', 'energy3': '石油', 'energy4': 'バイオエネルギー', 'energy5': '太陽光', 'energy6': 'フリーエネルギー', 'energy7': '永久機関'}
    Nature_li = {'nature0': '山', 'nature1': '川', 'nature2': '砂漠', 'nature3': '海', 'nature4': '動物', 'nature5': '植物', 'nature6': '虫'}
    Agri_li = {'agri0': '自然農法', 'agri1': '有機栽培', 'agri2': '植物工場', 'agri3': '家庭菜園'}
    Space_li = {'space0': '惑星', 'space1': '宇宙膨張', 'space2': '衛星'}
    Buisiness_li = {'buisiness0': '観光業', 'buisiness1': '農業', 'buisiness2': '工業', 'buisiness3': '水産業', 'buisiness4': '建設業', 'buisiness5': 'サービス業', 'buisiness6': '広告業', 'buisiness7': '林業', 'buisiness8': '医療'}
    Infra_li = {'infra0': '水道', 'infra1': '電気', 'infra2': '道路', 'infra3': 'ガス', 'infra4': '公園'}
    Poli_li = {'poli0': '自由主義', 'poli1': '社会主義', 'poli2': '資本主義', 'poli3': '共産主義', 'poli4': 'リベラリズム', 'poli5': '植民地', 'poli6': 'リアリズム'}
    Nation_li = {'nation0': '中国', 'nation1': 'アメリカ', 'nation2': 'ロシア', 'nation3': 'ドイツ', 'nation4': 'イタリア', 'nation5': 'フランス', 'nation6': 'スーダン', 'nation7': 'ブラジル', 'nation8': 'チリ', 'nation9': 'アルゼンチン', 'nation10': 'カナダ', 'nation11': 'インド', 'nation12': 'タイ', 'nation13': '日本', 'nation14': 'オーストラリア'}
    Inst1_li = {'inst1_0': '居酒屋', 'inst1_1': '１００均', 'inst1_2': 'ゲームセンタ', 'inst1_3': 'タピオカ', 'inst1_4': 'ブッフェ', 'inst1_5': '本屋', 'inst1_6': 'カフェ', 'inst1_7': '自転車屋', 'inst1_8': '玩具屋', 'inst1_9': 'コンビニ', 'inst1_10': '花屋', 'inst1_11': '駄菓子屋', 'inst1_12': '酒屋', 'inst1_13': '自動販売機', 'inst1_14': '学校', 'inst1_15': '病院', 'inst1_16': 'ガソリンスタンド'}
    Inst2_li = {'inst2_0': '児童館', 'inst2_1': 'ジム', 'inst2_2': 'お寺', 'inst2_3': '神社', 'inst2_4': '美容院', 'inst2_5': '床屋', 'inst2_6': '不動産屋', 'inst2_7': '中古店', 'inst2_8': '電気屋', 'inst2_9': 'アウトレット', 'inst2_10': '楽器屋', 'inst2_11': 'アクセサリー店', 'inst2_12': '洋服や', 'inst2_13': 'ファストフード', 'inst2_14': '文房具屋', 'inst2_15': 'ファミレス', 'inst2_16': '八百屋'}
    Edu_li = {'edu0': '教育科目', 'edu1': '奨学金'}
    Cust_li = {'cust0': 'おもてなし', 'cust1': 'ハグ', 'cust2': '握手', 'cust3': 'お辞儀'}
    Art_li = {'art0': '絵画', 'art1': '映画', 'art2': '音楽', 'art3': '彫刻', 'art4': '建築'}
    Life_li = {'life0': 'スポーツ', 'life1': 'エンタメ', 'life2': 'アート', 'life3': '食事', 'life4': '料理', 'life5': '睡眠', 'life6': '衣服'}
    Sense_li = {'sense0': '触覚', 'sense1': '味覚', 'sense2': '嗅覚', 'sense3': '視覚', 'sense4': '聴覚'}
    Feeling_li = {'feeling0': '喜', 'feeling1': '怒', 'feeling2': '哀', 'feeling3': '楽', 'feeling4': '恥'}
    BP_li = {'bp0': '頭', 'bp1': '腕', 'bp2': '腹', 'bp3': 'お尻', 'bp4': '足', 'bp5': 'ちんちん', 'bp6': '臓器'}
    
    Category_li = [Phisi_li, Medi_li, Chemi_li, Tech1_li, Tech2_li, Energy_li, Nature_li, Agri_li, Space_li, Buisiness_li, Infra_li, Poli_li, Nation_li, Inst1_li, 
               Inst2_li, Edu_li, Cust_li, Art_li, Life_li, Sense_li, Feeling_li, BP_li]

    Categories = {'phisi': Phisi_li, 'medi': Medi_li, 'chemi': Chemi_li, 'tech1_': Tech1_li, 'tech2_': Tech2_li, 'energy': Energy_li, 'nature': Nature_li, 'agri': Agri_li, 'space': Space_li, 'buisiness': Buisiness_li, 'infra': Infra_li, 'poli': Poli_li, 'nation': Nation_li, 'inst1_': Inst1_li, 
               'inst2_': Inst2_li, 'edu': Edu_li, 'cust': Cust_li, 'art': Art_li, 'life': Life_li, 'sense': Sense_li, 'feeling': Feeling_li, 'bp': BP_li}

    Categories_ja = {'phisi': '物理', 'medi': '医学', 'chemi': '化学', 'tech1_': 'テクノロジー１', 'tech2_': 'テクノロジー２', 'energy': 'エネルギー', 'nature': '自然', 'agri': '農業', 'space': '宇宙', 'buisiness': 'ビジネス', 'infra': 'インフラ', 'poli': '政治', 'nation': '国', 'inst1_': '施設１', 'inst2_': '施設２', 'edu': '教育', 'cust': '習慣', 'art': '芸術', 'life': '生活・暮らし', 'sense': '五感', 'feeling': '感情', 'bp': '体のパーツ'}


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

## オリジナル
# @login_required(redirect_field_name='login')
# def post_list(request):
#     keyword = request.GET.get('keyword')
#     object_list = Post.objects.all()
#     paginator = Paginator(object_list, 10) # Show 25 contacts per page.
#     page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#     page_obj = Post.objects.all() # paginationの場合は上

#     if keyword:
#         page_obj = page_obj.filter(
#                   Q(tags__name__icontains=keyword)
#                )
#         messages.success(request, '「{}」の検索結果'.format(keyword))
    
#     context = {
#         'paginator': paginator,
#         'page_obj': page_obj,
#         'object_list' : object_list,     
#     }
#     return render(request, 'posted/post_list.html', context)

@login_required(redirect_field_name='login')
def post_list(request):
    object_list = Post.objects.all()
    category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
    tag_num = Tag.objects.annotate(number_of_post=Count('post')).order_by('-number_of_post')[:10]
    like_num = Post.objects.annotate(number_of_like=Count('like')).order_by('-number_of_like')[:5]
    paginator = Paginator(object_list, 10) # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'post': Post.objects.all(),
        'category_num': category_num, 
        'paginator': paginator,
        'page_obj': page_obj,
        'object_list' : object_list,
        'tag_num': tag_num, 
        'like_num': like_num,
    }
    return render(request, 'posted/post_list.html', context)


def post_search_list(request):
    posts = None
    keyword = None
    category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
    tag_num = Tag.objects.annotate(number_of_post=Count('post')).order_by('-number_of_post')[:10]
    like_num = Post.objects.annotate(number_of_like=Count('like')).order_by('-number_of_like')[:5]
    like = 'いいね'
    search = '検索'
    #検索機能の実装
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        posts = Post.objects.all().filter(Q(tags__name__icontains=keyword))
    #ページネーションの実装
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    #追加
    csrf_token = request.GET.get('csrfmiddlewaretoken')
    page_obj = paginator.get_page(page)
    messages.success(request, '「{}」の検索結果'.format(keyword))
    #修正
    context = {
        'keyword':keyword, 
        'posts':posts, 
        'csrf_token':csrf_token,
        'like': like,
        'search': search,
        'page_obj': page_obj,
        'category_num': category_num,  
        'tag_num': tag_num,
        'like_num': like_num,

        }

    return render(request, 'posted/post_search_list.html', context)


@login_required(redirect_field_name='login')
def category_post(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    queryset = Post.objects.all().filter(Q(category__name__icontains=category))
    category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
    tag_num = Tag.objects.annotate(number_of_post=Count('post')).order_by('-number_of_post')[:10]
    like_num = Post.objects.annotate(number_of_like=Count('like')).order_by('-number_of_like')[:5]
    paginator = Paginator(queryset, 10) # Show 10 posts per page.

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        queryset = paginator.page(page)
    except (EmptyPage, InvalidPage):
        queryset = paginator.page(paginator.num_pages)

    #追加
    csrf_token = request.GET.get('csrfmiddlewaretoken')
    page_obj = paginator.get_page(page)
    
    
    context = {
        'post': Post.objects.all(),
        'category_num': category_num, 
        'paginator': paginator,
        'page_obj': page_obj,
        'category': category,
        'queryset': queryset,
        'csrf_token':csrf_token,
        'tag_num': tag_num, 
        'like_num': like_num,


    }
    return render(request, 'posted/category_post.html', context)


@login_required(redirect_field_name='login')
def popular_tag_post(request, tag_slug):
    tags = get_object_or_404(Tag, slug=tag_slug)
    queryset = Post.objects.all().filter(Q(tags__name__icontains=tags))
    category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
    tag_num = Tag.objects.annotate(number_of_post=Count('post')).order_by('-number_of_post')[:10]
    like_num = Post.objects.annotate(number_of_like=Count('like')).order_by('-number_of_like')[:5]
    paginator = Paginator(queryset, 10) # Show 10 posts per page.
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        queryset = paginator.page(page)
    except (EmptyPage, InvalidPage):
        queryset = paginator.page(paginator.num_pages)

    #追加
    csrf_token = request.GET.get('csrfmiddlewaretoken')
    page_obj = paginator.get_page(page)
    
    context = {
        'post': Post.objects.all(),
        'category_num': category_num, 
        'paginator': paginator,
        'page_obj': page_obj,
        'tags': tags,
        'queryset': queryset,
        'csrf_token':csrf_token,
        'tag_num': tag_num,
        'like_num': like_num,
  
    }
    return render(request, 'posted/popular_tag_post.html', context)
# @login_required(redirect_field_name='login')
# def post_list(request):
#     object_list = Post.objects.all()
#     category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
#     paginator = Paginator(object_list, 10) # Show 10 posts per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         'post': Post.objects.all(),
#         'category_num': category_num, 
#         'paginator': paginator,
#         'page_obj': page_obj,
#         'object_list' : object_list,
         
#     }
#     return render(request, 'posted/post_list.html', context)


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

# class CategoryListView(ListView):
#     queryset = Category.objects.annotate(
#         num_posts=Count('post', filter=Q(post__is_public=True)))

def category_list(request):
    posts = None
    keyword = None
    category_num = Category.objects.annotate(number_of_post=Count('post')).order_by('timestamp')
    like = 'いいね'
    search = '検索'
    #検索機能の実装
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        categories = Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True)))
    #ページネーションの実装
    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        categories = paginator.page(page)
    except (EmptyPage, InvalidPage):
        categories = paginator.page(paginator.num_pages)
    #追加
    csrf_token = request.GET.get('csrfmiddlewaretoken')
    page_obj = paginator.get_page(page)
    messages.success(request, '「{}」の検索結果'.format(keyword))
    #修正
    context = {
        'keyword': keyword, 
        'categories': categories, 
        'csrf_token': csrf_token,
        'like': like,
        'search': search,
        'page_obj': page_obj,
        'category_num': category_num,
        }

    return render(request, 'posted/category_list.html', context)


class TagListView(ListView):
    # annotate()に集計関数のCount()を引数として渡す
    queryset = Tag.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


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

def mypost_update(request, id):
    post = Post.objects.filter(author=request.user)
    context = {
        'post': post,
    }
    return render(request, 'posted/mypost_update.html', context)


def mypost_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posted:mypost')

    context = {
        'post': post,
    }
    return render(request, 'posted/mypost_delete.html', context)

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