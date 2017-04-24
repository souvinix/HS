class Account(object):
    global Acc_anzahl
    Acc_anzahl = 0
    def __init__(self, name, passwort, level, gold, packs, staub, ep=0, epnextlevel=100):
        global Acc_anzahl
        Acc_anzahl += 1
        self.name = name
        self.passwort = passwort
        self.level = level
        self.gold = gold
        self.packs = packs
        self.staub = staub
        self.ep = ep
        self.epnextlevel = epnextlevel
        
        try:
            if self.level < 1 or self.level > 30:
                del self
                print('Account konnte nicht erstellt werden.\nAufgrund: Level')
        except:
            pass

        try:
            if len(passwort) < 6:
                del self
                print('Account konnte nicht erstellt werden.\nAufgrund: Passwort')
        except:
            pass
            
    def __del__(self):
        global Acc_anzahl
        Acc_anzahl -= 1
        print(self.name,'wurde gelöscht!\n')
        print('Es existieren noch',str(Acc_anzahl),'Accounts.')
        

    def add_item(self, item, anzahl):
        try:
            if item == 'gold':
                self.gold += anzahl
            elif item == 'staub':
                self.staub += anzahl
            elif item == 'packs':
                self.packs += anzahl
        except:
            print(str(item),'gibt es nicht.')

    def buy_item(self, item, anzahl):
        try:
            if item == 'packs':
                preis = 100
                if self.gold < preis * anzahl:
                    print('Nicht genug Gold.')
                elif self.gold >= preis * anzahl:
                    self.gold -= preis * anzahl
                    self.packs += anzahl
                    
        except:
            print(str(item),'gibt es nicht.')

    def change_passwort(self, aktuellesPW, neuesPW):
        if aktuellesPW == self.passwort:
            self.passwort = neuesPW
            print('Passwort erfolgreich geändert!')
        else:
            print('Dies ist nicht dein aktuelles Passwort!')

    def item_configure(self, item, anzahl):
        try:
            if item == 'gold':
                self.gold = anzahl
            elif item == 'staub':
                self.staub = anzahl
            elif item == 'packs':
                self.packs = anzahl
        except:
            print(str(item),'gibt es nicht.')

    def leveldown(self):
        try:
            if self.level <= 1:
                print('Mindest Level erreicht!')
            elif self.level >= 2:
                self.level -= 1
                print('Level wurde auf',str(self.level),'gesetzt.')
                if self.level == 1:
                    self.epnextlevel = 100
                elif self.level == 2:
                    self.epnextlevel = 150
                elif self.level == 3:
                    self.epnextlevel = 200
                elif self.level == 4:
                    self.epnextlevel = 250
                elif self.level == 5:
                    self.epnextlevel = 500
                elif self.level == 6:
                    self.epnextlevel = 600
                elif self.level == 7:
                    self.epnextlevel = 700
                elif self.level == 8:
                    self.epnextlevel = 800
                elif self.level == 9:
                    self.epnextlevel = 900
                elif self.level == 10:
                    self.epnextlevel = 1000
                elif self.level == 11:
                    self.epnextlevel = 1250
                elif self.level == 12:
                    self.epnextlevel = 1500
                elif self.level == 13:
                    self.epnextlevel = 1750
                elif self.level == 14:
                    self.epnextlevel = 2000
                elif self.level == 15:
                    self.epnextlevel = 2500
                elif self.level == 16:
                    self.epnextlevel = 3000
                elif self.level == 17:
                    self.epnextlevel = 3500
                elif self.level == 18:
                    self.epnextlevel = 4000
                elif self.level == 19:
                    self.epnextlevel = 4500
                elif self.level == 20:
                    self.epnextlevel = 5000
                elif self.level == 21:
                    self.epnextlevel = 6000
                elif self.level == 22:
                    self.epnextlevel = 7000
                elif self.level == 23:
                    self.epnextlevel = 8000
                elif self.level == 24:
                    self.epnextlevel = 9000
                elif self.level == 25:
                    self.epnextlevel = 10000
                elif self.level == 26:
                    self.epnextlevel = 10000
                elif self.level == 27:
                    self.epnextlevel = 10000
                elif self.level == 28:
                    self.epnextlevel = 10000
                elif self.level == 29:
                    self.epnextlevel = 10000
                elif self.level == 30:
                    self.epnextlevel = 20000
                
        except:
            print('Fehler beim leveldown.')

    def level_configure(self, anzahl):
        try:
            if anzahl < 1 or anzahl > 30:
                print('Unmöglich!')
            else:
                self.level = anzahl
                print('Level wurde auf',str(self.level),'gesetzt.')
                if self.level == 1:
                    self.epnextlevel = 100
                elif self.level == 2:
                    self.epnextlevel = 150
                elif self.level == 3:
                    self.epnextlevel = 200
                elif self.level == 4:
                    self.epnextlevel = 250
                elif self.level == 5:
                    self.epnextlevel = 500
                elif self.level == 6:
                    self.epnextlevel = 600
                elif self.level == 7:
                    self.epnextlevel = 700
                elif self.level == 8:
                    self.epnextlevel = 800
                elif self.level == 9:
                    self.epnextlevel = 900
                elif self.level == 10:
                    self.epnextlevel = 1000
                elif self.level == 11:
                    self.epnextlevel = 1250
                elif self.level == 12:
                    self.epnextlevel = 1500
                elif self.level == 13:
                    self.epnextlevel = 1750
                elif self.level == 14:
                    self.epnextlevel = 2000
                elif self.level == 15:
                    self.epnextlevel = 2500
                elif self.level == 16:
                    self.epnextlevel = 3000
                elif self.level == 17:
                    self.epnextlevel = 3500
                elif self.level == 18:
                    self.epnextlevel = 4000
                elif self.level == 19:
                    self.epnextlevel = 4500
                elif self.level == 20:
                    self.epnextlevel = 5000
                elif self.level == 21:
                    self.epnextlevel = 6000
                elif self.level == 22:
                    self.epnextlevel = 7000
                elif self.level == 23:
                    self.epnextlevel = 8000
                elif self.level == 24:
                    self.epnextlevel = 9000
                elif self.level == 25:
                    self.epnextlevel = 10000
                elif self.level == 26:
                    self.epnextlevel = 10000
                elif self.level == 27:
                    self.epnextlevel = 10000
                elif self.level == 28:
                    self.epnextlevel = 10000
                elif self.level == 29:
                    self.epnextlevel = 10000
                elif self.level == 30:
                    self.epnextlevel = 20000

        except:
            print('Fehler')

    def levelup(self):
        try:
            if self.level >= 30:
                print('Maximales Level erreicht!')
            else:
                self.level += 1
                if self.level == 1:
                    self.epnextlevel = 100
                elif self.level == 2:
                    self.epnextlevel = 150
                elif self.level == 3:
                    self.epnextlevel = 200
                elif self.level == 4:
                    self.epnextlevel = 250
                elif self.level == 5:
                    self.epnextlevel = 500
                elif self.level == 6:
                    self.epnextlevel = 600
                elif self.level == 7:
                    self.epnextlevel = 700
                elif self.level == 8:
                    self.epnextlevel = 800
                elif self.level == 9:
                    self.epnextlevel = 900
                elif self.level == 10:
                    self.epnextlevel = 1000
                elif self.level == 11:
                    self.epnextlevel = 1250
                elif self.level == 12:
                    self.epnextlevel = 1500
                elif self.level == 13:
                    self.epnextlevel = 1750
                elif self.level == 14:
                    self.epnextlevel = 2000
                elif self.level == 15:
                    self.epnextlevel = 2500
                elif self.level == 16:
                    self.epnextlevel = 3000
                elif self.level == 17:
                    self.epnextlevel = 3500
                elif self.level == 18:
                    self.epnextlevel = 4000
                elif self.level == 19:
                    self.epnextlevel = 4500
                elif self.level == 20:
                    self.epnextlevel = 5000
                elif self.level == 21:
                    self.epnextlevel = 6000
                elif self.level == 22:
                    self.epnextlevel = 7000
                elif self.level == 23:
                    self.epnextlevel = 8000
                elif self.level == 24:
                    self.epnextlevel = 9000
                elif self.level == 25:
                    self.epnextlevel = 10000
                elif self.level == 26:
                    self.epnextlevel = 10000
                elif self.level == 27:
                    self.epnextlevel = 10000
                elif self.level == 28:
                    self.epnextlevel = 10000
                elif self.level == 29:
                    self.epnextlevel = 10000
                elif self.level == 30:
                    self.epnextlevel = 20000
                print('Level:',str(self.level),'wurde erreicht!')
                
        except:
            print('Fehler beim levelup.')
            

    def get_ep(self, anzahl):
        self.ep += anzahl
        if self.ep < self.epnextlevel:
            pass

        elif self.ep >= self.epnextlevel:
            while self.ep >= self.epnextlevel:
                self.ep -= self.epnextlevel
                self.levelup()

    
            
                    
                
            
