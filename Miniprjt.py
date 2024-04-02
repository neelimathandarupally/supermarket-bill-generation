from datetime import datetime
name=input("Enter the name:")
#list of items
list='''
"Rice"           50/kg
"Chilli Powder"  60/kg
"Salt"           20/kg
"Oil"            90/lt
"Masala"         30/pk
"Biscults"       90/pk
"panner"         100/kg
"Chocolates"     50/pk
"Jeera"          100/kg
"flour"          30/kg
'''
#Declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
plist=[]
qlist=[]
items={'Rice':50,'Chilli Powder':60,'Salt':20,'Oil':90,'Masala':30,'Biscults':90,'panner':100,'Chocolates':50,'Jeera':100,'flour':30}
option=int(input("Enter the list of items press1:"))
if option==1:
    print(list)
    for i in range(len(items)):
        input1=int(input("If you want to buy press1: or 2 for exit:"))
        if input1==2:
            break
        if input1==1:
            item=input("enter the items:")
            quantity=int(input("enter the quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
            else:
                print("sorry you entered item is not available")
        else:
            print("entered wrong pin")
        inp=input("can i bill the items yes or no:")
        if inp=='yes':
            pass
        if finalamount!=0:
            print(25*"= ","Junnu supermarket",25*"=")
            print(28*" ","Nalgonda")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*'  ',5*'  ',ilist[i],3*'  ',qlist[i],8*"" ,plist[i])                                                                                                                                                                                                                                                                                           
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*"  ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")
            # for i in range(len(pricelist)):
            #     print(i,ilist[i],qlist[i],plist[i])


