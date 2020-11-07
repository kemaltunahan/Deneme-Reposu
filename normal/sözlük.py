import operator
d = "/"
a = dict({"Ad" : "Kemal"  , "Yaş" : "20" , "Soyad" : "Bingöl"})

for i,b in sorted(a.items(), key = operator.itemgetter(0)):
    print(i + ":",b)

print(d.join(sorted(a)))