Bonjour !

Ce rendu de TP est le travail de Steve JATIERE et Loralie RIGAUD.
Il contient une mise à jour de la fonction stream_kmer et les nouvelles fonctions de sketch, le bottom minhash et le partition minhash, le tout à partir de la correction du TP1.
A cause de soucis de téléchargement des données, nous n'avons pas pu récupérer les génomes de l'humain, de la souris et du primate comme demandé. Nous avons donc lancé l'analyse sur les mêmes données que le TP1, soit les 5 génomes bactériens.

Ci-dessous les matrices des résultats pour les deux différentes méthodes.

BOTTOM MINHASH :
                GCA_000008865.2 GCA_000013265.1 GCA_030271835.1 GCA_000005845.2 GCA_000069965.1
GCA_000008865.2             1.0         0.12638        0.001753        0.163806        0.001402
GCA_000013265.1                             1.0        0.002674        0.187648        0.002004
GCA_030271835.1                                             1.0         0.00452        0.030574
GCA_000005845.2                                                             1.0        0.003009
GCA_000069965.1                                                                             1.0

PARTITION MINHASH :
                GCA_000008865.2 GCA_000013265.1 GCA_030271835.1 GCA_000005845.2 GCA_000069965.1
GCA_000008865.2             1.0        0.074345             0.0        0.129624             0.0
GCA_000013265.1                             1.0        0.000333        0.126549         0.00025
GCA_030271835.1                                             1.0        0.001001        0.012829
GCA_000005845.2                                                             1.0        0.000667
GCA_000069965.1                                                                             1.0

En comparaison avec les résultats du TP1, nous pouvons voir que le bottom minhash garde le même maximum donc l'estimation de Jaccard pour le bottom minhash renvoie les mêmes séquences comme étant les plus proches. Toutes les valeurs supérieures à 0.3 dans les résultats du TP1 ont diminué mais les autres valeurs sont restées proches de la correction. Le bottom minhash semble bien estimé les petites valeurs de Jaccard mais sous-estime les valeurs des séquences les plus proches.
Le partition minhash, semble avoir bien moins marché au vu des zéros qui apparaissent dans la matrice, cela aurait pu être parce que le svaleurs les plus petites sont mal estimées mais pourtant ce n'est pa sle ca pour les séquences les plus éloignées, leur estimation de Jaccard reste très faible mais supérieur à 0. Nous n'avons pas trouvé d'explication pour ces zéros ni su trouver l'erreur dans le code. De plus, les séquences les plus proches après lecture de l amatrice de résultat du partition minhash ne sont plus les mêmes que dans la correction ou bien le bottom minhash. Tout cela nous mène à conclure que nous nous sommes trompés quelque part mais n'avons pas su où.
Par manque de temps, nosu n'avons pas pu coder la troisième méthode d'estimation du Jaccard avec la transformation des integer en 16 bits.