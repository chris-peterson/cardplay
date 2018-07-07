import keyboard
import yaml
import soco
import webbrowser

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
        action = card['action'].lower()
        title = card['title']
        uri = card['uri']
        meta = card['meta']
        print('\t(' + action + ') - ' + title)
        if action == 'sonos':
            sonos.play_uri(uri=uri, title=title, meta=meta)
        elif action == 'browser':
            webbrowser.get(meta).open_new_tab(uri)
        else:
            print('\t|-> unsupported')
    else:
        print('\tno match')