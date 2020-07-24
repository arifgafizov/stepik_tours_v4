def departure(request):
	departures = {"msk": "Из Москвы", 
	"spb": "Из Петербурга", 
	"nsk": "Из Новосибирска",
    "ekb": "Из Екатеринбурга", 
    "kazan": "Из Казани"
    }
    return departures