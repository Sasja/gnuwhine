#!/usr/bin/env python

import urllib2, json
import datetime

# list of (tulip, ingredient, multiplier)
# see coinmarketcap.com for all available tulips
recipe = [
("bitcoin", "clubmate",1),
("ethereum", "vodka",2.0),
("raiblocks", "cognac",30),
("request-network", "lemon",500),
]

# choose a metric out of:
# price_usd, market_cap_usd, 24h_volume_usd, percent_change_{7d,24h,1h}
metric = "price_usd"


def getValue(tulip, metric):
    url = "https://api.coinmarketcap.com/v1/ticker/" + tulip
    return float(json.loads(urllib2.urlopen(url).read())[0][metric])

print "# gnuwhine recipe generated by purpletulip.py based on the tulip market as of"
print "# " + str(datetime.datetime.now())
print "#"
print "# using the " + metric + " metric"
print "#"
print "# using following translation table:"
print "#"
for tulip, ingredient, multiplier in recipe:
    print "#   {:20} {:20} {:10}".format(tulip, ingredient, multiplier)
print "#"

mix = []
total = 0
for tulip, ingredient, multiplier in recipe:
    print "# fetching " + metric + " from " + tulip + " ..."
    mix.append((ingredient, multiplier * getValue(tulip, metric)))
    total += mix[-1][1]
print "#"

print "# generating final recipe..."
print "#"
print
normalised = [(x[0], 100*x[1]/total) for x in mix]
for ingredient, percent in normalised:
    print "{}: {:.2f}%".format(ingredient,percent)
print 
print "# WARNING: never take investment advice from a cocktail robot!"
