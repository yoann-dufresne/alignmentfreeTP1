
# Alignment free - TP 1

## Télécharger la base de code du TP

Durant nos TPs, nous allons utiliser Git pour récupérer le TP, versionner votre code et rendre le TP. 

### Je n'ai jamais utilisé Git

Si tu n'as jamais utilisé Git, ce TP est le bon moment pour démarrer. En bioinformatique, tous les logiciels produits sont hébergés sur des dépôts en ligne Git.
Pour te faire la main avec git, je te laisse parcourir [ce tutoriel qui t'expliquera les bases](https://git.goffinet.org/02-les-bases-de-git)

Pour ce TP, nous utiliserons Github comme hébergeur. Si vous n'avez pas de compte, il vous faudra en créer un pour pouvoir rendre le TP.
Une fois votre compte créé vous allez devoir enregistrer votre clé ssh sur le serveur. Dans les paramètres de votre compte, allez dans la rubrique "SSH and GPG keys" et suivez le lien qui explique comment entrer votre clé publique.

Vous êtes maintenant prêt.e à télécharger les bases de votre TP

### Télécharger les bases pour le TP

* Rendez-vous à l'adresse du TP : https://github.com/yoann-dufresne/alignmentfreeTP1

* Cliquez sur le bouton "fork" en haut de la page pour créer une copie du TP au sein de votre compte. Nommez le comme bon vous semble et validez.

* Sur la page où vous arrivez, il faut récupérer l'adresse à laquelle télécharger le code sur votre ordinateur. Pour cela cliquez sur "code" puis "ssh" et copiez d'adresse qui apparait.

* Enfin, sur votre ordinateur, à l'emplacement où vous voulez télécharger le TP, utilisez la commande suivante **en changeant l'adresse git par celle que vous venez de copier**.

```bash
    # Télécharge le dépôt de code initial. Le --recursive est nécessaire pour télécharger les sous-dépôts liés.
    git clone --recursive git@github.com:ada-lovelace/alignmentfreeTP1.git
```


## Objectifs du TP

Pour ce TP il faudra comparer un ensemble de 5 bactéries pour retrouver les familles présentes. L'objectif final est de produire une matrice des similarités de Jaccard entre tous les échantillons.
**Attention** : Ce TP est une base pour le prochain. Si vous ne l'avez pas fini, vous ne pourrez pas faire le suivant !

### Récupérer les séquences bactériennes

Pour télécharger les données je vous ai préparé un fichier dataset.reg qui contient l'ensemble des accessions ENA à télécharger.
Vous pouvez utiliser le logiciel seqdd qui a été téléchargé au sein de votre TP pour facilement récupérer les fichiers fasta.
Pour cela, depuis la racine de votre projet vous devez effectuer la liste de commandes suivantes:

```bash
    # Installe localement l'outil seqdd depuis le répertoire nommé seqdd
    python3 -m pip install --user seqdd
    # Initialise le registre de données avec le fichier .reg du tp
    seqdd init -r dataset.reg
    # Télécharge les données depuis le European Nucleotide Archive (ENA)
    seqdd download -d data/
```

Si cette procédure ne fonctionne pas, vous pouvez ouvrir le fichier .reg comme un fichier texte puis vous rendre manuellement sur le site web de ENA et y télécharger manuellement les jeux de données listés.

### Composer le TP

La code que vous avez téléchargé fonctionne déjà mais ne calcul rien.
Pour le lancer, vous devez appeler la commande :

```bash
    # Déclenche l'exécution du fichier __main__.py dans le module TP
    python3 -m TP
```

Si tout se passe bien, le code devrait charger tous les échantillons présents dans le répertoire data/ puis lancer une distance de Jaccard entre toutes les pairs d'échantillon.
La fonction Jaccard n'étant pas codée, toutes les valeurs affichées devraient être à 0.

Votre travail sera de compléter les fonctions pour que les indices de Jaccard soient bons.


### Sauvegarder mon TP

En tant que bon.ne développeur.euse, mon TP est modifié et testé de manière incrémentale. Je m'assure à tout moment que ce que je viens de coder est correct.
Dès que j'ai ajouté une nouvelle fonctionnalité et que tout est ok, je la sauvegarde sur github de la manière suivante :

```bash
    # Ajout des fichiers modifiés à la liste des fichiers suivis par git
    git add TP/monfichier.py TP/mondeuxiemefichier.py
    # Packaging des fichiers modifiés et message explicatif de la nouvelle fonctionnalité
    git commit -m "Ajout de la fonctionnalité X, désormais le TP fait Y"
    # Envoie du package sur les serveurs github
    git push origin main
```

### Rendre mon TP

Le rendu attendu est un email indiquant l'adresse de votre dépôt git contenant le TP.
Vous devez Créer une branche "rendu_1" que vous ne toucherez plus après avoir envoyé le mail.

Dans votre dépôt est attendu :
* Le code complété pour que les indices de Jaccard soient calculés
* Un fichier RENDU.md qui contient un rapport succinct sur votre rendu. Ce rapport doit contenir la matrice des distances entre échantillons, un commentaire sur ce que cette matrice vous apprends et une description des méthodes que vous avez implémenté.

Le TP peut être rendu par bionôme. Vous devez me l'indiquer dans RENDU.md en précisant les prénoms et noms.
