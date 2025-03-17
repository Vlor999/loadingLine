
def loading(pos, taille, largeur=100):
    listElem = "▏▎▍▌▋▊▉█"
    tailleList = len(listElem) - 1
    pourcentage = (100 * pos) // taille

    full_blocks = (pos * largeur) // taille 
    remainder = ((pos * largeur) % taille) * tailleList // taille

    ligne = listElem[-1] * full_blocks
    if full_blocks < largeur:
        ligne += listElem[remainder]
    ligne += " " * (largeur - len(ligne) + 1) + "|"

    print(f"\r{ligne} {pourcentage:3d}%", end="", flush=True)