# Stacc code challenge 2021

## Oppgavebeskrivelse
> Jeg har valgt å løse oppgave b), altså å implementere mitt eget KYC API. Jeg ga også oppgave a) et forsøk, selv om jeg har veldig lite erfaring med front-end. Mer om dette i kommentarene under.
> Resultatet er en Flask web-app som inneholder både en søke-app og et REST API. Prosjektet inneholder også en modul "stacc.api.py" som henter og håndterer data fra Stacc KYC API (https://documenter.getpostman.com/view/9949536/UV5TEzGZ#61b845de-189f-4e71-85ef-c920f815eeb2).

## Hvordan kjøre prosjektet
Prerequisites:
  * Python 3
  * Virtualenv (installasjon virtualenv: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

1. Klon prosjektet fra https://github.com/thomassi98/Stacc-Coding-Challenge-KYC.git. (eks. git clone 'https://github.com/thomassi98/Stacc-Coding-Challenge-KYC.git')
2. Lag og start virtual environment (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Installer python-pakker:
    * Kjør pip install -r requirements.txt
4. Kjør app.py (main script).
5. Gå inn på localhost:5000 og voilá: her skal min web-app dukke opp :)

API endpoints:
* localhost:5000/API/PEP/name=name 
* localhost:5000/API/roles/org_num=org_num
* localhost:5000/API/company/org_num=org_num

## Kommentarer
Noen spesielle valg du ønsker å beskrive/forsvare?
> Jeg brukte en del tid på å sette meg inn i Flask og web-apper generelt da jeg ikke har jobbet med akkurat dette før. Dette merkes nok mest i oppgave a) der man kan si at designet ble veldig "minimalistisk". Til mitt forsvar er delene jeg prioriterte vekk (eks. pen formatering av HTML-tabeller) ikke viktig for funksjonaliteten til programmet, og andre moduler er ikke noe påvirket av disse.
