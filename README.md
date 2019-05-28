# Kapteenin viikkomaili
Tämä viikkomaili toimii Jekyllillä, jota Github tukee suoraan.

## Kansio sisältö

### includes
Sisältää footerin headerin ja head-osion sivusta.
Scripti importit ja css importit voi mukavasti pistää headiin

### layouts
Sivuston eri ulkoasut ovat täällä. Tärkeät filut ovat boldattu
* archive.html: Ei tällä hetkellä käytössä (Luultavasti voi poistaa)
* default.html: Käytetään sivulle yhteisien elementtien luomiseen
* <b>home.html</b>: On etusivu. Listaa kaikki tähän asti tulleet blogi-postaukset
* page.html: Ei ole käytössä (Luultavasti voi poistaa)
* <b>post.html</b>: On aina yksi postaus. Se määrittelee postauksen ulkoasun, ja miten markdown käyttäytyy sivulla.

### posts
Jokainen blogi postaus tänne muodossa yyyy-mm-dd-hieno-otsikko-tahan.markdown.
Postaus kirjoitetaan markdownissa, ja alkuun pitää aina muistaa laittaa ns. "front matter" eli:
~~~~
---
layout: post
title:  "Kapteenin viikkomaili 1/2018 - Koulun alkua"
date:   2018-09-10
categories: fuksit 
---
~~~~

Jekyll käyttää kramdown nimistä markdown kääntäjää, joten siihen liittyvät syntaxit löytyvät osoitteesta: <https://kramdown.gettalong.org/>

### sass
Sivun tyylitykset tänne. Sieltä löytyy esim. responsiivisen iframen css ja muuta olennaista mihin vuoden aikana törmäsi.

### assets
Blogien kuvat ja teeman kuvat löytyvät täältä. Postauksen kuvat löytyvät sen yyyy## nimisen kansion takaa (## tarkoittaa viikkomailin numeroa).

img-kansiossa on teemaan liittyviä kuvia.

## Miten koko homma siis toimii?

### Ensimmäiseksi
Forkkaa vaikka tämä repo itsellesi. Sitten mene repon asetuksiin kohtaan <i>Github Pages</i>
Sieltä valitse <b>sourceksi</b> master-branch ja <b>teemaksi</b> Minima. Jokin pohjateema pitää valita, niin Minima ei tuo mitään ylimääräistä.

Onnittelut, Githubin osalta kaikki on tehty!

Seuraavaksi mennään config.yml tiedostoon päivittäämään omat tiedot
Täältä voit intuitiivisesti muokata tiedot itsellesi sopiviksi.
Tärkeimmät osuudet ovat email, edition, title, baseurl ja url.

Muut asetukset toimivat hyvin sellaisinaan.

### Postauksen luominen
Jokainen uusi postaus on oma tiedostonsa posts-kansiossa. Jekyll osaa automaattisesti löytää ne sieltä, ja kääntää sivulle.
Tiedostonimen muoto on yyyy-mm-dd-hieno-otsikko.markdown.

Esimerkkiä postauksesta kannattaa katsoa tästä reposta.

Kun aloitat pistä päälle jekyll tässä kansiossa:

`jekyll serve` 

Niin saat reaaliaikaisen sivun pystyyn. Helpottaa huomattavasti työskentelyä.

Kun olet saanut postauksen tehtyä kuvine ja kaikkineen, kommitoi se ja puske. Github tekee kaiken sen jälkeen puolestasi.

Seuraavaksi navigoi omalle github-pages sivustollesi. Sivujen pitäisi nyt näkyä siellä. Linkin sinne löydät repon asetuksista kohdasta <i>Github Pages</i>

Huomioita! 

Jos pistät front-matteriin päiväyksen, joka on tulevaisuudessa, se EI näy etusivulla.

Jos sivu ei päivity pushin jälkeen, niin kokeile pistää perään tyhjä kommitti. Se joskus auttaa triggeröimään buildauksen Githubissa

### Sähköposti
Tuolta löytyy python filu mail.py, millä voi poistaa markdownin postauksesta. Jaksoin käyttää sitä ehkä kuukauden, kunnes lähetin sähköpostissa vain linkin sivustolle. Ihan turhaa sitä kirjoittaa viikkomailia kahteen paikkaan.


## Tunnettuja ongelmia
Telegram excerptit eivät toimi vaikka og-tagien pitäisi olla okein. En tiedä yhtään miksi ei toimi, joten sitä saa kokeilla korjata.
