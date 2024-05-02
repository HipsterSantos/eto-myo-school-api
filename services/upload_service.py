import pandas as pd
from models.schools import School

class UploadService:
    
    def __init__(self,file):
        self.file = pd.read_excel(file)
        
    def from_excel_to_rows(self,file=None):
            try:
                columns_to_filter = ['nome', 'email', 'total_salas', 'provincia']
                self.file = self.file[columns_to_filter]
                schools = [ 
                        School(
                            name=row['nome'],
                            email=row['email'],
                            total_room=row['total_salas'],
                            province=row['provincia']
                        ) for index,row in self.file.iterrows()
                        ]

                print(f'file is {schools}')
                return schools
            except Exception as e : 
                print(f'error {e}')
                raise Exception(f'from <upload_service> Error= {e} ')