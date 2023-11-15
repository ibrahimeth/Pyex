import numpy as np
import pandas as pn

df = pn.read_csv("USvideos.csv")

# ilk on kaydı getiriniz
res = df.head(10)
# ikinci 5 kaydı getiriniz
res = df[5:11].head()
# datasetde bulunan kolon isilerini ve sayısını bulunuz.
res = df.columns
res = len(df.columns)
# beğenme() like ve beğenmeme (dislike) sayılarının ortalamaalırnı bulun
res = df["likes"].mean()
res = df["likes"].mean()
# ilk 50 like ve dslike kolonlarını getiriniz
res = df[["title","likes","dislikes"]].head(50)
# en çok görüntülenen video hangisidir .
res = df[df["views"].max() == df["views"]]
# en düşük görüntülenen video hangisidir?
res = df[df["views"].min() == df["views"]]

# en fazla görütülenen ilik 10 kaydı getr.

# kategoriye göre beğeni ortalamaalarını sıraya göre getirsin 
res = df.groupby("category_id").mean().sort_values("likes")["likes"]
# kategoriye göre yorum sayılarını yukarıdan aşağı sıralayınız 
res = df.groupby("category_id").sum()
# her kategoride kaç video vardır 

# her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

# Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

# En popüler videoları listelyiniz ( Like / dislike oranına göre)


print(res)