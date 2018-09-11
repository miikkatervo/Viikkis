# Kapteenin viikkomaili

Tällä jekyll pohjalla saat helposti hyvännäköisen ulkoasun omalle viikkomailille.

Aluksi luo uusi repo viikkomailille

Aluksi muista asentaa bulma
<code>npm install</code> komennolla

Seuraavaksi voit aloittaa postauksien kirjoittamisen
Kaikki uudet julkaisut menevät _posts kansioon. Sinne kirjoitetaan markdownia. Jekyll käyttää markdownin kääntämiseen kramdown projekia, eli voit katsoa niiden sivuilta, millä tavalla eri tyylejä kirjoitetaan.

Kaikkien otsikointien tagit tulevat automaattisesti. Tapahtumien fuksipisteet toimivat eri tavalla. Niissä pitää lisätä pisteen tunniste lauseen alle.
Esim.
Tästä tapahtumasta saat vapaan pisteen
{: .vapaa}

Uudet julkaisut pitää nimetä YYYY-MM-DD-julkaisun-nimi. ja jokaisen alussa pitää olla tunniste, kuten alla
<code>
---
layout: post
title:  "Kapteenin viikkomaili 1/2018 - Esimerkki"
date:   2018-09-10
categories: fuksit
---
</code>

Kun uusi julkaisu on tehty, pitää vain commitoida se ja pushata gittiin.

Tässä vaiheessa, jos ei ole sitä jo aikaisemmin tehnyt, pitää yhdistää github repo github pagesiin.
Se löytyy settings-> GitHub Pages -> Source -> master branch

Tämän jälkeen kaiken pitäisi toimia. Jos ongelmia tulee, niin jekylin omilta sivuilta löytyy paljon tietoa.
