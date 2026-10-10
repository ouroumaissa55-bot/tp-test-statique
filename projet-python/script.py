import os
# ❌FAILLE DE SÉCURITÉ : Utilisation d'une fonction dangereuse (exec)
def executer_commande(user_input):
    exec(user_input) 

def verifier_age(age):
    # ❌BUG : Comparaison illogique
    if age == None:
        print("Age non fourni")
    # ❌CODE SMELL : Mauvaise pratique d'imbrication
    if age > 18:
        if age < 100:
            return True
        else:
            return False
    else:
        return False

# ❌DUPLICATION DE CODE EN TEST STATIQUE
def verifier_age_doublon(age):
    if age > 18:
        if age < 100:
            return True
        else:
            return False
    else:
        return False