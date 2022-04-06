steps = [
    { # 0
      'type': 'head'
    },
    { # 1
      'type': 'timed',
      'timing': 2,
      'text': 'Hallo, ik heet Robin. Hoe heet jij?'
    },
    { # 2
      'type': 'silence',
      'silence_time': 3,
      'text': 'Leuk je te ontmoeten. Ben je klaar om te starten met onze sessie?'
    },
    { # 3
      'type': 'boolean',
      'positive': 9,
      'negative': 4
    },
    { # 4
      'type': 'timed',
      'timing': 1,
      'text': 'Neem een momentje, we zullen het samen doen.'
    },
    { # 5
      'type': 'timed',
      'timing': 4,
      'text': 'Ok, zullen we beginnen?'
    },
    { # 6
      'type': 'boolean',
      'positive': 9,
      'negative': 7
    },
    { # 7
      'type': 'timed',
      'typing_time': 4000,
      'timing': 1,
      'text': 'Als je wilt, kun je de onderzoeker erbij halen. Raak mijn hoofd opnieuw aan wanneer je klaar bent om te beginnen.'
    },
    { # 8
      'type': 'head',
    },
    { # 9
      'type': 'timed',
      'timing': 1,
      'text': 'Mooi!'
    },
    { # 10
      'type': 'timed',
      'timing': 1,
      'text': 'Ik kan me voorstellen dat dit nieuw en misschien een beetje vreemd voor jou is. Ik denk dat het goed is om samen een korte ademhalingsoefening te doen om te ontspannen.'
    },
    { # 11
      'type': 'timed',
      'timing': 1,
      'text': 'Ben je er klaar voor om de oefening te starten?'
    },
    { # 12
      'type': 'boolean',
      'positive': 14,
      'negative': 13
    },
    { # 13
      'type': 'timed',
      'timing': 1,
      'text': 'Het is een korte oefening, we doen het samen en het is voorbij voordat je het weet.'
    },
    { # 14
      'type': 'timed',
      'timing': 1,
      'text': 'Ok. Zorg ervoor dat je comfortabel zit en probeer mijn instructies te volgen.'
    },
    { # 15
      'type': 'breathe'
    },
    { # 16
      'type': 'timed',
      'timing': 1,
      'text': 'Dat ging volgens mij wel goed. Hoe was het voor jou?'
    },
    { # 17
      'type': 'silence',
      'silence_time': 3,
      'text': 'Goed dat je hebt meegedaan. Laten we verder gaan met het volgende deel van onze sessie.'
    },
    { # 18
      'type': 'timed',
      'timing': 1,
      'text': 'Het is een drukke tijd. Het viel me op dat veel studenten druk bezig zijn met school. Hoe was jouw week.'
    },
    { # 19
      'type': 'silence',
      'silence_time': 5,
      'text': 'Heb je tijd gehad om je voor te bereiden, het selecteren van een stress volle gebeurtenis om over te praten?'
    },
    { # 20
      'type': 'boolean',
      'positive': 23,
      'negative': 21
    },
    { # 21
      'type': 'timed',
      'timing': 1,
      'text': 'Ah, dat kan gebeuren. Neem anders nu een moment om iets te bedenken, en laat me weten wanneer je klaar bent om door te gaan.'
    },
    { # 22
      'type': 'silence',
      'silence_time': 3,
      'text': 'Fijn om te horen. Ik vind het fijn dat je tijd hebt gemaakt om met mij te praten.',
      'next': 24
    },
    { # 23
      'type': 'timed',
      'timing': 1,
      'text': 'Fijn om te horen. Ik vind het fijn dat je tijd hebt gemaakt om met mij te praten.'
    },
    { # 24
      'type': 'timed',
      'timing': 1,
      'text': 'Studies hebben aangetoond dat het schrijven of praten over een stressvolle gebeurtenis kan helpen in het verlagen van de stress die je ervaart.'
    },
    { # 25
      'type': 'timed',
      'timing': 2,
      'text': 'Ik ga je nu wat vragen stellen over de gebeurtenis:'
    },
    { # 26
      'type': 'timed',
      'timing': 2.5,      
      'text': 'Wanneer is dit gebeurd?'
    },
    { # 27
      'type': 'silence',
      'silence_time': 5,
      'text': 'Waren er anderen bij betrokken?'
    },
    { # 28
      'type': 'silence',
      'silence_time': 5,
      'text': 'Kun je me vertellen wat er gebeurd is?'
    },    
    { # 29
      'type': 'silence',
      'silence_time': 5,
      'text': 'Dat klinkt inderdaad stressvol. Hoe voelde dat voor jou?'
    },
    { # 30
      'type': 'silence',
      'silence_time': 5,
      'text': 'Hoe ben je ermee omgegaan?'
    },    
    { # 31
      'type': 'silence',
      'silence_time': 5,
      'text': 'Zijn er nog andere dingen die je over deze gebeurtenis aan mij kwijt wilt?'
    },
    { # 32
      'type': 'silence',
      'silence_time': 5,      
      'text': 'Het is goed van je dat je dit met mij wilt delen. Viel het mee of tegen om dit met mij te delen?'
    },
    { # 33
      'type': 'silence',
      'silence_time': 5,      
      'text': 'Bedankt dat je jouw ervaring met mij hebt gedeeld.'
    },    
    { # 34
      'type': 'timed',
      'timing': 1.5,      
      'text': 'Ik vond dat het goed ging en dat je het heel goed hebt gedaan. De tijd vliegt, we zijn al bijna bij het einde van onze sessie.'
    },
    { # 35
      'type': 'timed',
      'timing': 1.5,
      'text': 'Om onze sessie af te sluiten is het goed om een oefening te doen. Zullen we deze oefening samen doen?'
    },
    { # 36
      'type': 'boolean',
      'positive': 38,
      'negative': 37
    },
    { # 37
      'type': 'timed',
      'timing': 1,
      'text': 'Kom op! We zijn bijna klaar, alleen nog deze laatste oefening om te zorgen voor een positieve afsluiting.'
    },
    { # 38
      'type': 'timed',
      'timing': 1,
      'text': 'Ok, zorg dat je comfortabel zit. Probeer mijn instructies te volgen, ben je klaar om te starten?'
    },
    { # 39
      'type': 'boolean',
      'positive': 44,
      'negative': 40
    },
    { # 40
      'type': 'timed',
      'timing': 1,
      'text': 'Probeer rechtop te zitten en plaats beide voeten op de grond. Hoe is het nu? Heb je een comfortabele houding gevonden?'
    },
    { # 41
      'type': 'boolean',
      'positive': 44,
      'negative': 42
    },
    { # 42
      'type': 'timed',
      'timing': 1,
      'text': 'Neem de tijd, en laat me weten als je klaar bent om te beginnen.'
    },
    { # 43
      'type': 'silence',
      'silence_time': 3,
      'text': 'Fijn! We gaan een lichaams scan doen. Dit is een oefening waar we ons concentreren op verschillende delen van het lichaam en hoe het voelt.',
      'next': 45
    },
    { # 44
      'type': 'timed',
      'timing': 1,
      'text': 'Fijn! We gaan een lichaams scan doen. Dit is een oefening waar we ons concentreren op verschillende delen van het lichaam en hoe het voelt.'
    },
    { # 45
      'type': 'timed',
      'timing': 1.5,
      'text': 'Wanneer we het lichaam scannen is het mogelijk dat je stress of spanning opmerkt in het lichaam.'
    },
    { # 46
      'type': 'timed',
      'timing': 2.5,
      'text': 'Dat is ok, als je hiervan bewust wordt, probeer het te observeren en rustig naar toe te ademen.'
    },
    { # 47
      'type': 'timed',
      'timing': 8,
      'text': 'Ok, probeer rechtop te zitten en plaats je armen op je bovenbenen.'
    },
    { # 48
      'type': 'timed',
      'timing': 10,
      'text': 'Laat het gewicht van het lichaam in de stoel zakken en breng je aandacht naar je voeten.'
    },
    { # 49
      'type': 'timed',
      'timing': 10,
      'text': 'Voel hoe je voeten contact maken met de grond. '
    },
    { # 50
      'type': 'timed',
      'timing': 8,
      'text': 'Van de voeten gaan we omhoog naar de benen, richt je aandacht op je linkerbeen en dan op je rechterbeen.'
    },
    { # 51
      'type': 'timed',
      'timing': 12,
      'text': 'Breng je aandacht rustig naar de heupen en voel hoe je zit op de stoel.'
    },
    { # 52
      'type': 'timed',
      'timing': 8,
      'text': 'Vanaf hier gaan we langzaam omhoog naar de onderrug, en buik.'
    },
    { # 53
      'type': 'timed',
      'timing': 8,
      'text': 'Adem rustig in en uit, voel hoe de buik uitzet bij een uitademing.'
    },
    { # 54
      'type': 'timed',
      'timing': 12,
      'text': 'Nu verplaatsen we rustig de aandacht naar de borst en bovenrug.'
    },
    { # 55
      'type': 'timed',
      'timing': 8,
      'text': 'Terwijl we verder gaan naar de schouders, voel je hoe de armen op de benen rusten.'
    },
    { # 56
      'type': 'timed',
      'timing': 10,
      'text': 'Observeer wat je voelt.'
    },
    { # 57
      'type': 'timed',
      'timing': 12,
      'text': 'Breng je aandacht nu naar je nek en vanaf hier gaan we naar het hoofd.'
    },
    { # 58
      'type': 'timed',
      'timing': 8,
      'text': 'Richt je aandacht op je gezicht, dan het achterhoofd en als laatste op de kruin.'
    },
    { # 59
      'type': 'timed',
      'timing': 15,
      'text': 'Het is mogelijk dat je in je lichaam ergens spanning of stress bespeurt. Dat is ok.'
    },
    { # 60
      'type': 'timed',
      'timing': 4,
      'text': 'Probeer even te blijven zitten terwijl je rustig in en uitademt.'
    },
    { # 61
      'type': 'timed',
      'timing': 12,
      'text': 'Observeer hoe je lichaam voelt in dit moment.'
    },
    { # 62
      'type': 'timed',
      'timing': 15,
      'text': 'Dat was de lichaams scan! Hoe ging het?'
    },
    { # 63
      'type': 'silence',
      'silence_time': 5,
      'text': 'Ik vond dat het goed ging. Bedankt dat je de tijd hebt genomen om jouw verhaal te vertellen en deze sessie te beeindigen met deze oefening. Je hebt het goed gedaan!'
    },
    { # 64
      'type': 'timed',
      'timing': 2,
      'text': 'Dat was het, we hebben het einde bereikt van onze sessie. Ik vond het leuk om met je te praten.'
    },
    { # 65
      'type': 'timed',
      'timing': 1.5,
      'text': 'Wanneer je er klaar voor bent, kun je de onderzoeker halen voor het laatste deel van het onderzoek.'
    },
    { # 66
      'type': 'timed',
      'timing': 1.5,
      'text': 'Doei.'
    },
  ]