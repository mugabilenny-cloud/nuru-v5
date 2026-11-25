"""Career videos shown on Nuru. Edit this list to swap videos: only the YouTube `id` is required.

All four were taken from NTV Uganda's own news pages (they embed these videos from NTV Uganda's YouTube channel).
The 11-character id is the part after `watch?v=` in a YouTube link.
"""

VIDEOS = [
    {"id": "U_Wx0DXdDeY", "channel": "NTV Uganda", "tag": "Labour market",
     "title": "Government plans regional skilling hubs to tackle 12% unemployment",
     "desc": "Ministries and planners explain how skilling hubs and workforce planning aim to close the gap between "
             "graduates' qualifications and what employers need. Youth unemployment is put at 16.2% (UBOS 2025)."},
    {"id": "Ef0JllpaTS4", "channel": "NTV Uganda", "tag": "Skills",
     "title": "Bridging the skills-to-jobs divide",
     "desc": "Nation Media Group, the Uganda Manufacturers Association and KCDI launch the Mbale Skills Expo, a two-week "
             "drive linking young people to practical training and industry opportunities."},
    {"id": "92GPDKAwDdk", "channel": "NTV Uganda", "tag": "Youth employment",
     "title": "ILO warns of deepening global youth employment crisis",
     "desc": "NTV Uganda's business desk reports the International Labour Organization's warning on the state of "
             "youth employment worldwide."},
    {"id": "_SOdewFUUxg", "channel": "NTV Uganda", "tag": "Green jobs",
     "title": "GREEN FUND: Uganda's youth demand more support",
     "desc": "Youth leaders at a national training convention in Kampala call for skills in climate finance, green jobs "
             "and advocacy to unlock Uganda's emerging green economy."},
]


def watch_url(vid):
    return f"https://www.youtube.com/watch?v={vid}"
