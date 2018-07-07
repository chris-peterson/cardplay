import yaml
import soco

library = yaml.load(open('library.yml'))
print(yaml.dump(library))

sonos=None
for zone in soco.discover():
    if zone.player_name == 'Media Room':
        sonos = zone
if not sonos:
    raise Exception('Did not find expected Sonos')

# TODO: integrate with RFID->keyboard
card = library['cards']['0003971976']

sonos.play_uri(uri=card['uri'], title=card['title'], meta=card['meta'])