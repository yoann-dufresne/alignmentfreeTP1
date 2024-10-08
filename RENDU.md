Bonjour !

Ce rendu du TP1 est valable pour le binôme JATIERE Steve et RIGAUD Loralie.
Il contient tous les fichiers déjà présents dans l'origine du dossier alignmentfreeTP1 + ce fichier RENDU.md.
Les ajouts de notre part dans le fichier kmer.py permettent d'encoder le premier kmer en integer ainsi que son reverse puis lors de la lecture de tous les kmers de ne choisir que les kmers canoniques (plus petits numériquement parlant).
Les ajouts dans le fichier __main__.py créent un index de ces kmers canoniques associés à leur fréquence d'apparition dans la séquence 1, puis calculent l'intersection et l'union de ces kmers avec la séquence 2 et la distance jaccard (I/U).
La fonction concatenate a été ajoutée afin d'éviter le problème des fichiers fasta avec plusieurs séquences. Elle permet d'accoller bout à bout ces séqeunces pour n'avoir qu'une séquence finale.
Le main final a été modifié pour ajouter la concatenation des séquences d'un fichier fasta.

Les résultats obtenus osnt les suivants :

Matrice Jaccard :
GCA_000008865.2 GCA_000013265.1 0.30704778384295633
GCA_000008865.2 GCA_030271835.1 0.0023181053492807354
GCA_000008865.2 GCA_000005845.2 0.43648199601088594
GCA_000008865.2 GCA_000069965.1 0.002313773013273979
GCA_000013265.1 GCA_030271835.1 0.0024340968309996
GCA_000013265.1 GCA_000005845.2 0.34100765807686256
GCA_000013265.1 GCA_000069965.1 0.002437004618858311
GCA_030271835.1 GCA_000005845.2 0.0025766983532214344
GCA_030271835.1 GCA_000069965.1 0.031133866426999456
GCA_000005845.2 GCA_000069965.1 0.0025674606419615006

Cette méthode permet de comparer globalement deux séquences sans alignement exact. Selon l'équation de la distance de Jaccard, soit I/U, les séquences ayant une distance à 1 sont plus proches l'une de l'autre que des séquences avec une distance à 0. 1 voudrait dire que l'intersection est égale à l'union, que les séquences partagent exactement les mêmes kmers avec la même fréquence. 0 voudrait dire qu'il n'y a pas d'intersection, les séquences n'ont aucun kmer en commun.
Dans notre exemple les séquences les plus proches sont GCA_000008865.2 et GCA_000005845.2 car elles ont la valeur la plus élevée de la matrice (0.43648199601088594).