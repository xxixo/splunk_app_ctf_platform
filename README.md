# Splunk apps for making custom CTF

Splunk apps that make your custom CTF easy.

---

## How to start

In install standalone splunk with `$SPLUNK_HOME=/opt/splunk/` version 9.x (8.x not test) install apps. 


```
cd /opt/splunk/etc/apps/
git clone https://github.com/xxixo/splunk_app_ctf_platform.git
/opt/splunk/bin/splunk restart
```
Or you can easy install its like app from Web.
<p align="center">
<img width="2526" alt="Screenshot 2023-07-28 at 12 50 04" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/b4b76e39-0598-44a5-ace9-98ed0a8dcd86">
</p>

<p align="center">
<img width="666" alt="Screenshot 2023-07-28 at 12 50 52" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/3085d5cb-ecdf-405b-ae29-486269629e6f">
</p>

<p align="center">
<img width="2532" alt="Screenshot 2023-07-28 at 12 51 17" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/b14cf04f-eef3-43f1-af5f-597cf7bb202e">
</p>

<p align="center">
<img width="275" alt="Screenshot 2023-07-28 at 12 51 48" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/a7a06e9b-6ec3-4afc-85bd-bcda69fde497">
</p>

<p align="center">
<img width="2525" alt="Screenshot 2023-07-28 at 12 52 05" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/c081e5cf-c6d0-457d-8ecc-502b5174ac24">
</p>

---


## Users permitions

CTF administrator user must have `admin` permition (becouse he must have access to change in "Important objects". All other CTF players must have only `user` permition. With this permition thay can meke research in splunk and dont have access to answers lookup.
<p align="center">
<img width="571" alt="Screenshot 2023-07-28 at 13 23 47" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/9a4b83fe-ab02-49c2-9b0d-1d271072059f">
</p>
<p align="center">
<img width="2533" alt="Screenshot 2023-07-28 at 13 36 16" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/4a7a6c74-7575-461f-ba8d-57fca2144c55">
</p>
<p align="center">
<img width="2526" alt="Screenshot 2023-07-28 at 13 37 12" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/974d74e5-2c40-4970-a657-ad0b8d5cc3f0">
</p>

<br>

---

## Important objects

The are two important lookup that need edit to manage your own CTF. Its easy to do with <a href="https://splunkbase.splunk.com/app/1724">lookups editor</a> .

`ctf_questions.csv` - the questions list that be aviable in your CTF.
<p align="center">
<img width="904" alt="Screenshot 2023-07-28 at 12 38 05" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/9942aec6-8b50-43aa-be4f-2ba1773d928f">
</p>

>It is important fill this tables how shows in screanshot.

<br>

`ctf_answers.csv` - the answers list.
<p align="center">
<img width="505" alt="Screenshot 2023-07-28 at 12 39 48" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d85fb9ce-9bf8-48ba-b054-ed16d6c1ab89">
</p>

>It is important fill this tables how shows in screanshot.

---

## Web navigation

After first installing you can go to start page of app.
<p align="center">
<img width="2530" alt="Screenshot 2023-07-28 at 12 53 33" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/f2994016-f948-431f-b44b-67e6a4eedbea">
</p>
You cat see that user Administrator already have 100 points. 

In the top user navigation bar exist 2 page "Scoreboard" and "Tasks". 



#### Scoreboard

Shows table of users score.
<p align="center">
<img width="2525" alt="Screenshot 2023-07-28 at 12 56 24" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/4572597d-cd4a-4f73-af9a-09862bdbabcb">
</p>


#### Tasks

Shows all answer that contains in our CTF (`ctf_questions.csv`). Also its shows values of each question numbers of user tryies and is this questions already slowed.
<p align="center">
<img width="2527" alt="Screenshot 2023-07-28 at 12 59 07" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/22375533-e929-4af6-b9da-bf9eaba79150">
</p>

After user click at one of aviable question he take the answer page.


#### Answer

`Not started` - when user not try to answer
<p align="center">
<img width="2523" alt="Screenshot 2023-07-28 at 13 00 33" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d5b179aa-640d-4d2e-9b95-11d7bf686e2d">
</p>

`Wrong answer` - if user make one or more wrong tryies

<p align="center">
<img width="2514" alt="Screenshot 2023-07-28 at 13 05 07" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d7ffe809-9b40-4ad2-a892-d97276195d50">
</p>

`Slowed`- if user make correct answer

<p align="center">
<img width="2524" alt="Screenshot 2023-07-28 at 13 14 57" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/048e916c-01a8-4453-9f01-f2b5d2e843b2">
</p>

After user make correct answer he redirected to "Tasks" dashboard. And if he try go to already slowed question he dont have access to answer form.

<p align="center">
<img width="2528" alt="Screenshot 2023-07-28 at 13 17 36" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/760676a4-8667-4002-a49a-713be6a9ab60">
</p>

---

## App structure

<p align="center">
<img width="546" alt="Screenshot 2023-07-28 at 14 30 36" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/5f2a3057-8c47-403c-9575-0d81607ea553">
</p>

App contains one python script `/ctf_platform/appserver/controler/ctf_controler.py` - this is the answer checker script. 

All users activity writes to `/ctf_platform/answers/ctf_answers.log` - for this file in `/ctf_platform/defalut/inputs.conf` exist monitor.

<p align="center">
<img width="621" alt="Screenshot 2023-07-28 at 14 35 31" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/3241164f-7cd6-4f9a-b98a-50ad40963be9">
</p>

Data from this file store in index `ctf_answers`. This index described in `/ctf_platform/default/indexes.conf`. All indexed files that will be created in this index will be contains at `/ctf_platform/var/lib/splunk/ctf_answer/`.

---

## How to clear data and start new CTF ? 

1. Clear file `/ctf_platform/answers/ctf_answers.log`

```
rm -f $SPLUNK_HOME/etc/apps/ctf_platform/answers/ctf_answers.log
touch $SPLUNK_HOME/etc/apps/ctf_platform/answers/ctf_answers.log
```
2. Clear index `ctf_answers`
```
rm -rf $SPLUNK_HOME/etc/apps/ctf_platform/var/lib/splunk/ctf_answer
```
3. Make change in lookups `ctf_questions.csv`, `ctf_answers.csv`
4. Restart splunk
```
$SPLUNK_HOME/bin/splunk restart
```

