class Account(object):
    global Acc_anzahl
    Acc_anzahl = 0
    def __init__(self, name, passwort, level, gold, packs, staub, ep=0):
        global Acc_anzahl
        Acc_anzahl += 1
        self.name = name
        self.passwort = passwort
        self.level = level
        self.gold = gold
        self.packs = packs
        self.staub = staub
        self.ep = ep

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

    def levelup(self):
        try:
            if self.level >= 30:
                print('Maximales Level erreicht!')
            elif self.level < 30:
                self.level += 1
                
        except:
            print('Fehler beim levelup.')

    def leveldown(self):
        try:
            if self.level <= 1:
                print('Mindest Level erreicht!')
            elif self.level >= 2:
                self.level -= 1
                
        except:
            print('Fehler beim leveldown.')

    def level_configure(self, anzahl):
        try:
            if anzahl < 1 or anzahl > 30:
                print('Unmöglich!')
            elif not anzahl < 1 or not anzahl > 30:
                self.level == anzahl

        except:
            print('Fehler')

    def get_ep(self, anzahl):
        if self.level == 1:
            pass
        
    
            
                    
                
            
