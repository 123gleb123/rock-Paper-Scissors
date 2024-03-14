import random

rock = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Programma jūs sveicina! Sveiki!")
while True:
    play = input("Vai vēlaties spēlēt? Nospiediet 'w' jebkura vērtības vietā, lai spēlētu, vai 'E', lai izietu no spēles: ")
    if play.upper() == "E":
        print("Paldies, ka spēlējāt! Uz redzēšanos!")
        break
    elif play.upper() == "W":
        print("Lūdzu, izvēlieties savu simbolu:")
        print("1: Akmens")
        print("2: Šķēres")
        print("3: Papīrs")

        vibor_igroka = input("Izvēlieties savu simbolu: ")
        while vibor_igroka not in ["1", "2", "3"]:
            vibor_igroka = input("Lūdzu, izvēlieties 1, 2 vai 3: ")

        if vibor_igroka == "1":
            vibor_igroka_str = rock
        elif vibor_igroka == "2":
            vibor_igroka_str = scissors
        else:
            user_choice_str = paper

        print("Jūsu izvēlētais simbols: ")
        print(vibor_igroka_str)

        vibor_kompa = random.randint(1, 3)
        if vibor_kompa == 1:
            vibor_kompa_str = rock
        elif vibor_kompa == 2:
            vibor_kompa_str = scissors
        else:
            vibor_kompa_str = paper

        print("Datora izvēlētais simbols: ")
        print(vibor_kompa_str)

        if vibor_igroka == str(vibor_kompa):
            print("Neizšķirts!")
        elif (vibor_igroka == "1" and vibor_kompa == 2) or (vibor_igroka == "2" and vibor_kompa == 3) or (vibor_igroka == "3" and vibor_kompa == 1):
            print("Jūs uzvarējāt!")
        else:
            print("Jūs zaudējāt!")
    else:
        print("Nederīga ievade! Lūdzu, izvēlieties atkal.")  
