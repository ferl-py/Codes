# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:01:56 2024

@author: ferly
"""

import pandas as pd
import os

file = r'C:\Users\ferly\OneDrive\Desktop\FTW\DASHBOARD\censusfilipinoyouth.csv'
output = os.path.join(os.path.expanduser('~'), 'Downloads', 'censusfilipinoyouth.csv')
x = os.path.join(os.path.expanduser('~'), 'Downloads', 'testv2.csv')
coordinates = os.path.join(os.path.expanduser('~'), 'Downloads', 'Barangay-Level Coordinates (2019).csv')
data = pd.read_csv(file)
coords = pd.read_csv(coordinates)

data.columns
data['Ethnicity'].unique().size
data['Highest Grade/Year Completed'].unique().size
data['Highest Grade/Year Completed'].unique()


# Define grouping functions
def group_education(level):
    if level in ['Kindergarten', 'Preschool']:
        return 'Early Education'
    elif any(grade in level for grade in ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6']):
        return 'Elementary Level'
    elif any(grade in level for grade in ['Grade 7', 'Grade 8', 'Grade 9', 'Grade 10']): 
        return 'Junior High School'
    elif any(grade in level for grade in ['Grade 11', 'Grade 12']):
        return 'Senior High School'
    elif 'High School' in level:
        return 'High School (Old Curriculum)'
    elif any(year in level for year in ['1st Year College', '2nd Year College', '3rd Year College', '4th Year College', '5th Year College', '6th Year College']):
        return 'College Level'
    elif 'Bachelor’s Degree Graduate' in level:
        return 'Bachelor’s Degree'
    elif 'Short-Cycle Tertiary' in level:
        return 'Short-Cycle Tertiary Programs'
    elif 'Post-Secondary Non-tertiary' in level:
        return 'Post-Secondary Non-Tertiary Programs'
    elif 'Post-Secondary Undergraduate' in level:
        return 'Post-Secondary Undergraduate'
    elif "Master's Degree Undergraduate" in level:
        return 'Master’s Level'  
    elif 'Master’s Degree Graduate' in level:
        return 'Master’s Degree'
    elif 'Doctorate Degree Undergraduate' in level:
        return 'Doctorate Level'
    elif 'Doctorate Degree Graduate' in level:
        return 'Doctorate Degree'
    elif 'Not Reported' in level or 'No Grade Completed' in level:
        return 'Not Reported or Unknown'
    elif 'Continuing/Second-Chance Education Program' in level:
        return 'Continuing Education Programs'
    elif 'Inclusive/Special Needs Education Programs' in level:
        return 'Inclusive Education Programs'
    else:
        return 'Other'

# Apply grouping function
data['Grouped_Education'] = data['Highest Grade/Year Completed'].apply(group_education)

# Display the grouped data
print(data[['Highest Grade/Year Completed', 'Grouped_Education']])
data['Grouped_Education'].unique().size

# Find and display entries categorized as 'Other'
other_categories = data[data['Grouped_Education'] == 'Other']
print(other_categories[['Highest Grade/Year Completed', 'Grouped_Education']])

data['Grouped_Education'].unique().size

data['Ethnicity'].unique().size
data['Ethnicity'].unique()


# Define a dictionary to map ethnicities to categories
ethnicity_group = {
    'Ilocano': 'Local Ethnicities',
    'Tagalog': 'Local Ethnicities',
    'Kapampangan': 'Local Ethnicities',
    'Bikol/Bicol': 'Local Ethnicities',
    'Ilonggo': 'Local Ethnicities',
    'Bisaya/Binisaya': 'Local Ethnicities',
    'Waray': 'Local Ethnicities',
    'Boholano': 'Local Ethnicities',
    'Ibanag': 'Local Ethnicities',
    'Tausog/Tausug': 'Local Ethnicities',
    'Cebuano': 'Local Ethnicities',
    'Ibaloy': 'Local Ethnicities',
    'Kankanaey': 'Local Ethnicities',
    'Sama/Samal': 'Local Ethnicities',
    'Ifugao': 'Local Ethnicities',
    'Kalinga': 'Local Ethnicities',
    'Itneg/Tinguian-Mabaka': 'Local Ethnicities',
    'Sama Delaut/ Sama Laut': 'Local Ethnicities',
    'Badjao': 'Local Ethnicities',
    'Maranao': 'Local Ethnicities',
    'Sama Badjao': 'Local Ethnicities',
    'Pangasinan': 'Local Ethnicities',
    'Mangyan': 'Local Ethnicities',
    'Palawan-O-Ken-ey': 'Local Ethnicities',
    'American': 'Foreign Ethnicities',
    'Chinese': 'Foreign Ethnicities',
    'Indian': 'Foreign Ethnicities',
    'Japanese': 'Foreign Ethnicities',
    'Korean, South': 'Foreign Ethnicities',
    'Korean, North': 'Foreign Ethnicities',
    'Turkish': 'Foreign Ethnicities',
    'Australian': 'Foreign Ethnicities',
    'Canadian': 'Foreign Ethnicities',
    'South African': 'Foreign Ethnicities',
    'Spanish': 'Foreign Ethnicities',
    'Italian': 'Foreign Ethnicities',
    'Singaporean': 'Foreign Ethnicities',
    'German': 'Foreign Ethnicities',
    'French': 'Foreign Ethnicities',
    'Taiwanese': 'Foreign Ethnicities',
    'Other Local Ethnicity': 'Other Local and Less Specific Ethnicities',
    'Other Foreign Ethnicity': 'Other Local and Less Specific Ethnicities',
    'Not Reported': 'Other Local and Less Specific Ethnicities',
    'Field Unknown': 'Other Local and Less Specific Ethnicities',
    'Itneg/Tinguian-Maeng': 'Local Ethnicities',
    'Itneg/Tinguian-Banao': 'Local Ethnicities',
    'Itneg/Tinguian-Adasen': 'Local Ethnicities',
    'Zamboangueño': 'Local Ethnicities',
    'Caviteno-Chavacano': 'Local Ethnicities',
    'Itneg/Tinguian-Masadiit': 'Local Ethnicities',
    'Itneg/Tinguian-Muyadan': 'Local Ethnicities',
    'Itneg/Tinguian-Inlaud': 'Local Ethnicities',
    'Yapayao': 'Local Ethnicities',
    'Sama Bangingi': 'Local Ethnicities',
    'Itneg/Tinguian-Binongan': 'Local Ethnicities',
    'Itneg/Tinguian-Balatok': 'Local Ethnicities',
    'Itneg/Tinguian': 'Local Ethnicities',
    'Bago': 'Local Ethnicities',
    'Higaonon/Higa-onon': 'Local Ethnicities',
    'Itneg/Tinguian-Gubang': 'Local Ethnicities',
    'Tingguian': 'Local Ethnicities',
    'Bajau': 'Local Ethnicities',
    'Lambanguian': 'Local Ethnicities',
    'Imalawa': 'Local Ethnicities',
    'Itneg': 'Local Ethnicities',
    'Jama Mapun': 'Local Ethnicities',
    'Itawes': 'Local Ethnicities',
    'Manobo': 'Local Ethnicities',
    'Yakan': 'Local Ethnicities',
    'Kalinga-Ab-abaan': 'Local Ethnicities',
    'Illaud': 'Local Ethnicities',
    'Mangyan-Iraya': 'Local Ethnicities',
    'Subanen/Subanon': 'Local Ethnicities',
    'Davaweno': 'Local Ethnicities',
    'Manobo-Aromanon': 'Local Ethnicities',
    'Manobo-Dulungan-Lambangian': 'Local Ethnicities',
    'Kaunana': 'Local Ethnicities',
    'Batangan': 'Local Ethnicities',
    'Maguindanao': 'Local Ethnicities',
    'Yogad': 'Local Ethnicities',
    'Agta-Agay': 'Local Ethnicities',
    'Kalinga-Culminga': 'Local Ethnicities',
    'Aromanen-Manobo/Eromanen-Manobo': 'Local Ethnicities',
    'Isneg': 'Local Ethnicities',
    'Kagan/Kalagan': 'Local Ethnicities',
    'Guiangan': 'Local Ethnicities',
    'Cotabateno-Chavacano': 'Local Ethnicities',
    'Itneg/Tinguian-Belwang': 'Local Ethnicities',
    'Bukidnon': 'Local Ethnicities',
    'Higaonon-Tagoloanon': 'Local Ethnicities',
    'Iwak': 'Local Ethnicities',
    'Surigaonon': 'Local Ethnicities',
    'Ibukid': 'Local Ethnicities',
    'Bontok': 'Local Ethnicities',
    'Capizeno': 'Local Ethnicities',
    'Romblomanon': 'Local Ethnicities',
    'Kailawan/Kaylawan': 'Local Ethnicities',
    'Kalinga-Aciga': 'Local Ethnicities',
    'Mandaya': 'Local Ethnicities',
    'Bagobo': 'Local Ethnicities',
    'Panay Bukidnon': 'Local Ethnicities',
    'Kalanguya-Yattuka':'Local Ethnicities',
    'Tuwali': 'Local Ethnicities',
    'Tigwahanon': 'Local Ethnicities',
    'Agta-Dupanigan': 'Local Ethnicities',
    'Tinananen': 'Local Ethnicities',
    'Sangir/Sangil': 'Local Ethnicities',
    'Cotabateno': 'Local Ethnicities',
    'Baliwon-I-Sadanga': 'Local Ethnicities',
    'Kalinga-Uma': 'Local Ethnicities',
    'Aromanen-Manobo/Eromanen-Manobo Direrayaan': 'Local Ethnicities',
    'Bukidnon-Pan-Anayon': 'Local Ethnicities',
    'Magahats': 'Local Ethnicities',
    'Mangyan-Buhid': 'Local Ethnicities',
    'Magahats': 'Local Ethnicities',
    'Davao-Chavacano': 'Local Ethnicities',
    'Kalinga-Magaogao': 'Local Ethnicities',
    'British': 'Foreign Ethnicities',
    'Masbateno/Masbatenon': 'Local Ethnicities',
    'Palawani': 'Local Ethnicities',
    'Balangao': 'Local Ethnicities',
    'Masbateno/Masbatenon': 'Local Ethnicities',
    'Kabihug-Manide': 'Local Ethnicities',
    'Agta Isigiran': 'Local Ethnicities',
    'Kalinga-Tongrayan': 'Local Ethnicities',
    'Aromanen-Manobo/Eromanen-Manobo Isoroken': 'Local Ethnicities',
    'Kalinga-Tobog': 'Local Ethnicities',
    'Sibuyan Mangyan-Tagabukid': 'Local Ethnicities',
    'Karay-a': 'Local Ethnicities',
    'Kalinga-Mabaca': 'Local Ethnicities',
    'Agta': 'Local Ethnicities',
    'Mangguangan': 'Local Ethnicities',
    'Aeta': 'Local Ethnicities',
    'Kalinga-Gubang': 'Local Ethnicities',
    'Isinai': 'Local Ethnicities',
    'Ayangan-Henanga': 'Local Ethnicities',
    'Gaddang': 'Local Ethnicities',
    'Cagayanen': 'Local Ethnicities',
    'Kalinga-Banao': 'Local Ethnicities',
    'Tagbanua-Kalamianen': 'Local Ethnicities',
    'Aeta/Ayta-Abelling/Abellen': 'Local Ethnicities',
    'Talaandig': 'Local Ethnicities',
    "Palawan-O-Tao't-Bato": 'Local Ethnicities',
    'Kalinga-Nanong': 'Local Ethnicities',
    'Kalinga-Pinukpuk': 'Local Ethnicities',
    'Kolibugan': 'Local Ethnicities',
    'Langilan': 'Local Ethnicities',
    'Manobo-Ata': 'Local Ethnicities',
    'Ayangan':'Local Ethnicities',
    'Kalinga-Balatoc':'Local Ethnicities',
    'Cuyonen/Cuyunon': 'Local Ethnicities',
    'Abelling/ Aberling': 'Local Ethnicities',
    'Bukidnon-Halowodnon':'Local Ethnicities',
    'Kalinga-Tulgao': 'Local Ethnicities',
    'Baliwon-Gaddang':'Local Ethnicities',
    'Afghan': 'Foreign Ethnicities',
    'Karao':'Local Ethnicities',
    'Dumagat':'Local Ethnicities',
    'Kalanguya':'Local Ethnicities',
    'Ibatan': 'Local Ethnicities',
    "Kankanaey-Hak'ki": 'Local Ethnicities',
    'Swiss': 'Foreign Ethnicities',
    'Ivatan': 'Local Ethnicities',
    'Kalinga-Lubuagan':'Local Ethnicities',
    'Kalinga-Malbong': 'Local Ethnicities',
    'Calinga': 'Local Ethnicities',
    'Agta-Cimaron':'Local Ethnicities',
    'Kalinga-Dao-Angan': 'Local Ethnicities',
    'Applai': 'Local Ethnicities',
    'Kalinga-Gaddang':'Local Ethnicities',
    'Aromanen-Manobo/Eromanen-Manobo Kulmanen':'Local Ethnicities',
    'Isnag' :'Local Ethnicities',
    'Kalinga-Pangol':'Local Ethnicities',
     'Kalinga-Buaya' :'Local Ethnicities',
     'Kalinga-Gaang' :'Local Ethnicities',
     'Malaueg' :'Local Ethnicities',
     'Bontok-Majukayong':'Local Ethnicities',
     'Kalinga-Butbut' :'Local Ethnicities',
     'Tagbanua' :'Local Ethnicities',
     'Baliwon' :'Local Ethnicities',
     'Kalinga-Ballayangan':'Local Ethnicities',
     'Kalinga-Salegseg' :'Local Ethnicities',
     'Kalinga-Dananao' :'Local Ethnicities',
     'Kalinga-Mangali' :'Local Ethnicities',
     'Caviteno':'Local Ethnicities',
     'Kalinga-Limos' :'Local Ethnicities',
     'Kalinga-Ammacian' :'Local Ethnicities',
     'Iranun/Iraynun' :'Local Ethnicities',
     'Kalinga-Sumadel':'Local Ethnicities',
     'Kalinga-Dugpa' :'Local Ethnicities',
     'Kalinga-Dangtalan' :'Local Ethnicities',
     'Dumagat-Kabolowen' :'Local Ethnicities',
     'Mamanwa' :'Local Ethnicities',
     'Ata':'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Lahitanen' :'Local Ethnicities',
     'Kalinga-Poswoy':'Local Ethnicities',
     "T'duray/Teduray" :'Local Ethnicities',
     'Ayta' :'Local Ethnicities',
     'Bukidnon-Akeanon' :'Local Ethnicities',
     'Baliwon-Miligan':'Local Ethnicities',
     'Applai-Kachakran/Kadaclan' :'Local Ethnicities',
     'Baliwon-Fiallig/Fialika' :'Local Ethnicities',
     'Isneg/Isnag':'Local Ethnicities',
     "T'boli/Tboli" :'Local Ethnicities',
     'Kamiguin' :'Local Ethnicities',
     'Balangao-Lias' :'Local Ethnicities',
     'Kalinga-Bangad':'Local Ethnicities',
     'Kalinga-Tanglag' :'Local Ethnicities',
     'Kalinga-Biga' :'Local Ethnicities',
     'Kalinga-Lubo' :'Local Ethnicities',
     'Kalinga-Mabongtot':'Local Ethnicities',
     'Kalinga-Ableg/Dalupa' :'Local Ethnicities',
     'Aeta/Ayta-Sambal' :'Local Ethnicities',
     'Kalinga-Dallac':'Local Ethnicities',
     'Kalinga-Dacalan' :'Local Ethnicities',
     'Manobo-Kirenteken' :'Local Ethnicities',
     'Kalinga-Guina-ang' :'Local Ethnicities',
     "B'laan/Blaan":'Local Ethnicities',
     'Bugkalot/Ilongot' :'Local Ethnicities',
     'Aeta/Ayta' :'Local Ethnicities',
     'Tuwali-Kele-I' :'Local Ethnicities',
     'Palawan-o' :'Local Ethnicities',
     'Banwaon':'Local Ethnicities',
     'Bagobo Klata' :'Local Ethnicities',
     'Dumagat-Edimala' :'Local Ethnicities',
     'Dumagat-Tagebolus' :'Local Ethnicities',
     'Mansaka':'Local Ethnicities',
     'Kalinga-Basao' :'Local Ethnicities',
     'Mangyan-Tau-Buid' :'Local Ethnicities',
     'Bagobo Tagabawa' :'Local Ethnicities',
     'Mangyan-Hanunuo':'Local Ethnicities',
     'Talaingod' :'Local Ethnicities',
     'Kalinga-Taloctoc' :'Local Ethnicities',
     'Kalinga-Balinciagao' :'Local Ethnicities',
     'Kalanguya-Ikalahan':'Local Ethnicities',
     'Ati' 'Kalinga-Guilayon' :'Local Ethnicities',
     'Pan-Ayanon' :'Local Ethnicities',
     'Aeta/Ayta-Mag-Indi':'Local Ethnicities',
     'Aeta/Ayta-Ambala' :'Local Ethnicities',
     'Mangyan-Buhid/Bangon' :'Local Ethnicities',
     'Agta-Labin' 'Diangan' :'Local Ethnicities',
     'Molbog':'Local Ethnicities',
     'Batak' :'Local Ethnicities',
     'Manobo-Blit' :'Local Ethnicities',
     'Ata/Negrito' :'Local Ethnicities',
     'Umayamnon' :'Local Ethnicities',
     'Bukidnon-Iraynon':'Local Ethnicities',
     'Kabayukan' :'Local Ethnicities',
     'Kalinga-Minanga' :'Local Ethnicities',
     'Agta-Dumagat' :'Local Ethnicities',
     'Mangyan-Alangan':'Local Ethnicities',
     'Indonesian' :'Foreign Ethnicities',
     'Agta-Taboy' :'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Ilianen':'Local Ethnicities',
     'Kalinga-Cagaluan' :'Local Ethnicities',
     'Parananum' :'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Dibabeen':'Local Ethnicities',
     'Eskaya' :'Local Ethnicities',
     'Kabihug' :'Local Ethnicities',
     'Bukidnon-Ituman' :'Local Ethnicities',
     'Agta-Tabangnon' :'Local Ethnicities',
     'Dumagat-Remontado':'Local Ethnicities',
     'Agutaynen' :'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Kirenteken' :'Local Ethnicities',
     'Alta':'Local Ethnicities',
     'Bantoanon' :'Local Ethnicities',
     'Matigsalog':'Local Ethnicities',
     'Ubo Manuvu/Manobo-Ubo/Ubo Manobo/Ubo Manuvu/Ubo Menuvu' :'Local Ethnicities',
     'Tagabawa':'Local Ethnicities',
     'Tagbanua-Calamian' :'Local Ethnicities',
     'Mangyan-Bangon':'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Mulitaan' :'Local Ethnicities',
     'Tagakaulo' :'Local Ethnicities',
     'Mangyan-Gubatnon':'Local Ethnicities',
     'Magkunana' :'Local Ethnicities',
     'Aeta/Ayta-Mang-Ansti' :'Local Ethnicities',
     'Mangyan-Tadyawan' :'Local Ethnicities',
     'Karulano':'Local Ethnicities',
     'Manobo-Blit-Tasaday' :'Local Ethnicities',
     'Aeta/Ayta-Magbukun' :'Local Ethnicities',
     'Mangyan-Ratagnon' :'Local Ethnicities',
     'Dibabawon':'Local Ethnicities',
     'Manobo-Dulangan' :'Local Ethnicities',
     'Bukidnon-Tagoloanon' :'Local Ethnicities',
     'Tagbanua-Tandulanen':'Local Ethnicities',
     'Obu-Manuvu' :'Local Ethnicities',
     'Manobo-Dunggoanon':'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Pulengien' :'Local Ethnicities',
     'Bukidnon-Magahat':'Local Ethnicities',
     'Manobo-Pulanguinon' :'Local Ethnicities',
     'Aromanen-Manobo/Eromanen-Manobo Livunganen':'Local Ethnicities',
     'Ati' :'Local Ethnicities',
     'Kalinga-Guilayon' :'Local Ethnicities',
     'Agta-Labin' :'Local Ethnicities',
     'Diangan':'Local Ethnicities'
    
}

# Map the ethnicities to the new categories
data['Grouped_Ethnicity'] = data['Ethnicity'].map(ethnicity_group)

# Check the results
print(data[['Ethnicity', 'Grouped_Ethnicity']])
missing_groups = data[data['Grouped_Ethnicity'].isna()]['Ethnicity'].unique()

data.columns
data['Barangay_PSGC'] = data['Barangay_PSGC'].astype(str).replace(' ', '', regex=False)
data['Barangay_PSGC'] = data['Barangay_PSGC'].astype(int)

print(missing_groups)
data['Grouped_Ethnicity'].isnull().sum()


### CLEAN REGION OF DATA DATA FRAME###
region_mapping = region_mapping = {
    'Cordillera Administrative Region (CAR)': 'Cordillera Administrative Region',
    'National Capital Region (NCR)': 'National Capital Region',
    'Region I (Ilocos Region)': 'Region I - Ilocos Region',
    'Region II (Cagayan Valley)': 'Region II - Cagayan Valley',
    'Region III (Central Luzon)': 'Region III - Central Luzon',
    'Region IV-A (CALABARZON)': 'Region IV-A - Calabarzon',
    'MIMAROPA Region': 'Region IV-B - MIMAROPA',
    'Region V (Bicol Region)': 'Region V - Bicol Region',
    'Region VI (Western Visayas)': 'Region VI - Western Visayas',
    'Region VII (Central Visayas)': 'Region VII - Central Visayas',
    'Region VIII (Eastern Visayas)': 'Region VIII - Eastern Visayas',
    'Region IX (Zamboanga Peninsula)': 'Region IX - Zamboanga Peninsula',
    'Region X (Northern Mindanao)': 'Region X - Northern Mindanao',
    'Region XI (Davao Region)': 'Region XI - Davao Region',
    'Region XII (SOCCSKSARGEN)': 'Region XII - SOCCSKSARGEN',
    'Region XIII (Caraga)': 'Region XIII - Caraga Region',
    'Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)': 'Bangsamoro Autonomous Region in Muslim Mindanao'
}

# Create a new column with cleaned region names
data['Region-Final'] = data['Region'].replace(region_mapping)

### CREATE COMPLETE ADDRESS ###
data['Complete_Address'] = (
    data['Region-Final'] + ', ' +
    data['Province'] + ', ' +
    data['City/Municipality'] + ', ' +
    data['Barangay'])


data.columns


### RENAME THE COMPLETE ADDRESS ###

rename_add = {
    'Cordillera Administrative Region, Abra, Bangued, Tablac': 'Cordillera Administrative Region, Abra, Bangued, Tablac (Calot)',
    'Cordillera Administrative Region, Abra, Bangued, Cosili West': 'Cordillera Administrative Region, Abra, Bangued, Cosili West (Buaya)',
    'Cordillera Administrative Region, Abra, Bangued, Cosili East': 'Cordillera Administrative Region, Abra, Bangued, Cosili East (Proper)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sapa-Sapa, Latuan': 'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sapa-Sapa, Latuan (Suasang)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sapa-Sapa, Tangngah': 'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sapa-Sapa, Tangngah (Lalung Sikubong)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 2 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 2 Pob. (Consiliman)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 3 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 3 Pob. (Lalaud)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 1 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 1 Pob. (Nalasin)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 4 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 4 Pob. (Town Proper)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 5 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 5 Pob. (Bo. Barikir)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 6 Pob. ': 'Cordillera Administrative Region, Abra, Bangued, Zone 6 Pob. (Sinapangan)',
    'Cordillera Administrative Region, Abra, Bangued, Zone 7 Pob.': 'Cordillera Administrative Region, Abra, Bangued, Zone 7 Pob. (Baliling)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sitangkai, South Larap': 'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Sitangkai, South Larap (Larap)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Tandubas, Tangngah': 'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Tandubas, Tangngah (Tangngah Ungus Matata)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Languyan, Jakarta' : 'Bangsamoro Autonomous Region in Muslim Mindanao, Tawi-Tawi, Languyan, Jakarta (Lookan Latuan)',
    'Cordillera Administrative Region, Abra, Boliney, Poblacion': 'Cordillera Administrative Region, Abra, Boliney, Poblacion (Boliney)',
    'Cordillera Administrative Region, Abra, Bucloc, Lingey' : 'Cordillera Administrative Region, Abra, Bucloc, Lingay',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Parang, Poblacion':'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Parang, Poblacion (Parang)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Patikul, Buhanginan': 'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Patikul, Buhanginan (Darayan)',
    'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Siasi, Poblacion': 'Bangsamoro Autonomous Region in Muslim Mindanao, Sulu, Siasi, Poblacion (Campo Baro)'
}



data['Complete_Address']= data['Complete_Address'].replace(rename_add)
data.shape


# Check which addresses in `data` are not in `coords`
data_not_in_coords = data[~data['Complete_Address'].isin(coords['FINAL_ADDRESS'])]
print(data_not_in_coords)
data_not_in_coords.shape

# Print unique addresses in `data_not_in_coords`
unique_addresses = data_not_in_coords['Complete_Address'].unique()
print(unique_addresses)



### ASSIGN COORDINATES TO BLANK COORDS ###
# Define a dictionary with addresses and their respective coordinates
#(LONG,LAT)

long_dict = {'Cordillera Administrative Region, Ifugao, Asipulo, Liwon': 121.044,
'Cordillera Administrative Region, Kalinga, City of Tabuk, Lacnog West': 121.5586,
'National Capital Region, City of Navotas, City of Navotas, North Bay Boulevard North': 120.95,
'National Capital Region, City of Navotas, City of Navotas, NBBS Kaunlaran': 120.957,
'National Capital Region, City of Navotas, City of Navotas, Tanza 1': 120.9389,
'National Capital Region, City of Navotas, City of Navotas, NBBS Proper': 120.950292,
'Region I - Ilocos Region, Ilocos Norte, Dumalneg, Kalaw': 120.8,
'Region I - Ilocos Region, Ilocos Norte, Dumalneg, Quibel': 120.817,
'Region II - Cagayan Valley, Cagayan, Camalaniugan, Jurisdiccion': 121.6833,
'Region III - Central Luzon, Tarlac, Camiling, San Isidro': 120.4667,
'Region IV-A - Calabarzon, Rizal, Tanay, Madilay-dilay': 121.4414,
'Region IV-A - Calabarzon, Quezon, Panukulan, Rizal': 121.9667,
'Region IV-B - MIMAROPA, Occidental Mindoro, San Jose, Naibuan': 121.1833,
'Region X - Northern Mindanao, City of Iligan, City of Iligan, Tomas L. Cabili': 124.2278,
'Region XI - Davao Region, City of Davao, City of Davao, Santo Niño': 125.5,
'Region XII - SOCCSKSARGEN, Sultan Kudarat, City of Tacurong, Virginia Griño': 124.6667,
'Region XII - SOCCSKSARGEN, Sultan Kudarat, City of Tacurong, Enrique J.C. Montilla': 124.65,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Poblacion': 124.6333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Bagumbayan': 124.6167,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Bandara-Ingud': 124.5899,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Comara': 124.6333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Frankfort': 124.6833,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Lambanogan': 124.6667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Lico': 124.55,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Mansilano': 124.5833,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Natangcopan': 124.6167,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Pagonayan': 124.6333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Pagalamatan': 124.65,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Piagma': 124.5667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Punud': 124.6667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Ranao-Baning': 124.5667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Salam': 124.5948,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Sagua-an': 124.5902,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Sumugot': 124.6295}

lat_dict = {'Cordillera Administrative Region, Ifugao, Asipulo, Liwon': 16.7343,
'Cordillera Administrative Region, Kalinga, City of Tabuk, Lacnog West': 17.4164,
'National Capital Region, City of Navotas, City of Navotas, North Bay Boulevard North': 14.65,
'National Capital Region, City of Navotas, City of Navotas, NBBS Kaunlaran': 14.643,
'National Capital Region, City of Navotas, City of Navotas, Tanza 1': 14.6753,
'National Capital Region, City of Navotas, City of Navotas, NBBS Proper': 14.648018,
'Region I - Ilocos Region, Ilocos Norte, Dumalneg, Kalaw': 18.5167,
'Region I - Ilocos Region, Ilocos Norte, Dumalneg, Quibel': 18.5,
'Region II - Cagayan Valley, Cagayan, Camalaniugan, Jurisdiccion': 18.2333,
'Region III - Central Luzon, Tarlac, Camiling, San Isidro': 15.6667,
'Region IV-A - Calabarzon, Rizal, Tanay, Madilay-dilay': 14.5647,
'Region IV-A - Calabarzon, Quezon, Panukulan, Rizal': 15.0167,
'Region IV-B - MIMAROPA, Occidental Mindoro, San Jose, Naibuan': 12.4833,
'Region X - Northern Mindanao, City of Iligan, City of Iligan, Tomas L. Cabili': 8.2056,
'Region XI - Davao Region, City of Davao, City of Davao, Santo Niño': 7.0833,
'Region XII - SOCCSKSARGEN, Sultan Kudarat, City of Tacurong, Virginia Griño':6.7167,
'Region XII - SOCCSKSARGEN, Sultan Kudarat, City of Tacurong, Enrique J.C. Montilla': 6.6667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Poblacion': 7.8167,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Bagumbayan': 7.7167,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Bandara-Ingud': 7.8006,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Comara': 7.8167,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Frankfort': 7.7833,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Lambanogan': 7.8,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Lico': 7.6667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Mansilano': 7.8667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Natangcopan': 7.8333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Pagonayan': 7.7667,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Pagalamatan': 7.8333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Piagma': 7.7333,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Punud': 7.8,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Ranao-Baning': 7.85,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Salam': 7.8280,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Sagua-an': 7.6666,
'Bangsamoro Autonomous Region in Muslim Mindanao, Lanao del Sur, Amai Manabilang, Sumugot': 7.7494}

data.rename(columns={'Complete_Address': 'FINAL_ADDRESS'}, inplace=True)
data = pd.merge(data, coords[['FINAL_ADDRESS', 'LATITUDE']], on='FINAL_ADDRESS', how='left')
data = pd.merge(data, coords[['FINAL_ADDRESS', 'LONGITUDE']], on='FINAL_ADDRESS', how='left')
data['LONGITUDE'] = data['LONGITUDE'].fillna(data['FINAL_ADDRESS'].map(long_dict))
data['LATITUDE'] = data['LATITUDE'].fillna(data['FINAL_ADDRESS'].map(lat_dict))


data.columns
data.info()    
data.isnull().sum()

# Filter rows where LATITUDE and LONGITUDE are both NaN
filtered_data = data[data['LATITUDE'].isna() & data['LONGITUDE'].isna()]


# Get unique FINAL_ADDRESS values
unique_addresses = filtered_data['FINAL_ADDRESS'].unique()
unique_addresses
# Save to CSV
unique_addresses_df = pd.DataFrame(unique_addresses)
unique_addresses_df
# unique_addresses_df.to_csv(x, index=False)

data.to_csv(output, index=False)
