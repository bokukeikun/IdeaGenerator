
from django.shortcuts import render
from datetime import datetime
from . import forms



def idea_generator(request):
    import random
    import os

    Tech_li = ['AR', 'VR', 'AI', 'IoT', '5G', '6G', '7G', 'CG', 
            'スマートスピーカー', '3dプリンタ', 'ブロックチェーン', 
            '自動運転', '言語翻訳']

    Category_li = ['農業', 'インフラ', 'エネルギー', '医療', '健康',
                '介護' '自動車', '建築', '金融', '物流', '流通', '防犯', 
                '防災', '教育',  '飲食', '林業', 'テクノロジー', '感覚']

    Agri_li = ['水耕栽培', '地中海式農業', '畜産',  '酪農', '園芸農業', 
            '混合農業', 'プランテーション', '遊牧', '焼畑', '耕作', 
            '有機栽培', '自然農法', '無農薬', 'バイオダイナミック農法', 
            '植物工場']

    Web_service_li = ['情報検索機能', '情報自動所得', 'EC', 'web会議', 
                    'データベース', 'クラウド', 'SNS', 'メディア']

    AI_li = ['迷惑メールフィルタ', '音声認識', 'レコメンデーション', '会話bot', 
            '音声合成', '自動運転車', '感情推定', '画像認識', '画像変換']

    Religion_li = ['ユダヤ教', 'キリスト教系', 'キリスト教', 'キリスト教系新宗教', 
                'イスラーム', 'インド宗教', 'ヒンドゥー教', 'インドの自由思想家', 
                'ジャイナ教', 'シク教', 'ゾロアスター教', '仏教', 'インド仏教', 
                '南伝仏教', '北伝仏教', '西アジアの宗教', '中央アジアの宗教', 
                '東アジアの宗教', '精神修養', '土着宗教など', 'ネオペイガニズム', 
                'アフロ・クレオール宗教', 'サタニズム系', '秘教', '神秘主義', 
                    'パロディー宗教', '非宗教、反宗教、メタ宗教']

    Feeling_li = ['触覚', '味覚', '嗅覚', '視覚', '聴覚']


    Tech_li = {'tech0': 'AR', 'tech1': 'VR', 'tech2': 'AI', 'tech3': 'IoT', 'tech4': '5G', 'tech5': '6G', 'tech6': '7G', 'tech7': 'CG', 'tech8': 'スマートスピーカー', 'tech9': '3dプリンタ', 'tech10': 'ブロックチェーン', 'tech11': '自動運転', 'tech12': '言語翻訳'}
    Agri_li = {'agri0': '水耕栽培', 'agri1': '地中海式農業', 'agri2': '畜産', 'agri3': '酪農', 'agri4': '園芸農業', 'agri5': '混合農業', 'agri6': 'プランテーション', 'agri7': '遊牧', 'agri8': '焼畑', 'agri9': '耕作', 'agri10': '有機栽培', 'agri11': '自然農法', 'agri12': '無農薬', 'agri13': 'バイオダイナミック農法', 'agri14': '植物工場'}
    Web_service_li = {'web0': '情報検索機能', 'web1': '情報自動所得', 'web2': 'EC', 'web3': 'web会議', 'web4': 'データベース', 'web5': 'クラウド', 'web6': 'SNS', 'web7': 'メディア'}
    AI_li = {'AI0': '迷惑メールフィルタ', 'AI1': '音声認識', 'AI2': 'レコメンデーション', 'AI3': '会話bot', 'AI4': '音声合成', 'AI5': '自動運転車', 'AI6': '感情推定', 'AI7': '画像認識', 'AI8': '画像変換'}
    Religion_li = {'religion0': 'ユダヤ教', 'religion1': 'キリスト教系', 'religion2': 'キリスト教', 'religion3': 'キリスト教系新宗教', 'religion4': 'イスラーム', 'religion5': 'インド宗教', 'religion6': 'ヒンドゥー教', 'religion7': 'インドの自由思想家', 'religion8': 'ジャイナ教', 'religion9': 'シク教', 'religion10': 'ゾロアスター教', 'religion11': '仏教', 'religion12': 'インド仏教', 'religion13': '南伝仏教', 'religion14': '北伝仏教'}
    Feeling_li = {'feeling0': '触覚', 'feeling1': '味覚', 'feeling2': '嗅覚', 'feeling3': '視覚', 'feeling4': '聴覚'}
    a = request.GET.get('test1')
    b = request.GET.get('test2')
    c = request.GET.get('test3')
    number = request.GET.get('number')
    Comb = [None,None,None,None,None,None,None,None,None,None]
    

    

    categories = {'tech': Tech_li, 'agri': Agri_li, 'feeling': Feeling_li,
     'web':Web_service_li, 'AI': AI_li, 'religion': Religion_li}

    for x in range(int(number)):
        a_out = None
        b_out = None
        c_out = None

        for category, value in categories.items():
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

        for i in range(len(Tech_li)):
            for key, value in Tech_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value

        for i in range(len(Agri_li)):
            for key, value in Agri_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value

        for i in range(len(Web_service_li)):
            for key, value in Web_service_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value

        for i in range(len(AI_li)):
            for key, value in AI_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value

        for i in range(len(Religion_li)):
            for key, value in Religion_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value

        for i in range(len(Feeling_li)):
            for key, value in Feeling_li.items():
                if key == a:
                    a_out = value
                elif key == b:
                    b_out = value
                elif key == c:
                    c_out = value
        
        if (a_out is not None) and (b_out is not None) and (c_out is not None):
            Comb[x] = a_out + "　×　" + b_out + "　×　" + c_out  

    text0 = Comb[0]
    text1 = Comb[1]
    text2 = Comb[2]
    text3 = Comb[3]
    text4 = Comb[4]
    text5 = Comb[5]
    text6 = Comb[6]
    text7 = Comb[7]
    text8 = Comb[8]
    text9 = Comb[9]

    context = {
        'a': a_out,
        'b': b_out,
        'c': c_out,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'text6': text6,
        'text7': text7,
        'text8': text8,
        'text9': text9,
    }
    return render(request, 'posted/post_form.html', context)

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
