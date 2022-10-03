from time import sleep
import pandas as pd
import numpy as np
from tqdm import tqdm

pd.options.mode.chained_assignment = None

print("Premier League 2022-23 Forward Statistics Setup\n")

print("The setup extracts data from FBRef.com and the time taken to complete the process varies on the internet connection.\n")

print("Would you like to update the player table? (Select Y if not updated previously)")

x = input("Y/N: ")

if (x=="Y"):
    prem_link = {
        'Mohamed Salah':['https://fbref.com/en/players/e342ad68/Mohamed-Salah#scout_summary_AM','Liverpool'],
        'Luis Diaz':['https://fbref.com/en/players/4a1a9578/Luis-Diaz#scout_summary_AM', 'Liverpool'],
        'Darwin Nunez':['https://fbref.com/en/players/4d77b365/Darwin-Nunez#scout_summary_FW', 'Liverpool'],
        'Diogo Jota':['https://fbref.com/en/players/178ae8f8/Diogo-Jota#scout_summary_FW', 'Liverpool'],
        'Roberto Firmino':['https://fbref.com/en/players/4c370d81/Roberto-Firmino#scout_summary_FW', 'Liverpool'],
        'Bukayo Saka':['https://fbref.com/en/players/bc7dc64d/Bukayo-Saka#scout_summary_AM', 'Arsenal'],
        'Martinelli':['https://fbref.com/en/players/48a5a5d6/Martinelli#scout_summary_AM', 'Arsenal'],
        'Gabriel Jesus':['https://fbref.com/en/players/b66315ae/Gabriel-Jesus#scout_summary_FW', 'Arsenal'],
        'Eddie Nketiah':['https://fbref.com/en/players/a53649b7/Eddie-Nketiah#scout_summary_FW', 'Arsenal'],
        'Emile Smith Rowe':['https://fbref.com/en/players/17695062/Emile-Smith-Rowe#scout_summary_AM', 'Arsenal'],
        'Ollie Watkins':['https://fbref.com/en/players/aed3a70f/Ollie-Watkins#scout_summary_FW', 'Aston Villa'],
        'Danny Ings':['https://fbref.com/en/players/07802f7f/Danny-Ings#scout_summary_FW', 'Aston Villa'],
        'Leon Bailey':['https://fbref.com/en/players/3a233281/Leon-Bailey#scout_summary_AM', 'Aston Villa'],
        'Emi Buendia':['https://fbref.com/en/players/66b76d44/Emi-Buendia#scout_summary_AM', 'Aston Villa'],
        'Philippe Coutinho':['https://fbref.com/en/players/0ef89a37/Philippe-Coutinho#scout_summary_AM', 'Aston Villa'],
        'Marcus Tavernier':['https://fbref.com/en/players/5c0da4a4/Marcus-Tavernier#scout_summary_AM', 'Bournemouth'],
        'Ivan Toney':['https://fbref.com/en/players/e09f279b/Ivan-Toney#scout_summary_FW', 'Brentford'],
        'Yoane Wissa':['https://fbref.com/en/players/2500cef9/Yoane-Wissa#scout_summary_AM', 'Brentford'],
        'Bryan Mbeumo':['https://fbref.com/en/players/6afaebf2/Bryan-Mbeumo#scout_summary_FW', 'Brentford'],
        'Danny Welbeck':['https://fbref.com/en/players/ce5143da/Danny-Welbeck#scout_summary_FW', 'Brighton'],
        'Enock Mwepu':['https://fbref.com/en/players/1d5cab82/Enock-Mwepu#scout_summary_MF', 'Brighton'],
        'Neal Maupay':['https://fbref.com/en/players/4bcf39f6/Neal-Maupay#scout_summary_FW', 'Brighton'],
        'Leandro Trossard':['https://fbref.com/en/players/38ceb24a/Leandro-Trossard#scout_summary_AM', 'Brighton'],
        'Armando Broja':['https://fbref.com/en/players/97220da2/Armando-Broja#scout_summary_FW', 'Chelsea'],
        'Raheem Sterling':['https://fbref.com/en/players/b400bde0/Raheem-Sterling#scout_summary_AM', 'Chelsea'],
        'Kai Havertz':['https://fbref.com/en/players/fed7cb61/Kai-Havertz#scout_summary_FW', 'Chelsea'],
        'Christian Pulisic':['https://fbref.com/en/players/1bf33a9a/Christian-Pulisic#scout_summary_AM', 'Chelsea'],
        'Mason Mount':['https://fbref.com/en/players/9674002f/Mason-Mount#scout_summary_AM', 'Chelsea'],
        'Odsonne Edouard':['https://fbref.com/en/players/0562b7f1/Odsonne-Edouard#scout_summary_FW', 'Crystal Palace'],
        'Jean-Philippe Mateta':['https://fbref.com/en/players/50e6dc35/Jean-Philippe-Mateta#scout_summary_FW', 'Crystal Palace'],
        'Wilfried Zaha':['https://fbref.com/en/players/b2bc3b1f/Wilfried-Zaha#scout_summary_AM', 'Crystal Palace'],
        'Jordan Ayew':['https://fbref.com/en/players/da052c14/Jordan-Ayew#scout_summary_AM', 'Crystal Palace'],
        'Eberechi Eze':['https://fbref.com/en/players/ae4fc6a4/Eberechi-Eze#scout_summary_MF', 'Crystal Palace'],
        'Michael Olise':['https://fbref.com/en/players/c4486bac/Michael-Olise#scout_summary_AM', 'Crystal Palace'],
        'Anthony Gordon':['https://fbref.com/en/players/2bd83368/Anthony-Gordon#scout_summary_AM', 'Everton'],
        'Demarai Gray':['https://fbref.com/en/players/4468ec10/Demarai-Gray#scout_summary_AM', 'Everton'],
        'Dwight McNeil':['https://fbref.com/en/players/fc15fb84/Dwight-McNeil#scout_summary_AM', 'Everton'],
        'Salomón Rondón':['https://fbref.com/en/players/b318a643/Salomon-Rondon#scout_summary_FW', 'Everton'],
        'Aleksandar Mitrovic':['https://fbref.com/en/players/3925dbd6/Aleksandar-Mitrovic#scout_summary_FW', 'Fulham'],
        'Bobby Reid':['https://fbref.com/en/players/0f7533cd/Bobby-Reid#scout_summary_AM', 'Fulham'],
        'Daniel James':['https://fbref.com/en/players/c931d9f9/Daniel-James#scout_summary_AM', 'Fulham'],
        'Jack Harrison':['https://fbref.com/en/players/aa849a12/Jack-Harrison#scout_summary_AM', 'Leeds'],
        # 'Patrick Bamford':['https://fbref.com/en/players/93feac6e/Patrick-Bamford#scout_summary_FW', 'Leeds'],
        'Joe Gelhardt':['https://fbref.com/en/players/01962d0d/Joe-Gelhardt#scout_summary_FW', 'Leeds'],
        'Rodrigo':['https://fbref.com/en/players/1fb1c435/Rodrigo#scout_summary_AM', 'Leeds'],
        'Brenden Aaronson':['https://fbref.com/en/players/5bc43860/Brenden-Aaronson#scout_summary_AM', 'Leeds'],
        'Jamie Vardy':['https://fbref.com/en/players/45963054/Jamie-Vardy#scout_summary_FW', 'Leicester'],
        'Patson Daka':['https://fbref.com/en/players/ca45605e/Patson-Daka#scout_summary_FW', 'Leicester'],
        'Kelechi Iheanacho':['https://fbref.com/en/players/c92e1a31/Kelechi-Iheanacho#scout_summary_FW', 'Leicester'],
        'Dennis Praet':['https://fbref.com/en/players/86695068/Dennis-Praet#scout_summary_AM', 'Leicester'],
        'Harvey Barnes':['https://fbref.com/en/players/3ea50f67/Harvey-Barnes#scout_summary_AM', 'Leicester'],
        'Erling Haaland':['https://fbref.com/en/players/1f44ac21/Erling-Haaland#scout_summary_FW', 'Manchester City'],
        'Riyad Mahrez':['https://fbref.com/en/players/892d5bb1/Riyad-Mahrez#scout_summary_AM', 'Manchester City'],
        'Jack Grealish':['https://fbref.com/en/players/b0b4fd3e/Jack-Grealish#scout_summary_AM', 'Manchester City'],
        'Phil Foden':['https://fbref.com/en/players/ed1e53f3/Phil-Foden#scout_summary_AM', 'Manchester City'],
        'Bernardo Silva':['https://fbref.com/en/players/3eb22ec9/Bernardo-Silva#scout_summary_MF', 'Manchester City'],
        'Marcus Rashford':['https://fbref.com/en/players/a1d5bd30/Marcus-Rashford#scout_summary_AM', 'Manchester United'],
        'Jadon Sancho':['https://fbref.com/en/players/dbf053da/Jadon-Sancho#scout_summary_AM', 'Manchester United'],
        'Anthony Elanga':['https://fbref.com/en/players/2fba6108/Anthony-Elanga#scout_summary_AM', 'Manchester United'],
        'Cristiano Ronaldo':['https://fbref.com/en/players/dea698d9/Cristiano-Ronaldo#scout_summary_FW', 'Manchester United'],
        'Antony':['https://fbref.com/en/players/99127249/Antony#scout_summary_AM', 'Manchester United'],
        'Anthony Martial':['https://fbref.com/en/players/8b788c01/Anthony-Martial#scout_summary_AM', 'Manchester United'],
        'Bruno Fernandes':['https://fbref.com/en/players/507c7bdf/Bruno-Fernandes#scout_summary_AM', 'Manchester United'],
        'Miguel Almiron':['https://fbref.com/en/players/862a1c15/Miguel-Almiron#scout_summary_AM', 'Newcastle'],
        'Allan Saint-Maximin':['https://fbref.com/en/players/2b16cb1a/Allan-Saint-Maximin#scout_summary_AM', 'Newcastle'],
        'Callum Wilson':['https://fbref.com/en/players/c596fcb0/Callum-Wilson#scout_summary_FW', 'Newcastle'],
        'Ryan Fraser':['https://fbref.com/en/players/d56543a0/Ryan-Fraser#scout_summary_AM', 'Newcastle'],
        'Alexander Isak':['https://fbref.com/en/players/8e92be30/Alexander-Isak#scout_summary_FW', 'Newcastle'],
        'Chris Wood':['https://fbref.com/en/players/4e9a0555/Chris-Wood#scout_summary_FW', 'Newcastle'],
        'Jacob Murphy':['https://fbref.com/en/players/de112b84/Jacob-Murphy#scout_summary_AM', 'Newcastle'],
        'Taiwo Awoniyi':['https://fbref.com/en/players/e5478b87/Taiwo-Awoniyi#scout_summary_FW', 'Nottingham'],
        'Emmanuel Dennis':['https://fbref.com/en/players/2c44a35d/Emmanuel-Dennis#scout_summary_AM', 'Nottingham'],
        'Brennan Johnson':['https://fbref.com/en/players/0cd31129/Brennan-Johnson#scout_summary_FW', 'Nottingham'],
        'Jesse Lingard':['https://fbref.com/en/players/810e3c74/Jesse-Lingard#scout_summary_AM', 'Nottingham'],
        'Che Adams':['https://fbref.com/en/players/f2bf1b0f/Che-Adams#scout_summary_FW', 'Southampton'],
        'Adam Armstrong':['https://fbref.com/en/players/68c720b5/Adam-Armstrong#scout_summary_FW', 'Southampton'],
        'Mohamed Elyounoussi':['https://fbref.com/en/players/68dc0dac/Mohamed-Elyounoussi#scout_summary_AM', 'Southampton'],
        'Sekou Mara':['https://fbref.com/en/players/3544641e/Sekou-Mara#scout_summary_FW', 'Southampton'],
        'Joe Aribo':['https://fbref.com/en/players/328f7d51/Joe-Aribo#scout_summary_AM', 'Southampton'],
        'Stuart Armstrong':['https://fbref.com/en/players/97333cf5/Stuart-Armstrong#scout_summary_AM', 'Southampton'],
        'Harry Kane':['https://fbref.com/en/players/21a66f6a/Harry-Kane#scout_summary_FW', 'Tottenham'],
        'Richarlison':['https://fbref.com/en/players/fa031b34/Richarlison#scout_summary_FW', 'Tottenham'],
        'Son Heung-min':['https://fbref.com/en/players/92e7e919/Son-Heung-min#scout_summary_AM', 'Tottenham'],
        'Dejan Kulusevski':['https://fbref.com/en/players/df3cda47/Dejan-Kulusevski#scout_summary_AM', 'Tottenham'],
        'Lucas Moura':['https://fbref.com/en/players/2b622f01/Lucas-Moura#scout_summary_AM', 'Tottenham'],
        'Jarrod Bowen':['https://fbref.com/en/players/79c84d1c/Jarrod-Bowen#scout_summary_AM', 'West Ham'],
        'Michail Antonio':['https://fbref.com/en/players/ac05f970/Michail-Antonio#scout_summary_FW', 'West Ham'],
        'Gianluca Scamacca':['https://fbref.com/en/players/8790f988/Gianluca-Scamacca#scout_summary_FW', 'West Ham'],
        'Maxwel Cornet':['https://fbref.com/en/players/beb391dd/Maxwel-Cornet#scout_summary_FW', 'West Ham'],
        'Said Benrahma':['https://fbref.com/en/players/5a04fd92/Said-Benrahma#scout_summary_AM', 'West Ham'],
        'Pablo Fornals':['https://fbref.com/en/players/82927de4/Pablo-Fornals#scout_summary_AM', 'West Ham'],
        'Raul Jimenez':['https://fbref.com/en/players/b561db50/Raul-Jimenez#scout_summary_FW', 'Wolves'],
        'Hwang Hee-chan':['https://fbref.com/en/players/169fd162/Hwang-Hee-chan#scout_summary_AM', 'Wolves'],
        'Sasa Kalajdzic':['https://fbref.com/en/players/15f24fe7/Sasa-Kalajdzic#scout_summary_FW', 'Wolves'],
        'Pedro Neto':['https://fbref.com/en/players/7ba2eaa9/Pedro-Neto#scout_summary_AM', 'Wolves'],
        'Goncalo Guedes':['https://fbref.com/en/players/e6bc67d7/Goncalo-Guedes#scout_summary_FW', 'Wolves'],
        'Daniel Podence':['https://fbref.com/en/players/7fcc71d8/Daniel-Podence#scout_summary_AM', 'Wolves'],
        'Adama Traore':['https://fbref.com/en/players/9a28eba4/Adama-Traore#scout_summary_AM', 'Wolves']
    }

    stats = {'Statistics': ['Non-Penalty Goals', 'Non-Penalty xG', 'Shots Total', 'Assists', 'xG Assisted', 'npxG + xA', 'Shot-Creating Actions', '', 'Passes Attempted', 'Pass Completion %', 'Progressive Passes', 'Progressive Carries', 'Dribbles Completed', 'Touches (Att Pen)', 'Progressive Passes Rec', '', 'Pressures', 'Tackles', 'Interceptions', 'Blocks', 'Clearances', 'Aerials won', 'Team']}
    prem_df = pd.DataFrame(stats)

    for i in tqdm(prem_link, desc = "Your player table is being updated..."):
        x = pd.read_html(prem_link.get(i)[0])[0]
        prem_df[i] = x['Per 90']
        tp = prem_df[i][9]
        tp = float(tp.strip()[:2])/100
        prem_df[i][9] = tp
        prem_df[i] = pd.to_numeric(prem_df[i], errors='ignore')
        prem_df[i][22] = prem_link.get(i)[1]

    prem_df.dropna(inplace=True)
    prem_df.insert(1, "Select", np.nan)

    prem_df.to_csv('Leagues/Premier League/prem_fw_py.csv')
print("Your table has been updated.\n")
print("Please run PremMatrix.Rmd to access your visualizatons.")

sleep(5)

exit()