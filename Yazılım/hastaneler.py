import math
cezeri = ...  # Define the missing variable or import the necessary module
en_kucuk_hipotenus = 100
for hastane_bolge in cezeri.harita.hastaneler:
    yatay = hastane_bolge.enlem - cezeri.gnss.enlem
    dikey = hastane_bolge.boylam - cezeri.gnss.boylam
    hipotenus = math.sqrt((yatay ** 2) + (dikey ** 2))
    if hipotenus <= en_kucuk_hipotenus:
        en_kucuk_hipotenus = hipotenus
        secilen_hastane = hastane_bolge
