from django.core.management.base import BaseCommand
from locmet import models

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        MATRICES = ('Tmax','Tmin','Rainfall')
        
        for m in MATRICES:
            self.delete_url_data(m)

                

    def delete_url_data(self,matrice):
        
        try:
            if matrice == 'Tmax':
                tmax = models.Tmax.objects.all()
                tmax.delete()

            elif matrice == 'Tmin':
                tmin = models.Tmin.objects.all()
                tmin.delete()

            elif matrice == 'Rainfall':
                rainfall = models.Rainfall.objects.all()
                rainfall.delete()
            
            else:
                print('Please make sure the matrice is proper')

        except Exception as e:
            print('Exception in record insertion :- ',e)
            


            

