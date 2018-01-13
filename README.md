# Gnüwhine recipe generator

## Generate your own Gnüwhine recipe based on the latest updates from the [tulip markets](https://coinmarketcap.com)
Run `purpletulip.py` to generate a recipe on stdout or `purpletulip.py > recipe.yaml`

Personalise `purpletulip.py` to your taste and portfolio. Purpletulip can track price, market cap, or - if you dare - `percent_change_1h` to create the most volatile cocktails that will keep you coming back for more!

See upstream for more info on ingredients and the robot itself

Set up a cronjob that runs `tulipupdate.sh` like e.g.
```
0 20 * * * /home/sasja/git/gnuwhine/tulipupdate.sh /home/sasja/git/gnuwhine
```

Happy Gnüwhining!
Never take investment advice from a cocktail robot!!!
