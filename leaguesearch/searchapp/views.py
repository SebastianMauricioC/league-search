from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Summoner, Champion

API_KEY = ''


def champions(request):
    try:
        url = 'https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion.json'

        r = requests.get(url)
        champion_data = r.json()

        champions = []

        data = champion_data['data']

        for c in data:
            champ = data[c]
            title = champ['title']
            info = champ['info']
            attack = info.get('attack')
            defense = info.get('defense')
            magic = info.get('magic')
            difficulty = info.get('difficulty')
            champion = Champion(champion_name=c, champion_title=title, champion_attack=attack, champion_defense=defense,
                                champion_magic=magic, champion_difficulty=difficulty)
            champions.append(champion)

        context = {
            'champions': champions
        }

        return render(request, 'champions.html', context)
    except requests.RequestException as e:
        print(e)
        return HttpResponse('There has been an error retrieving champion data, please try again later')




def index(request):
    return render(request, 'index.html')
