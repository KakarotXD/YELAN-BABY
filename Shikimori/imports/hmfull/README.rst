HMFULL
======

this library is a direct line by line translation of mikun_hatsune's
nodejs library of hmtai and hmfull. As such the original docs also apply
to this project

This package contains both hmtai and hmfull instead of making them
different packages

Original description
--------------------


HMfull is a Huge Anime (SFW) / Hentai (NSFW) Library that contains many
other popular and huge libraries~ Everything in one place, convenient
and simple! Call the function and get a random link with the content you
want! You no longer need to worry about finding a lot of Anime content.
Now all in one Hentai Manager Full! Will I be updating this API? Sure.
This is my main library. I will look for other libraries so you can
enjoy Anime content in large quantities!

HMfull now has over 5 thousand images! ~<3

My goal is to create the largest and most depraved library and I think I
got it :3


Installation
------------

``pip install hmfull``

Structures
----------

.. code:: py



   # Paths
   HMfull.[HMtai, Nekos, NekoLove, Miss, Freaker].[sfw, nsfw].function()
   # Exceptions
   HMfull.Nekos.ball8()
   HMfull.Miss.meme()

   # What libraries always return
   HMfull.HMtai.sfw.wallpaper() return { url: "link" }
   HMfull.Nekos.sfw.slap() return { url: "link" }

Examples
--------

.. code:: py

   # HMfull
   import hmfull as HMfull


   # Get SFW Neko Images, uwu from HMtai
   res = HMfull.HMtai.sfw.neko()
   print("SFW Neko: " + res["url"]);

   # Get other NSFW Images HMtai 
   res = HMfull.HMtai.nsfw.hentai()
   print("Hentai: " + res["url"]);

   # Get from others Libraries 
   def Nekos():
       res = HMfull.Nekos.sfw.neko()
       print("SFW Neko from nekos.life: " + res["url"]); 

   Nekos()

HMtai
-----

**SFW Function(s)**

=============== ==================================
Function        Description
=============== ==================================
wallpaper       SFW Wallpaper with Anime
mobileWallpaper SFW Wallpaper with Anime on Mobile
neko            SFW Neko Girls (Cat Girls)
jahy            So hot Jahy :3
lick            SFW licks gifs :P
slap            SFW slap gifs xD
=============== ==================================

**NSFW Function(s)**

+---------------------+-----------------------------------------------+
| Function            | Description                                   |
+=====================+===============================================+
| ass                 | I know you like anime ass~ uwu                |
+---------------------+-----------------------------------------------+
| bdsm                | If you don't know what it is, search it up    |
+---------------------+-----------------------------------------------+
| cum                 | Basically sticky white stuff that is usually  |
|                     | milked from sharpies.                         |
+---------------------+-----------------------------------------------+
| creampie            | So hot, sticky, and inside uwu                |
+---------------------+-----------------------------------------------+
| manga               | Sends a random doujin page imageURL!          |
+---------------------+-----------------------------------------------+
| femdom              | Female Domination?                            |
+---------------------+-----------------------------------------------+
| hentai              | Sends a random vanilla hentai imageURL~       |
+---------------------+-----------------------------------------------+
| incest              | I know, you like it. Brothet and sister <3    |
|                     | And..mo...omg                                 |
+---------------------+-----------------------------------------------+
| masturbation        | You like lewd solo?~                          |
+---------------------+-----------------------------------------------+
| public              | Some people like do it on a public..uh~       |
+---------------------+-----------------------------------------------+
| ero                 | eros, ero Uniforms, etc, you know what eros   |
|                     | are :3                                        |
+---------------------+-----------------------------------------------+
| orgy                | Group Lewd Acts                               |
+---------------------+-----------------------------------------------+
| elves               | So, it's not Elvis Presley, but i know, you   |
|                     | like it :)                                    |
+---------------------+-----------------------------------------------+
| yuri                | What about cute Les?~                         |
+---------------------+-----------------------------------------------+
| pantsu              | I mean... just why? You like underwear?       |
+---------------------+-----------------------------------------------+
| glasses             | Girls that wear glasses, uwu~                 |
+---------------------+-----------------------------------------------+
| cuckold             | Wow, I won't even question your fetishes.     |
+---------------------+-----------------------------------------------+
| blowjob             | Basically an image of a girl sucking on a     |
|                     | sharp blade!                                  |
+---------------------+-----------------------------------------------+
| boobjob             | So soft, round ... gentle ... damn we love it |
+---------------------+-----------------------------------------------+
| foot                | So you like smelly feet huh?                  |
+---------------------+-----------------------------------------------+
| thighs              | Oh, i so like it, it's best of the best, like |
|                     | a religion <3                                 |
+---------------------+-----------------------------------------------+
| vagina              | The genitals of a female, or a cat, you give  |
|                     | the meaning.                                  |
+---------------------+-----------------------------------------------+
| ahegao              | So happy woman faces :))                      |
+---------------------+-----------------------------------------------+
| uniform             | School and many other Uniforms~               |
+---------------------+-----------------------------------------------+
| gangbang            | 5 on 1? Uh..                                  |
+---------------------+-----------------------------------------------+
| tentacles           | I'm sorry but, why do you like it? Uh..       |
+---------------------+-----------------------------------------------+
| gif                 | Basically an animated image, so yes :3        |
+---------------------+-----------------------------------------------+
| nsfwNeko            | NSFW Neko Girls (Cat Girls)                   |
+---------------------+-----------------------------------------------+
| nsfwMobileWallpaper | NSFW Anime Mobile Wallpaper                   |
+---------------------+-----------------------------------------------+
| zettaiRyouiki       | That one part of the flesh being squeeze in   |
|                     | thigh-highs~<3                                |
+---------------------+-----------------------------------------------+

Nekos
-----

-  ball8 Function \| Magic 8ball give you answer [STRIKEOUT:-]

**SFW Function(s)**

======== ===================================
Function Description
======== ===================================
pat      Let's pet everyone gifs :3
hug      Let's hug everyone gifs <3
kiss     let's kiss and make up ;3
cry      So sad T.T
slap     Wanna somebody slap? SLAP SLAP! >:<
smug     Will show you a malicious face! >:3
neko     What about sweet neko?~
waifu    Generate Waifu with AI
cuddle   Cuuuddle cuddle cuddle~
feed     You wanna eat? I gonna feed you :3
foxgirl  Is this a parody of Neko?
======== ===================================

**NSFW Function(s)**

======== ==============================
Function Description
======== ==============================
nekogif  This is what are you wanted?..
======== ==============================

NekoBot
-------

**SFW Function(s)**

========== =======================================================
Function   Description
========== =======================================================
kanna      Sweet Kanna images ｶﾜ(・∀・)ｲｲ!!
neko       All your love in one picture !(´ \* ω \* \`)!
holo       What you think about kitsune Holo? >:3
kemonomimi IDK what it that, but, it's something sweet ╯-╰
coffee     What are you up to little mischievous? (0ˍ0)
gah        Are you sure you want to punch? Maybe not worth it? >:<
========== =======================================================

**NSFW Function(s)**

========= ========================================================
Function  Description
========= ========================================================
hentai    Mmmmm, anata wa hentai desu!!
hass      Has...Has what? Idk, maybe you know, huh :P
boobs     Very big, and so..soft, yeah, soft..very..very..soft :>
paizuri   You like something like yet? It some..nice
yuri      Two beautiful girls, it's awesome <3
thigh     It's my fetish, it's my weakness, dude, it's a perfect
lewdneko  Lewd Neko? GIVE ME ALL THAT YOU HAVE!!! Copypast, yeah..
midriff   Midriff, it's..Maybe, but i not fun of this..Maybe you?
kitsune   Kitsune. Just a..Fox-Girl, you love neko? Maybe fox too?
tentacle  Ugh....I don't like this, it's dirty and disgusting
anal      It's not bad, but, if we look on detail...No, please, no
hanal     It's not bad too, but..wait, is it same?! Or...not?
hneko     Are you sure about that? YES, WE'RE SURE!
wallpaper Do you like some...good wallpaper for Desktop?~
========= ========================================================

Neko-Love
---------

**SFW Function(s)**

======== =======================================================
Function Description
======== =======================================================
pat      For those with soft hands UωU
hug      All your love in one picture !(´ \* ω \* \`)!
kiss     Leave your memories in one action >:3
cry      Sometimes you just need to cry a little ╯-╰
slap     Are you sure you want to slap? Maybe not worth it? o_o
smug     What are you up to little mischievous? (0ˍ0)
punch    Are you sure you want to punch? Maybe not worth it? >:<
neko     Just Neko-chans to order (●'^'●)
kitsune  Kitsune... IT IS GREAT (¬.¬)
waifu    Yours and only yours (probably) waifu
======== =======================================================

**NSFW Function(s)**

======== =============================================
Function Description
======== =============================================
nekolewd Neko? Lewd Neko? GIVE ME ALL THAT YOU HAVE!!!
======== =============================================
