import tika
from tika import parser
import os
from django.conf import settings
from catalog.models import Document


directory = 'C:/Users/hassa/Desktop/pfa/corpus/BO/2017'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):

        file = 'C:/Users/hassa/Desktop/pfa/corpus/BO/2017/'+filename
       
        file_data = parser.from_file(file)
        b=""
        numero=file_data['metadata']
        
        for a in numero['resourceName']:
            if a==".":
                break
            b+=a
        b+= " : "
        
        text = file_data['content']
        res = text.split() 
        ab=0
        titre=""
        for word in res:
                
                if(ab==1):
                    titre+=str(word)
                    titre+=" "
                if(ab==1 & ("." in word)==True):
                    break
                if(word=="officielle"):
                    ab=1
        
        Document(num=b,name=titre,description=text).save()
        

