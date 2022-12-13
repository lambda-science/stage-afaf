import subprocess
import pandas as pd
import os
import glob

df=pd.read_csv('muscle_atlas_clean.csv')
#### Partie HE ##########
#### Préparation des listes pour les images######
df_HE=df[(df['Staining method'].str.contains( 'HE',na=False))] 
images_HE =  list(df_HE["Number"])


for images in images_HE:
    chemin = "Images/" + images
    myoquant= subprocess.run(['myoquant', "he-analysis", chemin,'--output-path',  '/Users/afaf/stage-afaf/data'])

  
#Mes fonctions
def conversion_pix_µm(im, data_frame,muscle_atlas):
  'Convertion du diamètre en µm'
  barre_echelle= muscle_atlas.loc[(df['Number']== im), 'Calibration (um/px)']
    
  data_frame['diameter_µm']=(data_frame['feret_diameter_max'].values)*barre_echelle.values

def count_atrophic_cells (data_frame,min_size, max_size):
  """
  Comptes le nombre de cellules normales, hyper ou hypo atrophique. min_size et max_size peuvent être changer ici on a pris les tailles trouvés dans la littéature
  """
  hyper='Hypertrophy'
  hypo= 'Hypotrophy'
  norm= 'Normal'
  data_frame["State_cell"] = ''
  for index in data_frame.index:
    a=data_frame['diameter_µm'][index]
    if a > max_size:
      data_frame["State_cell"][index]=hyper
    elif a < min_size:
      data_frame["State_cell"][index]=hypo
    else: 
      data_frame["State_cell"][index]= norm

#J'applique les fonctions sur les données 



ath = os.getcwd()
csv_files = []
for folder, subs, files in os.walk("data"):
  for filename in files:
    if filename.endswith(('_cell_details.csv')):
        csv_files .append(os.path.abspath(os.path.join(folder, filename)))


for f in csv_files:
    df_cell_details = pd.read_csv(f)
    for images in images_HE: 
    conversion_pix_µm(images,df_cell_details,df )  
    count_atrophic_cells (df_cell_details, 30, 80)
    #print('Location:', f)
    #print('File Name:', f.split("//")[-1])
    #display(df_cell_details)
    df_cell_details.to_csv(f,sep=",", index=False)



def pourcentage_state_cell (im,data_frame,muscle_atlas):
  """  
  Calcul du pourcentage des cellules normales, hypo et hyper atrophique 

  """
     data = {'Number':[],'Hypertrophy': [],'Normal':[],'Hypotrophy': []}  # Ici on créer un dataframe pour mettre ensuite les valeurs des pourcentages
     df_state_cell = pd.DataFrame(data)  
     percentage= (data_frame['State_cell'].value_counts()/data_frame['State_cell'].count())*100
     df_state_cell.loc[len(df_state_cell.index)] = percentage

     
     muscle_atlas.loc[(muscle_atlas['Number']== im),"Hypertrophic_cell_%"]=df_state_cell['Hypertrophy'].values
     muscle_atlas.loc[(muscle_atlas['Number']== im),"Normal_cell_%"]=df_state_cell['Normal'].values
     muscle_atlas.loc[(muscle_atlas['Number']== im),"Hypotrophic_cell_%"]=df_state_cell['Hypotrophy'].values

def diameter_mean_std (im,data_frame,muscle_atlas):
  """  
  Calcul du diamètre moyen, ainsi que de l'écart type du diamètre
  """
    cell_mean=data_frame['diameter_µm'].mean()
    cell_std=data_frame['diameter_µm'].std()
    muscle_atlas.loc[(muscle_atlas['Number']== im),"diameter_mean"]=cell_mean
    muscle_atlas.loc[(muscle_atlas['Number']== im),"diameter_std"]=cell_std




for f,images in zip(csv_files,images_HE):
    df_cell_details = pd.read_csv(f)
    pourcentage_state_cell (images,df_cell_details,df) 
    #display(df.head(10))
    diameter_mean_std(images,df_cell_details,df)  



fichier = []

for folder, subs, files in os.walk("data"):
  for filename in files:
    if filename.endswith(('_results_summary.csv',)):
        fichier.append(os.path.abspath(os.path.join(folder, filename)))


def ajout_He (im,dataframe,muscle_atlas):
  """ 
  Ajout des données générées par Myoquant dans l'atlas du muscle 
  """
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Proportion_nuclei"]=dataframe.loc['Proportion (%)','N° Nuclei']
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Number_nuclei"]=dataframe.iloc[0,0]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Proportion_intern_nuclei"]=dataframe.loc['Proportion (%)','N° Intern. Nuclei']
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Number_intern_nuclei"]=dataframe.iloc[0,1]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Number_Periph_nuclei"]=dataframe.iloc[0,2]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Proportion_Periph_nuclei"]=dataframe.loc['Proportion (%)','N° Periph. Nuclei']
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Number_Cells with 1+ intern.nuc"]=dataframe.iloc[0,3]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Proportion_Cells with 1+ intern. nuc"]=dataframe.loc['Proportion (%)','N° Cells with 1+ intern. nuc.']




for i ,images in zip(fichier,images_HE):
    df_results_summary=pd.read_csv(i)
    df3=df_results_summary.set_index('Feature')
    df4=df3.transpose()
    ajout_He(images,df4,df) 



#########Partie SDH ##########
####Préparation des listes pour les images######
df_SDH=df[(df['Staining method'].str.contains( 'SDH',na=False))] 
images_SDH=  list(df_SDH["Number"])

for chemin_image in images_SDH:
    myoquant_sdh= subprocess.run(['myoquant', "sdh-analysis",chemin_image ,'--output-path',  '/Users/afaf/stage-afaf/data'])


fichier_sdh = []

for folder, subs, files in os.walk("data"):
  for filename_sdh in files:
    if filename_sdh.endswith(('_results.csv')):
        fichier_sdh.append(os.path.abspath(os.path.join(folder, filename_sdh)))


#import glob
#glob("Users/afaf/stage-afaf/Images_sdh/*.jpg")
def ajout_SDH (im,dataframe,muscle_atlas):
    """ Ajout des données générées par myoquant dans l'atlas du muscle """
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Total cells (%)"]=dataframe.iloc[1,0]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"Number_cells"]=dataframe.iloc[0,0]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"normals_cells (%)"]=dataframe.iloc[1,1]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"normals_cells"]=dataframe.iloc[0,1]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"sick_cells"]=dataframe.iloc[0,2]
    muscle_atlas.loc[(muscle_atlas['Number']== im),"sick_cells (%)"]=dataframe.iloc[1,2]

for j ,images1 in zip(fichier_sdh,images_SDH):
    df_results_sdh=pd.read_csv(j)
    df_sdh=df_results_sdh.set_index('Feature')
    df_sdh1=df_sdh.transpose()
    data_sdh = {'Muscle Fibers': [],'control':[],'sick': []} 
    df_sdh2 = pd.DataFrame(data_sdh)  
    df_sdh3 = df_sdh2.append(df_sdh1,ignore_index = True)
    #display(df_sdh3)
    df_sdh3.to_csv(j,sep=",", index=False)

for j ,images1 in zip(fichier_sdh,images_SDH):
    df_sdh_final=pd.read_csv(j)
    ajout_SDH(images1,df_sdh_final,df) 