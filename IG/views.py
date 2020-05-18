
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
    
    # Sience_li = {'phisi': '物理', 'medi': '医学', 'chemi': '化学', 'tech1_': 'テクノロジー１', 'tech2_': 'テクノロジー２',}
    # Envi_li = {'energy': 'エネルギー', 'nature': '自然', 'agri': '農業', 'space': '宇宙'}
    # Society_li = {'buisiness': 'ビジネス', 'infra': 'インフラ', 'poli': '政治', 'nation': '国', 'inst1_': '施設１', 'inst2_': '施設２',}
    # Culture_li = {'edu': '教育', 'cust': '習慣', 'art': '芸術', 'life': '生活・暮らし'}
    # Human_li = { 'sense': '五感', 'feeling': '感情', 'bp': '体のパーツ'}
    
    d = {
        'phisi': Phisi_li, 
        'medi': Medi_li, 
        'chemi': Chemi_li, 
        'tech1_': Tech1_li, 
        'tech2_': Tech2_li, 

        'energy': Energy_li, 
        'nature': Nature_li, 
        'agri': Agri_li, 
        'space': Space_li, 

        'buisiness': Buisiness_li, 
        'infra': Infra_li, 
        'poli': Poli_li, 
        'nation': Nation_li, 
        'inst1_': Inst1_li, 
        'inst2_': Inst2_li, 

        'edu': Edu_li, 
        'cust': Cust_li, 
        'art': Art_li, 
        'life': Life_li, 

        'sense': Sense_li, 
        'feeling': Feeling_li, 
        'bp': BP_li,
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
