import random

i = random.randint(1, 20)
i1 = random.randint(1, 20)
tas1 = i
tas2 = i1

joueur1 = str(input("Veuillez entrer le pseudo du premier joueur : "))

joueur2 = str(input("Veuillez entrer le pseudo du deuxieme joueur : "))

print(str(joueur1) + " a le tas 1.")
print(str(joueur2) + " a le tas 2.")

print("Nombre de jetons dans chaque tas 1 : " + str(i))
print("Nombre de jetons dans chaque tas 2 : " + str(i1))

joueur1tour = True
joueur2tour = False

while tas1 > 0 or tas2 > 0:

    tas1 = tas1
    tas2 = tas2

    if joueur1tour == True:
        print(" ")
        print("C'est au tour de : " + str(joueur1))
        choixtas = int(input("Sur quel tas voulez vous jouer : "))

        if choixtas == 1:
            print("Parfait! Vous avez choisie de jouer sur le tas 1")

            jetonsR = int(
                input(
                    "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                ))

            while jetonsR > 3:
                print("Vous ne pouvez jouer que 1 à 3 jetons par tour !")
                jetonsR = int(
                    input(
                        "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                    ))

            if jetonsR == 1:
                tas1 -= 1
                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + " du tas 1 !")
                print("Jetons restants dans tas 1 : " + str(tas1))
                joueur1tour = False
                joueur2tour = True
                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 2:
                tas1 -= 2

                print(" ")

                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + " du tas 1 !")
                print(" ")

                print("Jetons dans tas 1 : " + str(tas1))
                joueur1tour = False
                joueur2tour = True

                print(" ")

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 3:
                tas1 -= 3
                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + " du tas 1 !")
                print(" ")

                print("Jetons dans tas 1 :" + str(tas1))
                joueur1tour = False
                joueur2tour = True

                print(" ")

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

        elif choixtas == 2:
            print("Parfait! Vous avez choisie de jouer sur le tas 2")

            jetonsR = int(
                input(
                    "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                ))

            while jetonsR > 3:
                print("Vous ne pouvez jouer que 1 à 3 jetons par tour !")
                jetonsR = int(
                    input(
                        "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                    ))

            if jetonsR == 1:
                tas2 -= 1
                print(" ")

                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + " du tas 2 !")
                print(" ")

                print("Jetons restants dans tas 1 : " + str(tas2))
                joueur1tour = False
                joueur2tour = True
                print(" ")

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 2:
                tas2 -= 2
                print(" ")

                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + " du tas 2 !")
                print(" ")

                print("Jetons dans tas 2 :" + str(tas1))
                joueur1tour = False
                joueur2tour = True
                print(" ")

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 3:
                tas2 -= 3

                print(" ")

                print("Le joueur " + str(joueur1) + " a retiré " +
                      str(jetonsR) + "du tas 2 !")

                print(" ")

                print("Jetons dans tas 2 :" + str(tas2))

                joueur1tour = False
                joueur2tour = True

                print(" ")

                for x in range(tas2):
                    print("O ", sep=' ', end=' ', flush=True)

    if joueur2tour == True:

        print(" ")

        print("C'est au tour de : " + str(joueur2))
        choixtas = int(input("Sur quel tas voulez vous jouer : "))

        if choixtas == 1:
            print(" ")

            print("Parfait! Vous avez choisie de jouer sur le tas 1")

            jetonsR = int(
                input(
                    "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                ))

            while jetonsR > 3:
                print("Vous ne pouvez jouer que 1 à 3 jetons par tour !")
                jetonsR = int(
                    input(
                        "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                    ))

            if jetonsR == 1:
                tas1 -= 1

                print(" ")

                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + " du tas 1 !")

                print(" ")

                print("Jetons restants dans tas 1 : " + str(tas1))

                print(" ")

                joueur1tour = True
                joueur2tour = False
                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 2:
                tas1 -= 2

                print(" ")

                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + "du tas 1 !")

                print(" ")

                print("Jetons dans tas 1 :" + str(tas1))

                print(" ")

                joueur1tour = True
                joueur2tour = False

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 3:

                print(" ")

                tas1 -= 3
                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + "du tas 1 !")

                print(" ")

                print("Jetons dans tas 1 :" + str(tas1))

                print(" ")

                joueur1tour = True
                joueur2tour = False

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

        elif choixtas == 2:

            jetonsR = int(
                input(
                    "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                ))

            while jetonsR > 3:
                print("Vous ne pouvez jouer que 1 à 3 jetons par tour !")
                jetonsR = int(
                    input(
                        "Combien de jetons voulez vous retirer (de 1 à 3 jetons): "
                    ))

            print("Parfait! Vous avez choisie de jouer sur le tas 2")
            if jetonsR == 1:

                print(" ")

                tas2 -= 1
                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + " du tas 2 !")

                print(" ")

                print("Jetons restants dans tas 1 : " + str(tas2))

                print(" ")

                joueur1tour = True
                joueur2tour = False

                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 2:

                print(" ")

                tas2 -= 2
                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + " du tas 2 !")

                print(" ")

                print("Jetons dans tas 2 : " + str(tas1))

                print(" ")

                joueur1tour = True
                joueur2tour = False
                for x in range(tas1):
                    print("O ", sep=' ', end=' ', flush=True)

            elif jetonsR == 3:

                print(" ")

                tas2 -= 3

                print("Le joueur " + str(joueur2) + " a retiré " +
                      str(jetonsR) + " du tas 2 !")

                print(" ")

                print("Jetons dans tas 2 : " + str(tas2))

                print(" ")

                joueur1tour = True
                joueur2tour = False
                for x in range(tas2):
                    print("O ", sep=' ', end=' ', flush=True)

if tas1 == 0 and tas1 < 0:
    print(str(joueur2) + " a gagné la partie !")
elif tas2 == 0 and tas2 < 0:
    print(str(joueur1) + " a gagné la partie !")
