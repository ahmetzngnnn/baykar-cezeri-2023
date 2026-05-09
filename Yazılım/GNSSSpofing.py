import cezeri
import math

def GNSSSpofing():
        
    sayac=0
    en_kucuk_irtifa=130
    en_buyuk_irtifa=110
    while sayac<100 :
        if cezeri.gnss.irtifa<=en_kucuk_irtifa :
            en_kucuk_irtifa=cezeri.gnss.irtifa
        if cezeri.gnss.irtifa>=en_buyuk_irtifa :
            en_buyuk_irtifa=cezeri.gnss.irtifa
        sayac=sayac+1
    while en_kucuk_irtifa<=120.0 or en_buyuk_irtifa>=130 :
        cezeri.ileri_git(cezeri.yavas)
        inis_kontrol=cezeri.yerel_harita[4]
        if inis_kontrol.inis_bolgesi :
            cezeri.dur()
            cezeri.bekle(1)
            break