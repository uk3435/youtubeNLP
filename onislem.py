
with open("y1.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f]
    liste=[]
    liste1=[]
    count=0
    f = open("y3.txt", "a", encoding="utf-8")
    for text in lines:
        liste.append(count)
        liste1.append(text)
       
        if "REPLY" in text:
            #print("OK")
            
            #print(liste[count-1])
            if liste1[int(liste[count-5])]=="REPLY":

                print(liste1[int(liste[count-2])])
                f.write(liste1[int(liste[count-2])]+"\n")
               
                #print(text)

            if  liste1[int(liste[count-6])]=="REPLY":
                print(liste1[int(liste[count-3])] + liste1[int(liste[count-2])])
                f.write(liste1[int(liste[count-3])] + liste1[int(liste[count-2])]+"\n")
              

            
            if  liste1[int(liste[count-4])]=="REPLY":
                print(liste1[int(liste[count-1])])
                f.write(liste1[int(liste[count-1])]+"\n")
               


        count=count+1
    f.close()
