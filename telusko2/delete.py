{% load static %}
{% static "images" as baseUrls %}
<!DOCTYPE html>

<html>

<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/css/bootstrap.min.css" integrity="sha384-SI27wrMjH3ZZ89r4o+fGIJtnzkAnFs3E4qz9DIYioCQ5l9Rd/7UAa8DHcaL8jkWt" crossorigin="anonymous">
  <title>67Channel</title>
  <style>
  .imagec{
  padding-left:30px;
  }
  </style>
  <style>
      blink {
        animation: blinker 0.6s linear infinite;
        color: red;
       }
      @keyframes blinker {  
        50% { opacity: 0; }
       }
       .blink-one {
         animation: blinker-one 1s linear infinite;
       }
       @keyframes blinker-one {  
         0% { opacity: 0; }
       }
       .blink-two {
         animation: blinker-two 1.4s linear infinite;
       }
       @keyframes blinker-two {  
         100% { opacity: 0; }
       }
    </style>
</head>

<body>
  <div class="images"><img src="{% static 'images/67Channelimg.png' %}" alt=""></div>
  

<a href="{% static 'BestMovies.html' %}"><button type="button" class="btn btn-outline-primary"><b class="list-group-item list-group-item-action list-group-item-primary">Best Movies</b></button></a><a href="{% static 'Feelgoodsongs.html' %}"><button type="button" class="btn btn-outline-primary">Feel good songs</button></a><a href="{% static 'hitmovies.html' %}"><button type="button" class="btn btn-outline-primary">Hit movies</button></a><a href="{% static 'moviereviews.html' %}"><button type="button" class="btn btn-outline-primary">Movie reviews</button></a><a href="{% static 'songsreviews.html' %}"><button type="button" class="btn btn-outline-primary">Song Reviews</button></a><a href="{% static 'upcomingmovies.html' %}"><button type="button" class="btn btn-outline-primary">Upcoming Movies</button></a><a href="{% static 'movienews.html' %}"><button type="button" class="btn btn-outline-primary">Movie news</button></a><a href="{% static 'celebritiesinfo.html' %}"><button type="button" class="btn btn-outline-primary">celebrities biodata</button></a>
    <hr>
<h2><blink>Best Movies</blink></h2>
<hr>
<ul id="nav">
  <div class="col-8">
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Vaana.html' %}">>> <b style="color:Red">Best Movie</b> : Vaana</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/AnukokundaOkaRoju.html' %}">>> <b style="color:Red">Best Movie</b> : Anukokunda Oka Roju</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/pisachi.html' %}">>> <b style="color:Red">Best Movie</b> : Pisachi</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/killer.html' %}">>> <b style="color:Red">Best Movie</b> : Killer</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/jessie.html' %}">>> <b style="color:Red">Best Movie</b> : Jessie</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/kancharapalem.html' %}">>> <b style="color:Red">Best Movie</b> : C/o Kancharapalem</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/PowerStar.html' %}">>> <b style="color:Red">Best Movie</b> : Power Star</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/AaNaluguru.html' %}">>> <b style="color:Red">Best Movie</b> : Aa Naluguru</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/gajini.html' %}">>> <b style="color:Red">Best Movie</b> : gajini</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/JaiLavakusa.html' %}">>> <b style="color:Red">Best Movie</b> : Jai Lavakusa</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Yamadonga.html' %}">>> <b style="color:Red">Best Movie</b> : yamadonga</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Sye.html' %}">>> <b style="color:Red">Best Movie</b> : sye</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Vikramarkudu.html' %}">>> <b style="color:Red">Best Movie</b> : vikramarkudu</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Bahubali.html' %}">>> <b style="color:Red">Best Movie</b> : bahubali</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Bahubali2.html' %}">>> <b style="color:Red">Best Movie</b> : bahubali2</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Eega.html' %}">>> <b style="color:Red">Best Movie</b> : Eega</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Maryadarammanna.html' %}">>> <b style="color:Red">Best Movie</b> : maryadaramanna</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/StudentNo1.html' %}">>> <b style="color:Red">Best Movie</b> : student no 1</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Simhadri.html' %}">>> <b style="color:Red">Best Movie</b> : simhadri</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Magadheera.html' %}">>> <b style="color:Red">Best Movie</b> : magadheera</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Bhadra.html' %}">>> <b style="color:Red">Best Movie</b> : bhadra</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Siva.html' %}">>> <b style="color:Red">Best Movie</b> : siva</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/ArjunReddy.html' %}">>> <b style="color:Red">Best Movie</b> : Arjun Reddy</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/MuniSeries.html' %}">>> <b style="color:Red">Best Movie</b> : muni series</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/GameOver.html' %}">>> <b style="color:Red">Best Movie</b> : Game Over</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/13B.html' %}">>> <b style="color:Red">Best Movie</b> : 13b</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Jayam.html' %}">>> <b style="color:Red">Best Movie</b> : jayam</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Dil.html' %}">>> <b style="color:Red">Best Movie</b> : Dil</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Ishq.html' %}">>> <b style="color:Red">Best Movie</b> : ishq</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/SwamyRaRa.html' %}">>> <b style="color:Red">Best Movie</b> : swamy ra ra</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Orange.html' %}">>> <b style="color:Red">Best Movie</b> : Orange</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Jalsa.html' %}">>> <b style="color:Red">Best Movie</b> : jalsa</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/NuveNuve.html' %}">>> <b style="color:Red">Best Movie</b> : nuve nuve</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Chirunavvutho.html' %}">>> <b style="color:Red">Best Movie</b> : chirunavvutho</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/NuvuNakuNachav.html' %}">>> <b style="color:Red">Best Movie</b> : nuvu naku nachav</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Gamyam.html' %}">>> <b style="color:Red">Best Movie</b> : gamyam</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Vedam.html' %}">>> <b style="color:Red">Best Movie</b> : vedam</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Kanche.html' %}">>> <b style="color:Red">Best Movie</b> : kanche</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/KrishnamVandeJagadguru.html' %}">>> <b style="color:Red">Best Movie</b> : krishnam vande jagadguru</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Manmadhudu.html' %}">>> <b style="color:Red">Best Movie</b> : manmadhudu</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Khaidi.html' %}">>> <b style="color:Red">Best Movie</b> : srikanth movies</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Premadesham.html' %}">>> <b style="color:Red">Best Movie</b> : premadesham</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/PillaJamindhar.html' %}">>> <b style="color:Red">Best Movie</b> : pilla jamindhar</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Jersey.html' %}">>> <b style="color:Red">Best Movie</b> : jersey</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/MalliRava.html' %}">>> <b style="color:Red">Best Movie</b> : mallirava</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/KamalHassan.html' %}">>> <b style="color:Red">Best Movie</b> : kamal hassan</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/RajiniKanth.html' %}">>> <b style="color:Red">Best Movie</b> : rajini kanth</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Manu.html' %}">>> <b style="color:Red">Best Movie</b> : manu</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Devi.html' %}">>> <b style="color:Red">Best Movie</b> : devi</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Chitralahari.html' %}">>> <b style="color:Red">Best Movie</b> : Chitralahari</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/AlaModalaindi.html' %}">>> <b style="color:Red">Best Movie</b> : AlaModalaindi</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/PelliChoopulu.html' %}">>> <b style="color:Red">Best Movie</b> : PelliChoopulu</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/ShatamanamBhavathi.html' %}">>> <b style="color:Red">Best Movie</b> : ShatamanamBhavathi</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/TheEnd.html' %}">>> <b style="color:Red">Best Movie</b> : TheEnd</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/100%Love.html' %}">>> <b style="color:Red">Best Movie</b> : 100%Love</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Missamma.html' %}">>> <b style="color:Red">Best Movie</b> : Missamma</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Tagore.html' %}">>> <b style="color:Red">Best Movie</b> : Tagore</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/96.html' %}">>> <b style="color:Red">Best Movie</b> : 96</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Gaganam.html' %}">>> <b style="color:Red">Best Movie</b> : Gaganam</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Muni.html' %}">>> <b style="color:Red">Best Movie</b> : Muni</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Kanchana.html' %}">>> <b style="color:Red">Best Movie</b> : Kanchana</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Mirchi.html' %}">>> <b style="color:Red">Best Movie</b> : Mirchi</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/Fidha.html' %}">>> <b style="color:Red">Best Movie</b> : Fidha</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/MalliRaava.html' %}">>> <b style="color:Red">Best Movie</b> : MalliRaava</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/180.html' %}">>> <b style="color:Red">Best Movie</b> : 180</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="{% static 'BestMovies/ArjunSuravaram.html' %}">>> <b style="color:Red">Best Movie</b> : ArjunSuravaram</a></li>
  <li class="list-group-item list-group-item-action list-group-item-secondary"><a href="/tips/">>> <b style="color:Red">Best Movie</b> : 50</a></li>
  </div>
</ul>
 
 </body>
</html>
