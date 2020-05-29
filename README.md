# IdeaGenerator

開発手順
ローカル環境で開発し、デプロイをHerokuで行う。


（１）ローカル環境のセッティング
１、 .gitignore
local_settings.py をコメントアウト

２、 pip install 後、　pip freeze > requirements.txt を必ず実行

3、 python manage.py runserver

４、　編集後
git add .
git commit -m 'modify'
git push origin branch_name


（２）heroku deploy
１、　manage.py ファイル
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local_settings')
⇩
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

２、 .gitignore ファイル
local_settings.py のコメントアウトを元に戻す

３、push する
git add .
git commit -m 'ryo/kei heroku deploy'
git push heroku master
