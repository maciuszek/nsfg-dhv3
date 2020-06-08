import gettext
import logging
import json

import discord
from discord.ext import commands

from cogs.helpers import context

import os

def config(bot):
    """
    This function will populate the bot object.

    This is the main config file of the bot. Replace variables you want to modify between the

    ## START CONFIG HERE

    and

    ## END CONFIG HERE

    comments. Thanks for using DuckHunt :)
    """

    # That function is here to mark items as "to be translated"
    def _(string):
        return string

    ## START CONFIG HERE

    # Change this to True once you are ready to run the bot
    bot.configured = True

    # This is the bot token. Used by the bot to connect to discord.
    bot.token = os.getenv('BOT_TOKEN')
    
    # > Language settings < #

    # This is the primary language used by the bot
    # Use C here to get the code locale. You should probably use that anyway.
    bot.default_language = "C"

    # When a duck appears (part 1)
    bot.canards_trace = ["-,_,.-'\`'°-,_,.-'\`'°", "-,..,.-'\`'°-,_,.-'\`'°", "-._..-'\`'°-,_,.-'\`'°", "-,_,.-'\`'°-,_,.-''\`"]

    # When a duck appears (part 2)
    bot.canards_portrait = ["\\_O<", "\\_o<", "\\_Õ<", "\\_õ<", "\\_Ô<", "\\_ô<", "\\_Ö<", "\\_ö<", "\\_Ø<", "\\_ø<", "\\_Ò<", "\\_ò<", "\\_Ó<", "\\_ó<", "\\_0<", "\\_©<", "\\_@<", "\\_º<", "\\_°<",
                            "\\_^<", "/_O<", "/_o<", "/_Õ<", "/_õ<", "/_Ô<", "/_ô<", "/_Ö<", "/_ö<", "/_Ø<", "/_ø<", "/_Ò<", "/_ò<", "/_Ó<", "/_ó<", "/_0<", "/_©<", "/_@<", "/_^<", "§_O<", "§_o<",
                            "§_Õ<", "§_õ<", "§_Ô<", "§_ô<", "§_Ö<", "§_ö<", "§_Ø<", "§_ø<", "§_Ò<", "§_ò<", "§_Ó<", "§_ó<", "§_0<", "§_©<", "§_@<", "§_º<", "§_°<", "§_^<", "\\_O-", "\\_o-", "\\_Õ-",
                            "\\_õ-", "\\_Ô-", "\\_ô-", "\\_Ö-", "\\_ö-", "\\_Ø-", "\\_ø-", "\\_Ò-", "\\_ò-", "\\_Ó-", "\\_ó-", "\\_0-", "\\_©-", "\\_@-", "\\_º-", "\\_°-", "\\_^-", "/_O-", "/_o-",
                            "/_Õ-", "/_õ-", "/_Ô-", "/_ô-", "/_Ö-", "/_ö-", "/_Ø-", "/_ø-", "/_Ò-", "/_ò-", "/_Ó-", "/_ó-", "/_0-", "/_©-", "/_@-", "/_^-", "§_O-", "§_o-", "§_Õ-", "§_õ-", "§_Ô-",
                            "§_ô-", "§_Ö-", "§_ö-", "§_Ø-", "§_ø-", "§_Ò-", "§_ò-", "§_Ó-", "§_ó-", "§_0-", "§_©-", "§_@-", "§_^-", "\\_O\{", "\\_o\{", "\\_Õ\{", "\\_õ\{", "\\_Ô\{", "\\_ô\{",
                            "\\_Ö\{", "\\_ö\{", "\\_Ø\{", "\\_ø\{", "\\_Ò\{", "\\_ò\{", "\\_Ó\{", "\\_ó\{", "\\_0\{", "\\_©\{", "\\_@\{", "\\_º\{", "\\_°\{", "\\_^\{", "/_O\{", "/_o\{", "/_Õ\{",
                            "/_õ\{", "/_Ô\{", "/_ô\{", "/_Ö\{", "/_ö\{", "/_Ø\{", "/_ø\{", "/_Ò\{", "/_ò\{", "/_Ó\{", "/_ó\{", "/_0\{", "/_©\{", "/_@\{", "/_^\{", "§_O\{", "§_o\{", "§_Õ\{", "§_õ\{",
                            "§_Ô\{", "§_ô\{", "§_Ö\{", "§_ö\{", "§_Ø\{", "§_ø\{", "§_Ò\{", "§_ò\{", "§_Ó\{", "§_ó\{", "§_0\{", "§_©\{", "§_@\{", "§_º\{", "§_°\{", "§_^\{"]

    # When a duck appears (part 3)
    bot.canards_cri = ["COIN", "COIN", "COIN", "COIN", "COIN", "KWAK", "KWAK", "KWAAK", "KWAAK", "KWAAAK", "KWAAAK", "COUAK", "COUAK", "COUAAK", "COUAAK", "COUAAAK", "COUAAAK", "QUAK", "QUAK",
                       "QUAAK", "QUAAK", "QUAAAK", "QUAAAK", "QUACK", "QUACK", "QUAACK", "QUAACK", "QUAAACK", "QUAAACK", "COUAC", "COUAC", "COUAAC", "COUAAC", "COUAAAC", "COUAAAC", "COUACK", "COUACK",
                       "COUAACK", "COUAACK", "COUAAACK", "COUAAACK", "QWACK", "QWACK", "QWAACK", "QWAACK", "QWAAACK", "QWAAACK", "ARK", "ARK", "AARK", "AARK", "AAARK", "AAARK", "CUI?", "PIOU?",
                       _("*cries*"), _("Hello world"), _("How are you today?"), _("Please don't kill me..."), "<https://youtu.be/r8EBoX9iUw4?t=25>", _("I love you too!"), _("Don't shoot me! I'm a fake duck!"), "<https://youtu.be/_0AAbWqxIs8>",
                       _("**Duck fact**: Some ducks can fly up to 332 miles in a single day!"), _("**Duck fact**: The feathers on a ducks back are waterproof."), _("**Duck fact**: Ducks have three eyelids!"), _("**Duck fact**: Depending on the species, a duck can live between 2 and 12 years. Not the ducks on this game tho..."),
                       _("I am invisible, don't bother killing me"), _("Who is the little ████ here that killed my friend ?"), _("You can't aim for good..."), _("The duck left."), _("The duck right."), _("STOP! It's not what you think!"),
                       _("Killing me will cost you 1562 experience points."), _("I have a secret plan to kill all hunters but I'm already short on breath I don't think I'll be able to explain it all to you before..."), _("[INSERT DUCK NOISE HERE]"), "<https://youtu.be/JZGjyxPc41o>",
                       "https://tenor.com/4nwy.gif", _("It's rabbit season."), _("Got a spare cape?"), _("Which side of a duck has more feathers? The outside."), _("I steal money. I'm a robber ducky."), _("I'm a very special duck."), _("**DuckHunt ProTip®**: use clovers to get more experience."),
                       _("**DuckHunt ProTip®**: use sights to improve accuracy at lower levels."), _("**DuckHunt ProTip®**: use grease to prevent weapon jams"), _("**DuckHunt ProTip®**: use clovers to get more experience."), _("*Slurp*"), _("Hopefully you are all AFK..."), _("**DuckHunt ProTip®**: use infrared detectors to prevent useless shots."),
                       _("I'm just doing my job..."), _("Hey there, DuckHunt quality insurance duck here. How would you rate your experience killing ducks so far ?"), _("YoU hAvE bEeN cOrRuPtEd."),
                       ]

    # When a duck leaves
    bot.canards_bye = [_("The duck went away.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck went to another world.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck didn't have time for this.  ·°'\`'°-.,¸¸.·°'\`"),
                       _("The duck left.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck dissipated in space and time.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck left out of boredom.  ·°'\`'°-.,¸¸.·°'\`"),
                       _("The duck doesn't want to be sniped.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck walked up to the lemonade stand.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck flew over a disproportionately small gap. ·°'\`'°-.,¸¸.·°'\`"),
                       _("The duck chickened out.  ·°'\`'°-.,¸¸.·°'\`")]

    # When a duck get killed
    bot.inutilite = [_("a stuffed duck."), _("a rubber ducky."), _("a vibrating duck."), _("a pile of feathers."), _("a chewed chewing gum."),
                     _("a leaflet from CACAD (Coalition Against the Comitee Against Ducks)."), _("an old shoe."), _("a spring thingy."), _("cow dung."), _("dog poop."),
                     _("an expired hunting license."), _("a cartridge."), _("a cigarette butt."), _("a used condom."), _("a broken sight."), _("a broken infrared detector."), _("a bent silencer."),
                     _("an empty box of AP ammo."), _("an empty box of explosive ammo."), _("a four-leaf clover with only 3 left."), _("a broken decoy."), _("a broken mirror."),
                     _("a rusty mechanical duck."), _("a pair of sunglasses without glasses."), _("Donald's beret."), _("a half-melted peppermint."), _("a box of Abraxo cleaner."),
                     _("a gun with banana peeled barrel."), _("an old hunting knife."), _("an old video recording: http://tinyurl.com/zbejktu"), _("an old hunting photo: http://tinyurl.com/hmn4r88"),
                     _("an old postcard: http://tinyurl.com/hbnkpzr"), _("a golden duck photo: http://tinyurl.com/hle8fjf"), _("a hunter pin: http://tinyurl.com/hqy7fhq"), _("bushes."),
                     _("https://www.youtube.com/watch?v=HP362ccZBmY"), _("a fish."), _("even more bushes."), _("Is your hand bigger than your face ?")]

    # > Database settings < #
    # User used to connect to the Mysql DB
    bot.database_user = os.getenv('MYSQL_USER')

    # Password for the user used to connect to the Mysql DB
    bot.database_password = os.getenv('MYSQL_PASSWORD')

    # Name of the table used in the Mysql DB
    bot.database_name = os.getenv('MYSQL_DB_NAME')

    # Name of the table used in the Mysql DB
    bot.database_address = os.getenv('MYSQL_ADDRESS')

    # Name of the table used in the Mysql DB
    bot.database_port = os.getenv('MYSQL_PORT')

    """
    todo-nsfg redo implementation to use scalar
    """
    # > User settings < #
    # This is a list of users IDs that are set as super admins on the bot. The bot will accept any command, from them,
    # regardless of the server and their permissions there
    bot.admins = [int(os.getenv('ADMIN_ID'))]

    """
    todo-nsfg implemented for env variables
    """
    # This is a list of users that are blacklisted from the bot. The bot will ignore dem messages
    bot.blacklisted_users = [
    ]

    # Bot Log Channel
    bot.log_channel_id = int(os.getenv('LOG_CHANNEL_ID'))

    # > Events Settings < #
    bot.event_list = [
        {"name": _("Everything is calm"), "description": _("Nothing is happening right now."), "id": 0},
        {"name": _("Ducks are migrating"), "description": _("Prepare to see more ducks in the next hour."), "id": 1, "chance_for_second_duck": 10},
        {"name": _("Foggy weather"), "description": _("It's harder to see killed ducks. You'll need a few more seconds to know if you missed or not."), "seconds_of_lag_added": 3, "id": 2},
        {"name": _("Steroids in the lake"), "description": _("A medical waste company dumped steroids in the lake. Ducks have mutated, and you'll see a lot more super ducks. But, be careful, and don't drink that water."), "id": 3, "chance_added_for_super_duck": 20},
        {"name": _("Safety class canceled"), "description": _("The safety class was canceled, beware not to shoot others hunters!"), "id": 4, "kill_chance_added": 5},
        {"name": _("Connection problems"), "description": _("Ducks cant find your computer due to connection problems, and there will be less of them until it's repaired"), "id": 5, "ducks_cancel_chance": 10},
        {"name": _("A new florist in town"), "description": _("A florist opened in town, and you can now find better 4-leaf-clovers. Go check them out!"), "id": 6, "ammount_to_add_to_max_exp": 10},
        {"name": _("Mega-ducks"), "description": _("Someone inflated a super duck, and now they are EVEN BIGGER!!"), "id": 7, "life_to_add": 3},
        {"name": _("Windy weather"), "description": _("Bullets are deflected by some strong wind"), "id": 8, "miss_chance_to_add": 8}, ]

    bot.current_event = next((item for item in bot.event_list if item['id'] == 0), None)  # event_list[0]

    # > Level Settings < #

    bot.players_levels = [
        {"niveau": 0, "expMin": -999, "nom": _("public danger"), "precision": 55, "fiabilitee": 85, "balles": 6, "chargeurs": 1},
        {"niveau": 1, "expMin": -4, "nom": _("tourist"), "precision": 55, "fiabilitee": 85, "balles": 6, "chargeurs": 2},
        {"niveau": 2, "expMin": 20, "nom": _("noob"), "precision": 56, "fiabilitee": 86, "balles": 6, "chargeurs": 2},
        {"niveau": 3, "expMin": 50, "nom": _("trainee"), "precision": 57, "fiabilitee": 87, "balles": 6, "chargeurs": 2},
        {"niveau": 4, "expMin": 90, "nom": _("duck misser"), "precision": 58, "fiabilitee": 88, "balles": 6, "chargeurs": 2},
        {"niveau": 5, "expMin": 140, "nom": _("member of the Comitee Against Ducks"), "precision": 59, "fiabilitee": 89, "balles": 6, "chargeurs": 2},
        {"niveau": 6, "expMin": 200, "nom": _("duck hater"), "precision": 60, "fiabilitee": 90, "balles": 6, "chargeurs": 2},
        {"niveau": 7, "expMin": 270, "nom": _("duck pest"), "precision": 65, "fiabilitee": 93, "balles": 4, "chargeurs": 3},
        {"niveau": 8, "expMin": 350, "nom": _("duck hassler"), "precision": 67, "fiabilitee": 93, "balles": 4, "chargeurs": 3},
        {"niveau": 9, "expMin": 440, "nom": _("duck plucker"), "precision": 69, "fiabilitee": 93, "balles": 4, "chargeurs": 3},
        {"niveau": 10, "expMin": 540, "nom": _("hunter"), "precision": 71, "fiabilitee": 94, "balles": 4, "chargeurs": 3},
        {"niveau": 11, "expMin": 650, "nom": _("duck inside out turner"), "precision": 73, "fiabilitee": 94, "balles": 4, "chargeurs": 3},
        {"niveau": 12, "expMin": 770, "nom": _("duck clobber"), "precision": 73, "fiabilitee": 94, "balles": 4, "chargeurs": 3},
        {"niveau": 13, "expMin": 900, "nom": _("duck chewer"), "precision": 74, "fiabilitee": 95, "balles": 4, "chargeurs": 3},
        {"niveau": 14, "expMin": 1040, "nom": _("duck eater"), "precision": 74, "fiabilitee": 95, "balles": 4, "chargeurs": 3},
        {"niveau": 15, "expMin": 1190, "nom": _("duck flattener"), "precision": 75, "fiabilitee": 95, "balles": 4, "chargeurs": 3},
        {"niveau": 16, "expMin": 1350, "nom": _("duck disassembler"), "precision": 80, "fiabilitee": 97, "balles": 2, "chargeurs": 4},
        {"niveau": 17, "expMin": 1520, "nom": _("duck demolisher"), "precision": 81, "fiabilitee": 97, "balles": 2, "chargeurs": 4},
        {"niveau": 18, "expMin": 1700, "nom": _("duck killer"), "precision": 81, "fiabilitee": 97, "balles": 2, "chargeurs": 4},
        {"niveau": 19, "expMin": 1890, "nom": _("duck skinner"), "precision": 82, "fiabilitee": 97, "balles": 2, "chargeurs": 4},
        {"niveau": 20, "expMin": 2090, "nom": _("duck predator"), "precision": 82, "fiabilitee": 97, "balles": 2, "chargeurs": 4},
        {"niveau": 21, "expMin": 2300, "nom": _("duck chopper"), "precision": 83, "fiabilitee": 98, "balles": 2, "chargeurs": 4},
        {"niveau": 22, "expMin": 2520, "nom": _("duck decorticator"), "precision": 83, "fiabilitee": 98, "balles": 2, "chargeurs": 4},
        {"niveau": 23, "expMin": 2750, "nom": _("duck fragger"), "precision": 84, "fiabilitee": 98, "balles": 2, "chargeurs": 4},
        {"niveau": 24, "expMin": 2990, "nom": _("duck shatterer"), "precision": 84, "fiabilitee": 98, "balles": 2, "chargeurs": 4},
        {"niveau": 25, "expMin": 3240, "nom": _("duck smasher"), "precision": 85, "fiabilitee": 98, "balles": 2, "chargeurs": 4},
        {"niveau": 26, "expMin": 3500, "nom": _("duck breaker"), "precision": 90, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 27, "expMin": 3770, "nom": _("duck wrecker"), "precision": 91, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 28, "expMin": 4050, "nom": _("duck impaler"), "precision": 91, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 29, "expMin": 4340, "nom": _("duck eviscerator"), "precision": 92, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 30, "expMin": 4640, "nom": _("ducks terror"), "precision": 92, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 31, "expMin": 4950, "nom": _("duck exploder"), "precision": 93, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 32, "expMin": 5270, "nom": _("duck destructor"), "precision": 93, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 33, "expMin": 5600, "nom": _("duck blaster"), "precision": 94, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 34, "expMin": 5940, "nom": _("duck pulverizer"), "precision": 94, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 35, "expMin": 6290, "nom": _("duck disintegrator"), "precision": 95, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 36, "expMin": 6650, "nom": _("duck atomizer"), "precision": 95, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 37, "expMin": 7020, "nom": _("duck annihilator"), "precision": 96, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 38, "expMin": 7400, "nom": _("serial duck killer"), "precision": 96, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 39, "expMin": 7790, "nom": _("duck genocider"), "precision": 97, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 40, "expMin": 8200, "nom": _("old noob"), "precision": 97, "fiabilitee": 99, "balles": 1, "chargeurs": 5},
        {"niveau": 41, "expMin": 9999, "nom": _("duck toaster"), "precision": 98, "fiabilitee": 99, "balles": 1, "chargeurs": 6},
        {"niveau": 42, "expMin": 11111, "nom": _("unemployed due to extinction of the duck species"), "precision": 99, "fiabilitee": 99, "balles": 1, "chargeurs": 7}]

    ## END CONFIG HERE

    # This is now the section to create runtime variables

    # Ducks storage

    bot.can_spawn = True
    bot.ducks_spawned = []
    bot.ducks_planning = {}

    bot.loop_latency = 1

    import datetime
    import random
    # Set the bot start time
    bot.uptime = datetime.datetime.utcnow()

    from collections import Counter
    bot.commands_used = Counter()

    class Domain:  # gettext config | http://stackoverflow.com/a/38004947/3738545
        def __init__(self, domain):
            self._domain = domain
            self._translations = {}

        def _get_translation(self, language):
            try:
                return self._translations[language]
            except KeyError:
                # The fact that `fallback=True` is not the default is a serious design flaw.
                rv = self._translations[language] = gettext.translation(self._domain, languages=[language], localedir="language", fallback=True)
                return rv

        def get(self, msg: str, language: str = bot.default_language):
            if language == "pain":
                return random.choice(["🥖", "🍞"])

            return self._get_translation(language).gettext(msg)

        def reload(self):
            self._translations = {}
            return True

    bot.translations = Domain("default")
    bot._ = bot.translations.get
