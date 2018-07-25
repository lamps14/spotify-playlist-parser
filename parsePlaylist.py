#!/usr/bin/python3

import json

json_file = 'playlist.json'
json_data = open(json_file)
playlist = open('playlist.txt', 'w+')
data = json.load(json_data)

i = 0
track_list = data['tracks']['items']

print(track_list)
for track in track_list:
    current_track = track_list[i]['track']
    print(current_track['artists'][0]['name'] + ' - ' + current_track['name'])
    playlist.write(current_track['artists'][0]['name'] + ' - ' + current_track['name'] + "\n")
    i = i + 1



