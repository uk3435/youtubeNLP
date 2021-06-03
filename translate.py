from langdetect import detect_langs
import bert_sentiment

def ayir(text):

    deger=text.split(":")
    return deger[1]

def dilSonucu(text):

    sonuc=text.split(":")
    return sonuc[0]

NihaiSonuc=""

with open("y3.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f]
    for text in lines:
        print(text)
        olasiliklar=detect_langs(text)
        
        
        if len(olasiliklar)>1 :
            
            o1=float(ayir(str(olasiliklar[0])))
            o2=float(ayir(str(olasiliklar[1])))
          
            if o1 >= 0.8 and o2 < 0.2:
                NihaiSonuc=dilSonucu(str(olasiliklar[0]))
                if NihaiSonuc=="tr":
                    print(NihaiSonuc)
                    bert_sentiment.analizEt(text)
                if NihaiSonuc=="en":
                    print("İngilizce algoritmaya")
            if o2 >= 0.8 and o1 < 0.2:
                NihaiSonuc=dilSonucu(str(olasiliklar[1]))
                if NihaiSonuc=="tr":
                    print(NihaiSonuc)
                    bert_sentiment.analizEt(text)
                if NihaiSonuc=="en":
                    print("İngilizce algoritmaya")

            if o1<0.8 and o2 >=0.2:
                print("Tahmin Edemedi")
            if o2<0.8 and o1 >=0.2:
                print("Tahmin Edemedi")
                
    
        else:

            o1=ayir(str(olasiliklar[0]))
            print(o1)
            NihaiSonuc=dilSonucu(str(olasiliklar[0]))
            if NihaiSonuc=="tr":

                print(NihaiSonuc)
                bert_sentiment.analizEt(text)
            if NihaiSonuc=="en":
                    print("İngilizce algoritmaya")
        print(detect_langs(text))
        
