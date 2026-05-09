# içe aktar readme.md
#-“hedefyon” fonksiyonu X ve Y olarak 
#yollanan koordinattan tgtX ve tgtY olarak 
#yollanan koordinata olan yönü arctangent2 
#fonksiyonu kullanarak bulur.

#-“hedefyon” fonksiyonu bulduğu yönü
#dereceye çevirir ve bu değeri döndürür.

#-“hedefmesafe” fonksiyonu X ve Y olarak
#yollanan koordinattan tgtX ve tgtY olarak
#yollanan koordinata olan mesafeyi hesaplar.
#Bu değeri döndürür.



import math
def hedefyon(X,Y,tgtX,tgtY):
    yon=math.degrees(math.atan2(tgtY-Y,tgtX-X))
    return yon
def hedefmesafe(X,Y,tgtX,tgtY):
    mesafe=math.sqrt((tgtX-X)**2+(tgtY-Y)**2)
    return mesafe
print(hedefyon(0,0,1,1))
print(hedefmesafe(0,0,1,1))


#NAV isminde, içinde enlem ve boylam 
#değerleri bulunan class oluşturulur. “nav” 
#ve “target” adında iki değişken bu class 
#yapısında oluşturulur.-Aracın enlem ve boylamı “Cenlem” ve 
#“Cboylam” değişkenlerine atanır. Aracın 
#yön değeri, “yon” değişkenine atanır. 

class NAV:
    def __init__(self,Cenlem,Cboylam):
        self.nav=(Cenlem,Cboylam)
        self.target=(0,0)
        self.yon=0
    def hedef(self,tgtX,tgtY):
        self.target=(tgtX,tgtY)
        self.yon=hedefyon(self.nav[0],self.nav[1],tgtX,tgtY)
    def hedefbilgi(self):
        print("Hedef Enlem:",self.target[0],"Hedef Boylam:",self.target[1],"Hedef Yön:",self.yon)
    def hedefmesafe(self):
        return hedefmesafe(self.nav[0],self.nav[1],self.target[0],self.target[1])
nav=NAV(39.925533,32.866287)
nav.hedef(39.925533,32.866287)
nav.hedefbilgi()
print(nav.hedefmesafe())

#Path: ikinokta.py
