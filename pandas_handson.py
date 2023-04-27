#!/usr/bin/env python
# coding: utf-8

# # Pythonで面倒なExcelの仕事を自動化しよう
# # 一瞬で仕事がおわるプログラミング活用術

# Excelでの単純作業を面倒だと感じたことはありませんか？
# 
# 私はプログラミングを覚える前、Excelでの単純作業を毎日繰り返していました。
# 
# 例えば、上司へのレポートを作るため毎日1時間かけて作業をしていました。1年間だと200時間以上です。
# 
# 200時間以上あれば、もっと成果を出せる仕事に集中できたり、早く帰宅して自分のやりたいことに集中できたはずです。
# 
# 皆さんも、そんな単純作業に頭を抱えていませんか？
# 
# Pythonでは、色々なことを自動化することができます。
# 
# したがって、そのExcelでの単純作業は、プログラミングのPythonで自動化できるかもしれません。
# 
# プログラミングを1度書いてしまえば、ほんの一瞬で作業が終わります。

# ## Excelファイルの説明

# まず、このレッスンで使うExcelの説明をします。
# 
# エクセルのファイル名は、sales_mgmt.xlsxです。
# 
# このファイルには、シートが3つあります。
# 
# 予実管理表、売上管理表、発注管理表です。

# ## 具体的なケース

# これらはどのように仕事で使っているのでしょうか？
# 
# 例えば、こういったケースをイメージしてください。
# 
# 複数の店舗を運営しているアパレル会社Aがあったとします。
# 
# 会社Aの発注担当者は、毎日定時に「発注管理表」を確認し、取引先ごとエクセルファイルを分割して、メールで発注しています。
# 
# しかし、この発注業務は、面倒だし、作業時間がかかっています。また、作業ミスが発生してしまうこともありました。
# 
# もし、毎日の発注業務を自動化できたら、毎月どれくらいの時間を減らすことができるでしょうか。
# 
# 例えば、1日1時間かかっているとしたら、月20時間くらいは減らすことができます。
# 
# そうすると、他の業務ができたり、早く帰れたり、有給を取得したりできますね。
# 
# この面倒な作業はすべてPythonにやってもらいましょう。
# 
# Pythonでコーディングし、実際に動作させてみます。

# ## ライブラリのインストール

# はじめに、ライブラリをインストールしていきます。
# 
# ライブラリとはなんでしょうか？
# 
# ライブラリとは、よく使う機能・関数をまとめて、簡単に使えるようにしたものです。
# 
# 例えば、あとから説明するPandasというライブラリには、csvファイルやExcelファイルを読み取るための機能や、データを表にする機能、グラフにする機能など、データ分析の際によく使う機能がまとめられています。
# 
# JupyterLabでライブラリをインストールする場合は、以下のように書きます。
# 
# 「!pip install ラブラリ名」
# 
# また、オフライン環境でインストールする場合は、以下のようにwhlファイルを指定します。
# 
# 「!pip install --no-deps ファイル名」
# 
# 以下のセルを実行して、このレッスンで使用するライブラリをインストールしましょう。

# In[ ]:


# get_ipython().system('pip install --no-deps numpy-1.24.1-cp311-cp311-win_amd64.whl')
# get_ipython().system('pip install --no-deps pandas-1.5.2-cp311-cp311-win_amd64.whl')


# ## データ解析を支援するPandas

# Pandasは、データ解析を支援するための機能を提供するライブラリです。
# 
# Pandasには、PythonでExcelやcsv操作、グラフ化、人工知能の開発で大切なデータの集計や加工などの機能が入っています。
# 
# Pandasで扱うデータ構造としてよく使うもので、「Series」と「Dataframe」があります。
# 
# 1次元のデータを扱うときは「Series」、2次元のデータを扱うときは「Dataframe」を使用します。
# 
# つまり、1列だと「Series」、2列以上だと「Dataframe」です。

# ## ライブラリのインポート

# ライブラリはインストールしただけでは使用できないため、プログラム内でインポートする必要があります。
# 
# インポートの際は「import ライブラリ名」と書きます。
# 
# また、importの際にasを付けると、ライブラリに好きな名前を付けることができます。
# 
# 通例として、pandasはpdと省略します。
# 
# 以下のセルを実行して、このレッスンで使用するライブラリをインポートしましょう。

# In[ ]:


import pandas as pd
import os


# ## ファイルやディレクトリに関する操作を行うos

# osは、WindowsやMacなどのOSが行う操作を、Pythonで行うためのライブラリです。
# 
# Windowsの区切り文字は「\」や「¥」ですが、MacやLinuxでは「/」です。
# こうした環境による違いを吸収して、適切なファイルパスを生成するために使用します。

# ## ファイルパスの設定

# 次に、読み取るエクセルファイルの場所やシート名を、変数に代入していきましょう。
# 
# そうすることにより、後日使う時に、ここだけ編集すれば良いことになり楽です。
# 
# エクセルファイルが置いてある場所を記述しましょう。
# 
# 変数名は、ファイルを取り込む場所という意味で「import_file_path」にします。
# 
# ファイルの場所とファイル名を調べるには、Jupyter Labのサイドバーで表示されているファイルを右クリック。「パスをコピー」をクリックしてペーストすればわかります。
# 
# これをシングルクォーテーションでくくればよいです。
# 
# 次に、シート名を変数に格納します。
# 
# 変数名は、Excelのシート名として、「excel_sheet_name」にします。
# 
# 変数にシート名の「発注管理表」を記述します。
# 
# 次に、取引先ごとに分割したファイルを書き出す場所を記述します。
# 
# 変数名は、出力したファイルを置く場所という意味で「export_file_path」にします。

# In[ ]:


import_file_path = 'sales_mgmt.xlsx'
excel_sheet_name = '発注管理表'
export_file_path = 'output'


# ## Excelファイルを読み込むread_excel関数

# 次に、「pandas」を使って、Excelファイルの内容を読み込みます。
# 
# Excelファイルの内容を読み込むのは、pandasのread_excel関数でできます。
# 
# その読み取ったデータを格納する変数を定義していきましょう。
# 
# read_excel関数を使うと、「Dataframe」というデータ構造で取得するため、「df」とします。
# 
# 次に、アンダースコアを書きます。
# 
# 最後に、発注という意味の「order」を書きます。
# 
# 次に、「pandas」を使って、Excelファイルの内容を読み込む記述を書きます。
# 
# 「import pandas as pd」で「pandas」の名前を「pd」としたため、「pd」と書きます。
# 
# 次に、ドットを書いて、「read_excel」を書きます。
# 
# これが先ほど説明したread_excelで、これでExcelファイルを読み込むことができます。
# 
# 次に、丸括弧を書きます。
# 
# 丸括弧の中には、引数を記述します。
# 
# 例えば、ファイルの場所とファイル名、他には読み取るシート名を記述します。
# 
# まず最初に、ファイルの場所とファイル名を記述しましょう。
# 
# 先ほど「import_file_path」という変数にファイル名と場所を記述したので、この変数を記述。
# 
# 次に、カンマを書いて、シート名を記述します。
# 
# シート名は先ほどexcel_sheet_nameという変数に代入しました。
# 
# sheet_nameという引数にイコールで、excel_sheet_nameを代入しましょう。
# 
# これで、Excelファイルの内容を読み込む記述が完了しました。

# In[ ]:


df_order = pd.read_excel(import_file_path, sheet_name = excel_sheet_name)


# 次に、変数「df_order」を書いて、中身を確認してみます。
# 
# では、実行してみましょう。

# In[ ]:


df_order


# 「発注管理表」シートの内容が読み込まれています。

# ## ユニーク（重複をなくす）するunique関数

# 読み込んだデータの列に会社名があります。
# 
# 会社名には、「株式会社A」と「株式会社A」のように重複する名前があります。
# 
# 重複する名前を除いた会社名一覧を取得してみましょう。
# 
# 会社名一覧という意味の変数「company_name_lists」を定義します。
# 
# 次に、「df_order」を書いて、角括弧を書きます。
# 
# 角括弧の中に、シングルクォーテーションを書いて、列名を書きます。
# 
# 取得したいのは会社名なので、'会社名'を書きます。
# 
# これで、先ほど確認したデータの、「会社名」の列だけを対象とすることができます。
# 
# 次に、カンマを書いて、ユニーク関数（unique()）を書きます。
# 
# これで、重複を除く会社名一覧が取得できました。

# In[ ]:


company_name_lists = df_order['会社名'].unique()


# company_name_listsを書いて、確認してみましょう。

# In[ ]:


company_name_lists


# 重複を除く会社名を取得できました。

# ちなみに、先ほどとデータの構造が違います。
# 
# type関数を使って、データ型を確認してみましょう。

# In[ ]:


type(company_name_lists)


# numpy.ndarrayは、NumPyというライブラリの配列ということになります。

# 比較として、df_orderのデータ型も確認してみましょう。

# In[ ]:


type(df_order)


# DataFrameとなっています。
# 
# つまり、データフレームからユニーク関数を使って列を取得すると、データ型が変わると覚えておきましょう。

# ## ファイル分割

# それでは、会社名ごとのデータに分割してみましょう。
# 
# 試しに、株式会社Aだけのデータを取得してみます。
# 
# df_orderの会社名というカラムの中で、株式会社Aだけ一致するものを取得してみましょう。
# 
# この場合は、df_orderのあとに角括弧。角括弧の中にシングルクオテーション。「会社名」と記述します。
# 
# そして、株式会社Aだけを取得したいので、イコールを2つ書いて株式会社Aとします。
# 
# そうすると、一致する行はTrue、一致しない行はFlaseが配置された、真理値の一覧が返ってきます。

# In[ ]:


df_order['会社名'] == '株式会社A'


# Pandasでは、この真理値一覧をそのままdf_orderの角括弧の中に記述でき、
# Trueに該当する行だけを抽出することができます。
# 
# 実行してみましょう。

# In[ ]:


df_order[df_order['会社名'] == '株式会社A']


# 株式会社Aだけが抽出されました。

# この方法にfor文を組み合わせて、会社名ごとにデータを分割していきましょう。
# 
# まず、「for」と書いて、会社名を1つずつ取り出すための変数「company_name」を書きます。
# 
# 次に、「in」を書い、会社名一覧が保存された「company_name_lists」を書きます。
# 
# 最後に、コロンを書きます。
# 
# こうすることで、先ほど取得したcompany_name_listsの内容が、先頭から順にcompany_nameに代入されていきます。
# 
# printで表示させてみましょう。

# In[ ]:


for company_name in company_name_lists:
    print(company_name)


# 会社名を1つずつ取得できました。

# 次は、for文の中身を書き換えて、会社名ごとに発注データをエクスポートしていきましょう。
# 
# まず、変数を書きます。
# 
# 変数名は、会社ごとの発注として「df_order_company」とします。
# 
# 次に、読み込んだデータを会社ごとに分けます。
# 
# df_orderから、'会社名'の列がcompany_nameと一致する行だけを抽出したいので、
# 
# 角括弧の中にdf_order['会社名'] == company_nameと書きます。
# 
# そしてprint関数を使って、変数の中身をみていきましょう。

# In[ ]:


for company_name in company_name_lists:
    df_order_company = df_order[df_order['会社名'] == company_name]
    print(df_order_company)


# 会社名ごとにデータが分かれていることが確認できます。

# 最後に、会社ごとに分けたデータを、printで画面に表示する代わりに、ファイルに出力します。
# 
# Pandasのデータをエクセルファイルとして出力するためには、to_excelメソッドを使用します。
# 
# 引数には、保存するエクセルファイルの名前を指定します。
# 
# 会社名ごとにファイルを作成したいので、ファイル名にはcompany_nameを使用しましょう。
# 
# パスと結合する際は、OSによって区切り文字が異なる可能性があるため、os.path.joinを使用して、影響を回避しましょう。
# 
# なお、拡張子の.xlsxは単純に文字列を結合するだけで大丈夫です。
# 
# これで記述はおわりです。
# 
# それでは、実行してみましょう。

# In[ ]:


for company_name in company_name_lists:
    df_order_company = df_order[df_order['会社名'] == company_name]
    df_order_company.to_excel(os.path.join(export_file_path, company_name) + '.xlsx')


# ファイルが作成されています。
# 
# ファイルの中身も確認してみましょう。
# 
# 会社ごとのデータが書き込まれています。

# ## Pythonファイルへの変換

# これをpythonファイルに変換して実行をすると、今の作業が1秒で終わります。
# 
# やってみましょう。
# 
# Jupyter Labの「ファイル」メニューから「名前を付けてNotebookをエキスポート...」の中の「実行可能なスクリプト」を選んでクリックします。
# 
# 拡張子が「.py」のプログラムファイルとして出力されるので、Notebookと同じフォルダに配置しましょう。
# 
# プログラムの中身を見ると、このノートブックの内容がそのまま出力されています。
# 
# 「!pip～」の部分が「get_ipython().system(!pip～」と変換されていますが、このままでは実行できないので、コメントアウトしておきましょう。

# In[ ]:


# get_ipython().system('pip install --no-deps numpy-1.24.1-cp311-cp311-win_amd64.whl')
# get_ipython().system('pip install --no-deps pandas-1.5.2-cp311-cp311-win_amd64.whl')


# 先程出力したエクセルファイルを削除して、あらためて出力し直してみましょう。
# 
# 拡張子が「.py」のプログラムファイルは、PythonがインストールされたPCなら、ダブルクリックするだけ実行できます。
# 
# 実行後にoutputフォルダの中身を確認してみましょう。
# 
# 1秒も経たないうちにファイルが作成されましたね。

# ## まとめ

# このように、Pythonで実行すると、圧倒的な業務効率化が可能です。
# 
# また、毎日この作業をするとしたら、毎月どのぐらいの時間が短縮できるのでしょうか。
# 
# 仮に毎日30分かかっているとしたら、月10時間の時間削減です。時給換算すると数万円以上の経費削減です。
# 
# また、ファイル内のデータを手動で選別するわけではないので、間違いが起こりません。
# 
# 間違いがなければ、取引先や上司や同僚にも迷惑がかかりません。
# 
# 今回のレッスンでは紹介しませんが、分割したファイルをメールで送るようにプログラムを組むと、自動的に発注することができます。
# 
# さらに、毎日決まった時間になったら、プログラムを実行するように設定すると、何もしなくても発注できるようになります。
# 
# ファイル分割、メール送信などの作業が1日1時間なら、年間200時間の時間削減です。約1か月分の労働時間になりますね。
# 
# 他にも、Pythonによるエクセル操作の方法はあります。
# 
# ほぼ、できないことはないといっても過言ではないです。
# 
# みなさんもPythonを勉強して、仕事の生産性をあげていきましょう。
