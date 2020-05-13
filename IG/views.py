
from django.shortcuts import render
from datetime import datetime
from . import forms





def hello_get_query(request):
    d = {
        'test1':request.GET.get('test1'),
        'test2':request.GET.get('test2'),
        'test3':request.GET.get('test3'),
    }
    return render(request, 'IG/form.html', d)

def bulletin_board(request):
    d = {}
    return render(request, 'IG/bulletin_board.html', d)


def category_create(request):
    d = {}
    return render(request, 'IG/category_create.html', d)

### template views ###

def index(request):
    Tech_li = {'tech0': 'AR', 'tech1': 'VR', 'tech2': 'AI', 'tech3': 'IoT', 'tech4': '5G', 'tech5': '6G', 'tech6': '7G', 'tech7': 'CG', 'tech8': 'スマートスピーカー', 'tech9': '3dプリンタ', 'tech10': 'ブロックチェーン', 'tech11': '自動運転', 'tech12': '言語翻訳'}
    Agri_li = {'agri0': '水耕栽培', 'agri1': '地中海式農業', 'agri2': '畜産', 'agri3': '酪農', 'agri4': '園芸農業', 'agri5': '混合農業', 'agri6': 'プランテーション', 'agri7': '遊牧', 'agri8': '焼畑', 'agri9': '耕作', 'agri10': '有機栽培', 'agri11': '自然農法', 'agri12': '無農薬', 'agri13': 'バイオダイナミック農法', 'agri14': '植物工場'}
    Web_service_li = {'web0': '情報検索機能', 'web1': '情報自動所得', 'web2': 'EC', 'web3': 'web会議', 'web4': 'データベース', 'web5': 'クラウド', 'web6': 'SNS', 'web7': 'メディア'}
    AI_li = {'AI0': '迷惑メールフィルタ', 'AI1': '音声認識', 'AI2': 'レコメンデーション', 'AI3': '会話bot', 'AI4': '音声合成', 'AI5': '自動運転車', 'AI6': '感情推定', 'AI7': '画像認識', 'AI8': '画像変換'}
    Religion_li = {'religion0': 'ユダヤ教', 'religion1': 'キリスト教系', 'religion2': 'キリスト教', 'religion3': 'キリスト教系新宗教', 'religion4': 'イスラーム', 'religion5': 'インド宗教', 'religion6': 'ヒンドゥー教', 'religion7': 'インドの自由思想家', 'religion8': 'ジャイナ教', 'religion9': 'シク教', 'religion10': 'ゾロアスター教', 'religion11': '仏教', 'religion12': 'インド仏教', 'religion13': '南伝仏教', 'religion14': '北伝仏教'}
    Feeling_li = {'feeling0': '触覚', 'feeling1': '味覚', 'feeling2': '嗅覚', 'feeling3': '視覚', 'feeling4': '聴覚'}
    d = {
        'tech': Tech_li,
        'agri': Agri_li,
        'web': Web_service_li,
        'AI': AI_li,
        'religion': Religion_li,
        'feeling': Feeling_li,
        'form': forms.NumberForm(),

    }
    return render(request, 'templates/index.html', d)

def about(request):
    d = {}
    return render(request, 'templates/about.html', d)

def blog(request):
    d = {}
    return render(request, 'templates/blog.html', d)

def blog_details(request):
    d = {}
    return render(request, 'templates/blog_details.html', d)

def contact(request):
    d = {}
    return render(request, 'templates/contact.html', d)

def listing(request):
    d = {}
    return render(request, 'templates/listing.html', d)

def listing_details(request):
    d = {}
    return render(request, 'templates/listing_details.html', d)
