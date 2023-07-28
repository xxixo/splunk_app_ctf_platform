# Splunk apps for making custom CTF

Splunk apps that make your custom CTF easy.

## How to start

In install standalone splunk with `$SPLUNK_HOME=/opt/splunk/` version 9.x (8.x not test) install apps. 


```
cd /opt/splunk/etc/apps/
git clone https://github.com/xxixo/splunk_app_ctf_platform.git
/opt/splunk/bin/splunk restart
```
Or you can easy install its like app from Web.

<img width="2526" alt="Screenshot 2023-07-28 at 12 50 04" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/b4b76e39-0598-44a5-ace9-98ed0a8dcd86">

<img width="666" alt="Screenshot 2023-07-28 at 12 50 52" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/3085d5cb-ecdf-405b-ae29-486269629e6f">

<img width="2532" alt="Screenshot 2023-07-28 at 12 51 17" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/b14cf04f-eef3-43f1-af5f-597cf7bb202e">

<img width="275" alt="Screenshot 2023-07-28 at 12 51 48" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/a7a06e9b-6ec3-4afc-85bd-bcda69fde497">

<img width="2525" alt="Screenshot 2023-07-28 at 12 52 05" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/c081e5cf-c6d0-457d-8ecc-502b5174ac24">


<br>

## Important objects

The are two important lookup that need edit to manage your own CTF. Its easy to do with <a href="https://splunkbase.splunk.com/app/1724">lookups editor</a> .

`ctf_questions.csv` - the questions list that be aviable in your CTF.

<img width="904" alt="Screenshot 2023-07-28 at 12 38 05" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/9942aec6-8b50-43aa-be4f-2ba1773d928f">

>It is important fill this tables how shows in screanshot.

<br>

`ctf_answers.csv` - the answers list.

<img width="505" alt="Screenshot 2023-07-28 at 12 39 48" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d85fb9ce-9bf8-48ba-b054-ed16d6c1ab89">

>It is important fill this tables how shows in screanshot.

## Web navigation

After first installing you can go to start page of app.

<img width="2530" alt="Screenshot 2023-07-28 at 12 53 33" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/f2994016-f948-431f-b44b-67e6a4eedbea">

You cat see that user Administrator already have 100 points. 

In the top user navigation bar exist 2 page "Scoreboard" and "Tasks". 

### Scoreboard

Shows table of users score.

<img width="2525" alt="Screenshot 2023-07-28 at 12 56 24" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/4572597d-cd4a-4f73-af9a-09862bdbabcb">

### Tasks

Shows all answer that contains in our CTF (`ctf_questions.csv`). Also its shows values of each question numbers of user tryies and is this questions already slowed.

<img width="2527" alt="Screenshot 2023-07-28 at 12 59 07" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/22375533-e929-4af6-b9da-bf9eaba79150">


After user click at one of aviable question he take the answer page.

### Answer

This siple page contains question text, status (Not started - when user not try to answer, Wrong answer - if user make one or more wrong tryies, Slowed - if user make correct answer)

<img width="2523" alt="Screenshot 2023-07-28 at 13 00 33" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d5b179aa-640d-4d2e-9b95-11d7bf686e2d">

<img width="2514" alt="Screenshot 2023-07-28 at 13 05 07" src="https://github.com/xxixo/splunk_app_ctf_platform/assets/131694570/d7ffe809-9b40-4ad2-a892-d97276195d50">










