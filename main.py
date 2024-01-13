# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def exercice1(num1, num2):
    pro = num1 * num2
    if pro <= 1000:
        print(pro)
    else:
        print(num1 + num2)


def exercice2_1():
    for current in range(10):
        if current > 0:
            previous = current - 1
        else:
            previous = 0
        total = previous + current
        print(f"Current number {current} Previous number {previous} Sum: {total}")


def exercice2_2():
    for current in range(10):
        previous = max(0, current - 1)
        print(f"Current number {current} Previous number {previous} Sum: {previous + current}")


def exercice2_3():
    print("Printing current and previous number and their sum in a range(10)")
    previous = 0
    for current in range(0, 10):
        total = previous + current
        print("Current Number", current, "Previous Number ", previous, " Sum: ", total)
        previous = current


def exercice3_1():
    word = input("Enter a word : ")
    for letter in range(0, len(word) - 1, 2):
        print(word[letter])


def exercice3_2():
    word = input("Enter a word : ")
    word_letter = list(word)
    for letter in word_letter[::2]:
        print(letter)


def exercice4():
    word = input("Enter a word : ")
    num = int(input("Enter a number : "))
    new_word = word[num:]  # [start:stop:step]=> start=index3, stop=fin et step=1 par défaut
    print(new_word)


def test():
    word = input("Enter a word : ")
    even_letters = word[::2]
    print(even_letters)


def test2():
    word = input("Enter a word : ")
    num = int(input("Enter a number : "))
    new_word = word[:len(word) - num:]
    print(new_word)


def exercice5():
    list1 = [10, 20, 30, 40, 10]
    list2 = [75, 65, 35, 75, 30]
    print("The first and the last numbers of the list are the same :")
    if list1[0] == list1[len(list1) - 1]:
        print("Liste 1 : True")
    else:
        print("Liste 1 : False")
    if list2[0] == list2[len(list2) - 1]:
        print("Liste 2 : True")
    else:
        print("Liste 2 : False")


def exercice6():
    list1 = [10, 20, 33, 46, 55]
    for num in list1:
        if num % 5 == 0:
            print(num)


def test3():
    list1 = [10, 89, 46, 31, 5, 55, 75, 102]
    num_pre = 0
    for num in list1:
        if num >= num_pre:
            print(num)
        num_pre = num


def test4():
    list1 = [10, 89, 46, 31, 5, 55, 75, 102]
    num_pre = 0
    for num in list1:
        if num >= num_pre:
            print(num)
    num_pre = list1[+1]


def exercice7_1():
    phrase = input("Enter a sentence : ")
    word = input("Search for : ")
    count1 = phrase.count(word)
    print(f"There {'are' if count1 != 1 else 'is'} {count1} '{word}' in that sentence.")  # !=1 revient à not in [1]


def exercice7_2(statement, word):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + len(word)] == word
    print(word, "appeared ", count, "times")


# count = exercice7_2("Emma is good developer. Emma is a writer", "Emma")

def exercice8(i):
    for num in range(1, i + 1):
        print(f"{num} " * num)


def test1():
    a = input("Entrez un nombre : ")
    while not a.isdigit():
        a = input("Veuillez ne rentrer que des nombres : ")
    a = int(a)
    b = input("Entrez un nombre : ")
    while not b.isdigit():
        b = input("Veuillez ne rentrer que des nombres : ")
    b = int(b)
    c = a + b
    print(c)


def exo1():
    phrase = "Bonjour tout le monde."
    nouvelle_phrase = phrase.replace("jour", "soir")
    print(nouvelle_phrase)


def exo2(lettre, phrase):
    resultat = phrase.count(lettre)
    print(f'There is {resultat} "{lettre}" in "{phrase}".')


def exo3():
    chaine = "Pierre, Julien, Anne, Marie, Lucien"
    result = ", ".join(chaine.split(", "))
    print(result)


def exo3_bis():
    chaine = "Pierre, Julien, Anne, Marie, Lucien"
    chaine_in_order = sorted(chaine.split(", "))
    result = ", ".join(chaine_in_order)
    print(result)


# Aussi possible :
#    chaine = "Pierre, Julien, Anne, Marie, Lucien"
#    chaine_liste = chaine.split(", ")
#    chaine_liste.sort()     (=> modifie la liste même contrairement à sorted())
#    chaine_en_ordre = ", ".join(chaine_liste)


def test5():
    nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
    if nom_utilisateur == "Eva":
        print("Accès autorisé")
    elif nom_utilisateur == "Phil":
        print("Accès autorisé")
    else:
        print("Accès refusé")


# Quand il y a juste un if-else, on peut le mettre en une ligne (=opérateur ternaire). Ex.:
# age = int(input("Entrez votre âge : "))
# print("Vous êtes majeur") if age >= 18 else print("Vous êtes mineur")


def test6():
    nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
    mot_de_passe = input("Entrez votre mot de passe: ")
    if nom_utilisateur == "Eva" or "Phil" and mot_de_passe == "mioumiou":
        print("Accès autorisé")
    else:
        print("Accès refusé")


def test7():
    import random
    a = random.randrange(101)
    b = random.randrange(101)
    if a > b:
        print(f"Le nombre a ({a}) est plus grand que le nombre b ({b}).")
    elif b > a:
        print(f"Le nombre b ({b}) est plus grand que le nombre a ({a}).")
    else:
        print(f"Le nombre a et le nombre b sont égaux ({b}).")


def test8():
    import random
    from pprint import pprint
    pprint(dir(random))
    help(random.uniform)


def test9():
    liste = [1, 2, 3, 4, 5]
    liste.append(6)
    if 6 in liste:
        print(f"Le nombre 6 a bien été ajouté à la liste : {liste}.")


def exo4():
    for i in range(10):
        print(f"Utilisateur {i + 1}")


def exo5():
    mdp = input("Entrez un mot de passe (min 8 caractères) : ")
    mdp_trop_court = "votre mot de passe est trop court."
    if len(mdp) < 8:
        print(mdp_trop_court.capitalize())
    elif mdp.isdigit():
        print("Votre mot de passe ne contient que des nombres.")
    else:
        print("Inscription terminée.")


def exo6():
    mot = "Python"
    for lettre in reversed(mot):
        print(lettre)


# Aussi possible :
# mot = "Python"
# for lettre in mot[::-1]:
#    print(lettre)


def exo7():
    continuer = "o"
    while continuer == "o":
        print("On continue !")
        continuer = input("Voulez-vous continuer ? o/n ")


def exo8():
    nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
    nombres_pairs = [i for i in nombres if i % 2 == 0]
    print(nombres_pairs)
    # ---------------------------------------------------- #
    nombres = range(-10, 10)
    nombres_positifs = [i for i in nombres if i >= 0]
    print(nombres_positifs)
    # ---------------------------------------------------- #
    nombres = range(5)
    nombres_doubles = [i * 2 for i in nombres]
    print(nombres_doubles)
    # ---------------------------------------------------- #
    nombres = range(10)
    nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
    print(nombres_inverses)


def test_fichier_texte():
    chemin = r"C:\Users\Eva Boland\Desktop\Cours Python\Exercice\Fichier.txt"
    with open(chemin, "a") as mon_fichier:
        mon_fichier.write("\nComment allez-vous ?")
        # mon_fichier.write("Bonjour")
        # contenu = mon_fichier.read


def test_json():
    # json.dump("Bonjour", mon_fichier) json.dump(list(range(10)), mon_fichier, indent=4) Il ne peut pas y avoir
    # plusieurs objets à l'intérieur d'un même fichier json (par exemple une liste et une chaîne de caractères,
    # ou deux listes).
    import json
    chemin = r"./fichier.json"

    '''with open(chemin, "w") as mon_fichier:
        contenu = ["Bonjour,"]
        json.dump(contenu, mon_fichier)'''

    with open(chemin, "r") as mon_fichier:
        contenu = json.load(mon_fichier)

    '''contenu.append("\nComment allez-vous?")'''

    with open(chemin, "w") as mon_fichier:
        json.dump(contenu, mon_fichier, indent=4)

    # N.B. :quand on lit un fichier (fichier.read), on déplace le curseur de lecture jusqu'à la fin. Pour pouvoir lire
    # une seconde fois, il faut remettre ce curseur au début avec fichier.seek(0).


def test_pathlib():
    from pathlib import Path
    print(Path.home())  # Affiche le dossier maison
    print(Path.cwd())  # Affiche le dossier dans lequel on est (dossier courrant)
    p = Path.home()  # Je choisis de nommer ma variable p pour path
    p1 = p / "PycharmProjects" / "pythonProject"  # Concaténer des bouts de chemin
    p2 = p.joinpath("PycharmProhects", "pythonProject")  # Autre façon de concaténer des bouts de chemin

    p = Path(r"C:\Users\Eva Boland\PycharmProjects\pythonProject\main.py")
    # p.name      # main.py
    # p.parent    # "C:\Users\Eva Boland\PycharmProjects\pythonProject"
    # p.stem      # Réccupère ce qu'il y a avant la dernière extension : "main"
    # p.suffix    # réccupérer le suffix : .py
    # p.suffixes  # réccupérer les suffixes s'il y en a plusieurs
    # p.parts     # ('C:\\', 'Users', 'Eva Boland', 'PycharmProjects', 'pythonProject', 'main.py')
    # p.exists()  # Vérifier s'il existe
    # p.is_dir()  # Vérifier si c'est un dossier
    # p.is_file() # Vérifier si c'est un fichier

    p = p.parent
    p = p.joinpath("Dossier test")  # Ajouter au chemin le dossier qu'on voudra créer
    p.mkdir(exist_ok=True)  # Créer le dossier (exist_ok=True permet de ne pas créer d'erreur s'il existe déjà)
    p = p.joinpath("Test 1", "Test 2", "Test 3")  # Crée les trois dossiers les un dans les autres
    p.mkdir(parents=True, exist_ok=True)  # parents=True permet de créer des dossiers dans des dossiers qui
    # n'existent donc pas encore
    p = p.joinpath("Fichier test.txt")  # Ajoute au chemin le fichier à créer
    p.touch()  # Crée le fichier
    p.unlink()  # Supprime le fichier
    p = p.parent  # Je remonte le chemin de 1
    p.rmdir()  # Je supprime le dossier (ne marche que s'il est vide)

    # Pour supprimer un dossier pas vide :
    import shutil
    p = p.parent.parent  # Je remonte de 2 dans le path jusqu'à Test 1 qui contient Test 2
    shutil.rmtree(p)  # Supprime le dossier Test 1
    p = p.parent  # Je remonte dans Dossier Test
    p = p.joinpath("Fichier Test.txt")
    p.touch()
    p.write_text("Bonjour")  # Permet d'écrire dans le fichier
    print(p.read_text())  # Permet de lire le contenu du fichier


def exo_dictionnaire():
    films = {"Le Seigneur des Anneaux": 12, "Harry Potter": 9, "Blade Runner": 7.5}
    prix: float = 0
    films["Harry Potter"] = 10
    if "Frozen" not in films:
        films["Frozen"] = 5
    if "Frozen" in films:
        del films["Frozen"]
    for key in films:
        prix += float(films.get(key))
    print(prix)


def delete_entry(employes: dict, ids: dict, prenom: str):
    eid: str = ids.get(prenom)
    if eid:
        del employes[eid]
    else:
        print("Employee not found.")


def exo_dictionnaire2():
    employes = {
        "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
        "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
        "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
    }

    ids = {employes[key]["prenom"]: key for key in employes.keys()}

    prenom = input()
    delete_entry(employes, ids, prenom)

    """del employes["id03"]
    employes["id02"]["age"] = 26
    age_paul = employes["id01"]["age"]"""


exo_dictionnaire2()
