class Produkt(object):
    'Produkter i HayDay'
    
    def __init__(self, fpris, ingredienser,tid,kostnad):
        self.fpris = fpris
        self.ingredienser = ingredienser
        self.tid = tid
        self.kostnad = kostnad
        
    def totalpris(self):
        totalkostnad = self.fpris - self.kostnad
        if self.ingredienser is None:
            return totalkostnad
        else:
            for ingr in self.ingredienser:
            
                totalkostnad = totalkostnad - my_dicts[ingr].totalpris()
                 
            return totalkostnad
    
    def totaltid(self):
        totaltid = self.tid
        if self.ingredienser is not None:
            for ingr in self.ingredienser:
                totaltid = totaltid + my_dicts[ingr].totaltid()
        return totaltid
        
    def effektivitetsfaktor(self):
        vinst = self.totalpris()
        tid = self.totaltid()
        effektivitetsfaktor = float(vinst)/float(tid)
        return effektivitetsfaktor
        
KGlass = Produkt(352,["Sirap","KJos"],180,0)
KJos = Produkt(216,["KBar","KBar"],150,0)
Mjolk = Produkt(32,["KoFoder"],60,0)
KoFoder = Produkt(14,["Soya","Soya","Majs"],10,0)
Soya = Produkt(10,None,20,0)
Majs = Produkt(7,None,5,0)
Sirap = Produkt(90,["Socker","Socker","Socker","Socker"],90,0)
Socker = Produkt(14,None,30,0)
KBar = Produkt(68,None,125,32)
Vete = Produkt(3,None,2,0)
Agg = Produkt(18,["HFoder"],20,0)
HFoder = Produkt(7,["Majs","Vete","Vete"],5,0)
Brod = Produkt(21,["Vete","Vete","Vete"],5,0)
Gradde = Produkt(50,["Mjolk"],20,0)
MajsBrod = Produkt(72,["Majs","Majs","Agg","Agg"],30,0)
BrunSocker = Produkt(32,["Socker"],20,0)
Popcorn = Produkt(32,["Majs","Majs"],30,0)
Morot = Produkt(7,None,10,0)
Smor = Produkt(82,["Mjolk","Mjolk"],30,0)
Pannkakor = Produkt(108,["BrunSocker","Agg","Agg","Agg"],30,0)
GFoder = Produkt(50,["Morot","Morot","Soya"],20,0)
Bacon = Produkt(50,["GFoder"],240,0)
Kakor = Produkt(104,["BrunSocker","Agg","Agg","Vete","Vete"],60,0)
BaconAAgg = Produkt(201,["Bacon","Bacon","Agg","Agg","Agg","Agg"],60,0)
Ost = Produkt(122,["Mjolk","Mjolk","Mjolk"],60,0)
Indigo = Produkt(25,None,120,0)
VitSocker = Produkt(50,["Socker","Socker"],40,0)
MorotsPaj = Produkt(82,["Agg","Morot","Morot","Morot","Vete","Vete"],60,0)
Pumpa = Produkt(32,None,180,0)
PumpaPaj = Produkt(158,["Agg","Pumpa","Pumpa","Pumpa","Vete","Vete"],120,0)

my_dicts = {"KGlass":KGlass, "KJos":KJos, "Mjolk":Mjolk, "KoFoder":KoFoder, "Soya":Soya, "Majs":Majs, "Sirap":Sirap, "Socker":Socker, "KBar":KBar, "Vete":Vete, "Agg":Agg, "HFoder":HFoder, "Brod":Brod, "Gradde":Gradde, "MajsBrod":MajsBrod, "BrunSocker":BrunSocker, "Popcorn":Popcorn, "Morot":Morot, "Smor":Smor, "Pannkakor":Pannkakor, "GFoder":GFoder, "Bacon":Bacon, "Kakor":Kakor, "BaconAAgg":BaconAAgg, "Ost":Ost, "VitSocker":VitSocker, "MorotsPaj":MorotsPaj, "Pumpa":Pumpa, "PumpaPaj":PumpaPaj}
for i in my_dicts.iterkeys():
    print i ,"    \t"," vinst ", my_dicts[i].totalpris(), "\t"," tid ", my_dicts[i].totaltid(), "\t" , " effektivitet ", my_dicts[i].effektivitetsfaktor()
                
            
