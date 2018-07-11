import keyboard
import psutil
import soco
import webbrowser
import yaml

library = yaml.load(open('library.yml'))

try:
    sonos=None
    for zone in soco.discover():
        if zone.player_name == 'Media Room':
            sonos = zone
except:
    print('no sonos found')
    sonos=None

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
            if not sonos:
                print('sonos not available, please restart application')
                continue
            if meta == 'playlist':
                sonos.clear_queue()
                sonos.add_uri_to_queue(uri)
                sonos.play_from_queue(0)
            elif meta == 'tunein':
                sonos.play_uri(uri=uri, title=title)
            else: # e.g. amazon music station
                sonos.play_uri(uri=uri, title=title, meta=meta)
        elif action == 'browser':
            webbrowser.get(meta).open_new_tab(uri)
        elif action == 'diag':
            print('killing all firefox processes...')
            for proc in psutil.process_iter():
                if proc.status() != 'zombie' and proc.name() == 'firefox':
                    proc.kill()
            if sonos:
                print('setting sonos input to line in')
                sonos.switch_to_line_in()
        else:
            print('\t|-> unsupported')
    else:
        print('\tno match')