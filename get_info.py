import pyautogui, time

#top x: 600 y:900
#bot x: 1350 y: 940
store_cords = ((600,908),(750,908),(899,908),(1048,908),(1198,908))

def find_champion_shop():
    counter = 0
    champions = ['aatrox', 'gragas', 'kalista', 'khazix', 'kled', 'leona', 'olaf', 'poppy', 'senna', 'udyr', 'vayne', 'vladimir', 'ziggs', 'brand', 'hecarim', 'irelia', 'kennen', 'nautilus', 'pyke', 'sejuani', 'sett', 'soraka', 'syndra', 'thresh', 'tristana', 'varus', 'ashe', 'leesin', 'lulu', 'lux', 'missfortune', 'nidalee', 'nocturne', 'nunu', 'rakan', 'riven', 'yasuo', 'zyra', 'aphelios', 'diana', 'draven', 'fiddlesticks', 'galio', 'ivern', 'jax', 'karma', 'lucian', 'rell', 'velkoz', 'akshan', 'garen', 'gwen', 'heimerdinger', 'kayle', 'teemo', 'viego', 'volibear']
    for champion in champions:
        locations = list(pyautogui.locateAllOnScreen(f'screenshots/store/{champion}.png', region=(600, 908, 750, 40), confidence=0.9, grayscale=True))
        if locations:
            for location in locations:
                counter += 1
                print(f"Found {champion} at {location.left}")
        if counter == 5:
            break
    