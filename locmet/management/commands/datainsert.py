from django.core.management.base import BaseCommand
import requests
import json
from locmet import models
from django.db import IntegrityError

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        MATRICES = ('Tmax','Tmin','Rainfall')
        LOCATION = ('UK','England','Scotland','Wales')

        for l in LOCATION:
            for m in MATRICES:
                self.fetch_url_data(l,m)

                

    def fetch_url_data(self,location,matrice):
        
        if location and matrice:
            url_str = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{0}-{1}.json'
            url = url_str.format(matrice,location)
            data = requests.get(url)
            data_list = json.loads(data.text)

            for d in data_list:
                
                d.update({'location' : location})
                
                try:
                    if matrice == 'Tmax':
                        tmax = models.Tmax(**d)
                        tmax.save()

                    elif matrice == 'Tmin':
                        tmin = models.Tmin(**d)
                        tmin.save()

                    elif matrice == 'Rainfall':
                        rainfall = models.Rainfall(**d)
                        rainfall.save()

                    else:
                        print('Please make sure the matrice is proper')

                except IntegrityError:
                    print('Duplicate record insertion :- ',d)

                except Exception as e:
                    print('Exception in record insertion :- ',e,d)
            

