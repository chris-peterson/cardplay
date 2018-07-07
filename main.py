import keyboard
import yaml
import soco

library = yaml.load(open('library.yml'))

sonos=None
for zone in soco.discover():
    if zone.player_name == 'Media Room':
        sonos = zone

while True:
    print('waiting for event...')

    keys = list(keyboard.record(until='enter'))[:-2]
    last_scan = list(keyboard.get_typed_strings(keys))[-1][-10:]

    card_number = ''
    for c in last_scan:
        if c in {'0','1','2','3','4','5','6','7','8','9'}:
            card_number += c
        else:
            continue

    #print(card_number + ':')
    if card_number in library['cards']:
        card = library['cards'][card_number]
        if card['action'] == 'sonos':
            print('\t(sonos:play_uri) ' + card['title'])
            sonos.play_uri(uri=card['uri'], title=card['title'], meta=card['meta'])
        else:
            print('\t('+ card['action'] + ') unsupported')
    else:
        print('\tno match')