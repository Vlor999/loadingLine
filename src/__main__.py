#!/usr/bin/env python3
import time
from loadingLine import loading

def main():
    taille = 500
    largeur_barre = 100 
    for i in range(taille + 1):
        loading(i, taille, largeur_barre)
        time.sleep(0.01)

    print()

if __name__ == '__main__':
    main()
