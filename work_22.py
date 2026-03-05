#17misol
#son=int(input())
#birlik=son%10
#onlik=son//10*10
#match onlik:
#   case 10:
#        print("on")
#    case 20:
#       print("yigirma")
#    case 30:
#       print("o'ttiz")
#    case 40:
#       print("qirq")
#match birlik:
#    case 1:
#        print("bir")
#    case 2:
#       print("ikki")
#    case 3:
#       print("uch")
#    case 4:
#       print("to'rt")
#    case 5:
#       print("besh")
#    case 6:
#        print("olti")
#    case 7:
#       print("yetti")
#    case 8:
#        print("sakkiz")
#    case 9:
#        print("to'qiz")
#        print(onlik+birlik)

#18-misol
#son=int(input("son="))
#birlik=son//10
#onlik=son//10%10*10
#yuzlik=son//100*100
#match yuzlik:
#    case 1:
#       print('bir yuz')
 #   case 2:
 #       print("ikki yuz")
 #   case 3 :
 #       print("uch yuz")
 #   case 4:
 #       print("to`rt yuz")
 #   case 5:
 #       print("besh yuz")
 #   case 6:  
 #       print("olti  yuz")
 #   case 7:
 #       print("yetti yuz")
 #   case 8:
 #       print("sakkiz yuz")
 #   case 9:
#      print("to`qqiz yuz")
#match onlik:
#    case 10:
#        print('o`n ')
#    case 20:
#        print("yigirma ")
#    case 30 :
#        print("o`ttiz ")
#    case 40:
#        print("qirq")
#    case 50:
#        print("ellik")
#    case 60:  
#        print("oltmish")
#    case 70:
#        print("yetmish")
#    case 80:
#        print("sakson")
#    case 90:
#       print("to`qson")    
#match birlik:
#   case 100:
#       print('bir')
#   case 200:
#        print("ikki")
#    case 300 :
#       print("uch")
#   case 400:
#       print("to`rt")
#   case 500:
#       print("besh")
 #   case 6:  
 #       print("olti")
#    case 700:
#        print("yetti")
#    case 800:
#        print("sakkiz")
#    case 900:
#        print("to`qqiz")
#        print(yuzlik+onlik+birlik)

#19-misol
#yil=int(input("yilni kiriting="))
#a=1984
#rang=((yil - a) // 12)+1
#qiymat=(yil-a) % 12 
#match rang:
#    case 1:
#        print("Yashil")
#    case 2:
#        print("Qizil")
#   case 3:
#       print("Sariq")
#   case 4:
 #       print("Oq")
#    case 5:
#        print("qora")
#match qiymat:
#    case 1:
#        print("sichqon yili")
#    case 2:
#        print("Sigir yili")
#    case 3:
#        print("Yo'lbars yili")
#    case 4:
#        print("Quyon yili")
#    case 5:
#        print("Ajdar yili")
#    case 6:
#        print("Ilon yili")
#    case 7:
#        print("Ot yili")
#    case 8:
#        print("Qo'y yili")
#    case 9:
#        print("Maymun yili")
#    case 10:
#        print("Tovuq yili")
#    case 11:
#        print("It yili")
#    case 12:
#        print("To'ng'iz yili")

#20-misol
#D = int(input("Kunini kiriting: "))
#M = int(input("Oyni kiriting: "))
#match M:
#    case 1:
#        print("Qovg'a" if D >= 20 else "Echki")
#    case 2:
#        print("Baliq" if D >= 19 else "Qovg'a")
#    case 3:
#        print("Qo'y" if D >= 21 else "Baliq")
#    case 4:
#        print("Buzoq" if D >= 20 else "Qo'y")
#    case 5:
#        print("Egizaklar" if D >= 21 else "Buzoq")
#    case 6:
#        print("Qisqichbaqa" if D >= 22 else "Egizaklar")
#    case 7:
#        print("Arslon" if D >= 23 else "Qisqichbaqa")
#    case 8:
#        print("Parizod" if D >= 23 else "Arslon")
#    case 9:
#        print("Tarozi" if D >= 23 else "Parizod")
#    case 10:
#        print("Chayon" if D >= 23 else "Tarozi")
#    case 11:
#        print("O‘qotar" if D >= 23 else "Chayon")
#    case 12:
#        print("Echki" if D >= 22 else "O‘qotar")
#    case _:
#        print("Noto‘g‘ri oy kiritildi")

