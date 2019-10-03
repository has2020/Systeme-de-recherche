# Systeme-de-recherche

Rèalisation d'un systeme de rechere
L'objectif de ce projet et de créer un système de recherche sur des textes de bulletin officiel sous forme de PDF, 
tout en faisant l’extraction des données du pdf, la création d’indexes et finalement la recherche.

Outils : Django , Elasticsearch , Haystack , Apache

INSTALLATION:

installation d'elasticsearch:(d'autre version que celle ci ne fonctionne pas)
vous devrez d'abord avoir jdk1.8.0 installer  dans votre machine
puis vous deverez ajouter le jdk dans la variable d'envirenement dans votre machine
apres cela vous devrez acceder au dossier elasticsearch-1.7.5/bin et executer elasticsearch.bat en tant qu'administrateur.
pour savoir est ce que elasticsearch fonctionne ou pas acceder a http://127.0.0.1:9200 
vous deverz voir quelque chose semble a cela :
{
  "status" : 200,
  "name" : "Jane Foster",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.7.5",
    "build_hash" : "00f95f4ffca6de89d68b7ccaf80d148f1f70e4d4",
    "build_timestamp" : "2016-02-02T09:55:30Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
} 

--------------------------------------------------------------------
installation de haystack:
tous d'abord vous deverez avoir python installer dans votre machine
apres l'installation du python ouvrir cmd et taper la commande : pip install django-haystack	

---------------------------------------------------------------------

EXECUTION:
ouvrir cmd est acceder au path de l'application systeme_recherche
puis taper la commende: C:\Systeme-de-recherche> python manage.py rebuild_index
puis C:\Systeme-de-recherche> python manage.py runserver
puis acceder a http://127.0.0.1:8000
