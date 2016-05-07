# IB030-sentiment  

Programátorský úkol do IB030.  
Program na analýzu sentimentu v českých textech, zejména pak v recenzích filmů.  


Prerekvizity:
Je nutne mit nainstalovanou knihovnu nltk pro python
pip install nltk

Instalace:

wget https://github.com/asketak/IB030-sentiment/archive/master.zip
unzip master.zip
cd IB030-sentiment-master/

Použití:  


Repozitář obsahuje:  

classifier.py:  
  
	jednoduchá klasifikace na základě četnosti výskytu slov  
  
classifier_bigrams.py   
	klasifikuje na základě dvojic slov, je tak schopný odlišit kontext slova "rád" ve spojeních "nemám rád" a "mám rád".  

classify_first_n.py:  
	snaha zbavit se šumu a slov, které se vyskytují v obou kategoriích  
	klasifikuje na základě 10 000 "nejvyhraněnějších" slov  

Všechny programy dělí data na data pro učení a data pro testovaní v poměru daném proměnnou `train_test_ratio`  

csfd_fetcher.py - program pro stahování komentáře a příslušného hodnocení z csfd.cz  
data - adresář s daty, která byla použita a mohou sloužit dále pro testování  

scraped_data.txt - neupravená stáhnutá data z csfd_fetcher.py  
0-5.txt - data rozdělená dle hodnocení  

movie_reviews - data rozdělená na pozitivní sentiment(4-5*) a negativní(0-3*)  
movie_reviews2 - data rozdělená na pozitivní sentiment(4-5*) a negativní(0-2*), 3* vynechány  
movie_reviews3 - data rozdělená na pozitivní sentiment(4-5*) a negativní(0-2*), 3* vynechány, odebrány veškeré číslovky z hodnocení, odebrány speciální znaky a diakritika, odebrány komentáře kratší než 40 písmen  
movie_reviews4 - data rozdělená na pozitivní sentiment(4-5*) a negativní(0-2*), 3* vynechány, odebrány veškeré číslovky z hodnocení, odebrány speciální znaky a diakritika, odebrány komentáře kratší než 40 písmen, vše převedeno na lowercase  