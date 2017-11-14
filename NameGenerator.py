import random
import itertools

nm1 = ["Abbas","Afshin","Ahmad","Akbar","Ali","Ali Reza","Amin","Amir","Amir Ali","Amir Hossein","Amir Mohammad","Amir Reza",
       "Anooshirvan","Arash","Aref","Arman","Arsalan","Arzhang","Asghar","Aziz","Babak","Bagher","Bahman","Bahram","Bairam",
       "Behnam","Behrad","Behrouz","Behzad","Benyamin","Bijan","Borzou","Changiz","Dariush","Davoud","Ebrahim","Ehsan","Enayat",
       "Erfan","Esfandiyar","Esmaeel","Faramarz","Farhad","Fariborz","Farid","Farrokh","Farzad","Farzin","Fazel","Ferdous",
       "Firooz","Freydoun","Habib","Hadi","Hamed","Hamid","Hamidreza","Hashem","Hassan","Hesam","Heshmat","Heydar","Homayoun",
       "Hooman","Hossein","Houshang","Iraj","Jaffar","Jahangir","Jallal","Jamshid","Javad","Kambiz","Kamran","Kamyar","Kannan",
       "Karim","Kaveh","Kazem","Keyhan","Keykavous","Khashayar","Khosrow","Kioumars","Kooroush","Latif","Mahdi","Mahyar","Majid",
       "Mamad","Mani","Manouchehr","Mansour","Mazyar","Mehdi","Mehran","Mehrdad","Meysam","Milad","Moein","Mohammad Ali","Mohammad Reza",
       "Mohsen","Mojtaba","Morteza","Mostafa","Nader","Naghi","Naser","Nima","Nouzar","Nozar","Omid","Parsa","Parviz","Payam","Pejman",
       "Peyman","Pouria","Pouya","Qobad","Ramin","Rasoul","Reza","Rostam","Sadeq","Saeed","Sahand","Salar","Salman","Sam","Saman","Sasan",
       "Sattar","Sepand","Shadmehr","Shahab","Shahin","Shahram","Shapoor","Siamak","Siavash","Sina","Sirvan","Soheil","Sohrab","Soroosh",
       "Taghi","Vahid","Youssef","Zakaria"]

nm2 =["Afagh","Afsaneh","Afsoon","Aida","Akhtar","Akram","Anahita","Anna","Aram","Arezoo","Asal","Atefeh","Atena","Athar","Azadeh","Azar",
      "Azita","Bahar","Bahareh","Baran","Behnaz","Behnoosh","Bita","Darya","Dorsa","Ehteram","Elahe","Elham","Elnaz","Fahime","Fakhri","Falamak",
      "Farahnaz","Faranak","Fariba","Farzaneh","Fatemeh","Fereshteh","Foroogh","Frouzan","Ghazal","Gohar","Golchehreh","Goli","Golrokh","Golsa",
      "Hadis","Halimeh","Hamideh","Hanieh","Hannaneh","Hasti","Hedieh","Hengameh","Homa","Jamileh","Katayoun","Khatereh","Khatoun","Kheyri",
      "Kobra","Ladan","Leila","Leyli","Mahboobeh","Mahdieh","Mahnaz","Mahtab","Mahya","Malihe","Maryam","Marzieh","Mehraveh","Melika","Mitra",
      "Mohadese","Mohtaram","Monir","Mozhde","Mozhgan","Naghme","Narges","Nasim","Nasrin","Nassim","Nastaran","Nazanin","Negar","Negin","Niki",
      "Nikou","Niloofar","Ozraa","Parastoo","Pardis","Pari","Parichehr","Parisa","Parvaneh","Parvin","Pegah","Poopak","Pooran","Pouri","Raha",
      "Rahele","Razieh","Reyhaneh","Roohangiz","Roushanak","Rouya","Roya","Saba","Sadaf","Sadiqe","Sahar","Sakineh","Samira","Sara","Setareh",
      "Shabnam","Shahin","Shahla","Shamsi","Shaqayegh","Sharareh","Shila","Shirin","Shiva","Sima","Simin","Soheila","Somayeh","Soraya","Susan",
      "Tahmine","Tannaz","Taraneh","Touran","Vida","Yasaman ","Yekta","Youkhavid","Zahra","Zari","Ziba","Zohreh"]

nm3 =["Abbasi","Abdi","Abedi","Adib","Afshani","Afshar","Aghili","Ahangar","Ahmadi","Alidoosti","Almasi","Amini","Arabnia","Arjmand","Asadi","Asayesh",
      "Askari","Aslani","Atlasi","Azadeh","Azari","Baghaii","Bagherzadeh","Bahadori","Bahreini","Barbarz","Bayat","Behdad","Beheshti","Bina","Blourian",
      "Boromand","Bozorgi","Chavoshi","Danesh","Dara","Darvishi","Dehghan","Deljou","Derakhshani","Diba","Dirbaz","Eftekhar","Eghbali","Entezami","Ershadi",
      "Esfahani","Eshtiaq","Eskandari","Faghih","Fallah","Farahani","Faramarzian","Fardin","Farzin","Fathi","Fatollahi","Foroutan","Freydooni","Frootan","Froozan",
      "Gankhaki","Ghaffari","Gharibian","Golchin","Golshani","Golzar","Haghighi","Haghjoo","Haghshenas","Hajar","Hashemi","Hashempour","Hatami","Hayaii","Hayati",
      "Hedayati","Hematti","Heydarpanah","Hosseini","Jabarzadeh","Jafarnejad","Jahangiri","Kamran","Kardan","Karimi","Kasebi","Kashkouli","Kaviani","Keramati",
      "Keshavarz","Khaledi","Khalili","Khodadad","Khoshkam","Khosravi","Kiaei","Kianian","Layegh","Loolaii","Lorestani","Lotfi","Mahdavi","Mahmoodi","Malakooti",
      "Manesh","Mashayekhi","Mehrian","Mehrjoo","Mehrnia","Meskini","Miri","Mirzaii","Modiri","Mofid","Moghadam","Mohebi","Momeni","Moshiri","Mosta'An","Mostofi",
      "Mousavi","Mozafari","Najafi","Nasirian","Nassirian","Nassour","Nazeri","Nemati","Noori","Nouzari","Pahlevan","Pakdel","Panahi","Parastui","Pasdar","Pirdoost",
      "Pirouzfar","Poozesh","Qaderi","Qaedi","Qajar","Qanbari","Qasemi","Raad","Radan","Radish","Raeisi","Rahnema","Raoufi","Rashidi","Rastegar","Rastkar","Rayegan",
      "Razavian","Rezghi","Riahi","Rostami","Rouhani","Sadeghi","Sadiq","Safavi","Saharkhiz","Salehi","Sayyad","Sayyadi","Sehat","Shahi","Shajarian","Shakibaii",
      "Shariati","Shojaii","Shokoohi","Shookohi","Sobhani","Soleymani","Tabasi","Tabatabaii","Taghipour","Taheri","Tahmasb","Tajik","Tarokh","Tarrokh","Tavakoli",
      "Teymoori","Torabi","Vahdat","Vakili","Verdisefat","Vossoughi","Yaghmaei","Yazdani","Yeganeh","Yekta","Zakaria","Zamani","Zand","Zangane","Zareii","Zarqan"]



def rnd():
    opt_rnd=random.randint(0,1)
    result=""
    if opt_rnd==1:
        result=random.choice(nm1)+ " "+random.choice(nm3)
    else:
        result=random.choice(nm2)+ " "+random.choice(nm3)
    return result

def male():
    result=""
    result=random.choice(nm1)+ " "+random.choice(nm3)
    return result

def female():
    result=""
    result=random.choice(nm2)+ " "+random.choice(nm3)
    return result

    
    
