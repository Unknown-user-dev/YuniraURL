import colorama
import os 
import pyshorteners
from colorama import Fore, Back, Style
from colorama import init
os.system("cls || clear") 
init()
banner = Fore.RED + f"""
 __     __          _           _    _ _____  _      
 \ \   / /         (_)         | |  | |  __ \| |     
  \ \_/ /   _ _ __  _ _ __ __ _| |  | | |__) | |     
   \   / | | | '_ \| | '__/ _` | |  | |  _  /| |     
    | || |_| | | | | | | | (_| | |__| | | \ \| |____ 
    |_| \__,_|_| |_|_|_|  \____|\____/|_|  \_\______|
                                                                                          
            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
"""

print(banner)

def menu():
    print(Fore.GREEN + """
    [1] Raccourcir un lien
    [2] Credits
    [3] Quitter
    """)
    choice = input(Fore.BLUE + "Choisissez une option : ")
    if choice == "1":
        url = input(Fore.BLUE + "Entrez l'url à raccourcir : ")
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(url)
        print(Fore.GREEN + f"Le lien raccourci est : {x}")
        input(Fore.BLUE + "Appuyez sur entrée pour revenir au menu...")
        os.system("cls || clear")
        print(banner)
        menu()
    elif choice == "2":
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 ")
        print(banner)
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !")
        exit()
    else:
        print(Fore.RED + "Erreur : Veuillez saisir une option valide !")
        menu()
if __name__ == "__main__":
    menu()

