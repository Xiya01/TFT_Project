import pyautogui, time

#top x: 600 y:900
#bot x: 1350 y: 940


def find_champion_shop():
    import numpy as np 

    champions = ['aatrox', 'gragas', 'kalista', 'khazix', 'kled', 'leona', 'olaf', 'poppy', 'senna', 'udyr', 'vayne', 'vladimir', 'ziggs', 'brand', 'hecarim', 'irelia', 'kennen', 'nautilus', 'pyke', 'sejuani', 'sett', 'soraka', 'syndra', 'thresh', 'tristana', 'varus', 'ashe', 'leesin', 'lulu', 'lux', 'missfortune', 'nidalee', 'nocturne', 'nunu', 'rakan', 'riven', 'yasuo', 'zyra', 'aphelios', 'diana', 'draven', 'fiddlesticks', 'galio', 'ivern', 'jax', 'karma', 'lucian', 'rell', 'velkoz', 'akshan', 'garen', 'gwen', 'heimerdinger', 'kayle', 'teemo', 'viego', 'volibear']

    for champion in champions:
        location = pyautogui.locateOnScreen(f'screenshots/store/{champion}.png', region=(600,900, 750, 40))
        if location:
            print(f"Found {champion}")