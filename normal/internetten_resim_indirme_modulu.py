import urllib.request
url1="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.abakuskitap.com%2Fblog%2Ficerik%2Fpython-dilinin-bir-anda-populer-olmasinin-5-temel-sebebi&psig=AOvVaw3lFG6JuGZN_hmxuKhkJaLZ&ust=1587751547216000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODjk8-R_-gCFQAAAAAdAAAAABAD"
url2="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.abakuskitap.com%2Fblog%2Ficerik%2Fpython-ile-ne-yapabilirsiniz-pythonin-3-temel-kullanim-alani&psig=AOvVaw3lFG6JuGZN_hmxuKhkJaLZ&ust=1587751547216000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODjk8-R_-gCFQAAAAAdAAAAABAJ"
url3="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fpython-ve-opencv-ile-y%25C3%25BCz-tan%25C4%25B1ma-mennan-sevi%25CC%2587m&psig=AOvVaw3lFG6JuGZN_hmxuKhkJaLZ&ust=1587751547216000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODjk8-R_-gCFQAAAAAdAAAAABAP"

url=[url1,url2,url3]
say=1
for i in url:
    urllib.request.urlretrieve(i,"C:/Users/Acer/Desktop/Resim" + str(say) + ".png")
    say+=1
