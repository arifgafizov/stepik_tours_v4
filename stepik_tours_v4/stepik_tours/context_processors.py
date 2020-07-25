def departure(request):
    departures_dic = {
    'departures': {"msk": "Из Москвы",
	"spb": "Из Петербурга", 
	"nsk": "Из Новосибирска",
    "ekb": "Из Екатеринбурга", 
    "kazan": "Из Казани"
        }
    }
    return departures_dic