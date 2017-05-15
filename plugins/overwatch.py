"""
overwatch.py

Check's a players competitive stats.

Created By:
    - LaxWasHere <https://github.com/LaxWasHere> for the sole purpose of showing spottedleaf that he's still plat

License:
    GPL v3
"""

from cloudbot import hook
import requests
import json

@hook.command("owstats", "owrank")
def owrank(text,bot,notice):
    """ Check a persons overwatch rank .owstats battle#id"""

    url = "https://owapi.net/api/v3/u/{}/blob".format(text.replace("#","-"))

    notice("Requesting stats, please hold on.")

    try:
        req = requests.get(url,headers={'User-Agent': bot.user_agent})
        req.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        return "Could not find stats"

    compstats = json.loads(req.text)["us"]["stats"]["competitive"]["overall_stats"]

    rank = str(compstats["comprank"]) #TypeError my ass
    tier = compstats["tier"]
    wins = str(compstats["wins"])
    losses = str(compstats["losses"])
    draws = str(compstats["ties"])
    wr = str(compstats["win_rate"])

    return text + " is currently ranked " + tier.title() + " at " + rank + " " + wins+"W/"+losses+"L/"+draws+"D" + " WinRate: " + wr
