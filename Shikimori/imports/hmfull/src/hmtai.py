import json
import random
import os
directory_name = os.path.dirname(__file__)

sfwNeko = json.load(open(os.path.join(directory_name,('images/sfwNeko.json'))))
nsfwNeko = json.load(open(os.path.join(directory_name,('images/nsfwNeko.json'))))
jahyImages = json.load(open(os.path.join(directory_name,('images/jahy.json'))))


wallpaperDesktop = json.load(open(os.path.join(directory_name,('images/wallpaper.json'))))
mobileWallpaper = json.load(open(os.path.join(directory_name,('images/mobileWallpaper.json'))))


nsfwMobileWallpaper = json.load(open(os.path.join(directory_name,('images/nsfwMobileWallpaper.json'))))

bdsmImages = json.load(open(os.path.join(directory_name,('images/bdsm.json'))))
creampieImages = json.load(open(os.path.join(directory_name,('images/creampie.json'))))
cumImages = json.load(open(os.path.join(directory_name,('images/cum.json'))))
mangaImages = json.load(open(os.path.join(directory_name,('images/manga.json'))))
hentaiImages = json.load(open(os.path.join(directory_name,('images/hentai.json'))))
eroImages = json.load(open(os.path.join(directory_name,('images/ero.json'))))
pantyImages = json.load(open(os.path.join(directory_name,('images/panties.json'))))
assImages = json.load(open(os.path.join(directory_name,('images/ass.json'))))
orgyImages = json.load(open(os.path.join(directory_name,('images/orgy.json'))))
femdomImages = json.load(open(os.path.join(directory_name,('images/femdom.json'))))
elvesImages = json.load(open(os.path.join(directory_name,('images/elves.json'))))
incestImages = json.load(open(os.path.join(directory_name,('images/incest.json'))))
cuckoldImages = json.load(open(os.path.join(directory_name,('images/cuckold.json'))))
hentaiGifs = json.load(open(os.path.join(directory_name,('images/hnt_gifs.json'))))
blowjobImages = json.load(open(os.path.join(directory_name,('images/blowjob.json'))))
boobjobImages = json.load(open(os.path.join(directory_name,('images/boobjob.json'))))
ahegaoImages = json.load(open(os.path.join(directory_name,('images/ahegao.json'))))
footImages = json.load(open(os.path.join(directory_name,('images/foot.json'))))
pussyImages = json.load(open(os.path.join(directory_name,('images/pussy.json'))))
uniformImages = json.load(open(os.path.join(directory_name,('images/uniform.json'))))
gangBangImages = json.load(open(os.path.join(directory_name,('images/gangbang.json'))))
glassesImages = json.load(open(os.path.join(directory_name,('images/glasses.json'))))
tentaclesImages = json.load(open(os.path.join(directory_name,('images/tentacles.json'))))
thighsImages = json.load(open(os.path.join(directory_name,('images/thighs.json'))))
yuriImages = json.load(open(os.path.join(directory_name,('images/yuri.json'))))
zettaiRyouikiImages = json.load(open(os.path.join(directory_name,('images/zettaiRyouiki.json'))))
masturbationImages = json.load(open(os.path.join(directory_name,('images/masturbation.json'))))
publicImages = json.load(open(os.path.join(directory_name,('images/public.json'))))
lickImages = json.load(open(os.path.join(directory_name,('images/lick.json'))))
slapImages = json.load(open(os.path.join(directory_name,('images/slap.json'))))
depressionImages = json.load(open(os.path.join(directory_name,('images/depression.json'))))
def wallpaper(): 
    return random.choice(wallpaperDesktop);

def mobileWallpaper(): 
    return random.choice(mobileWallpaper)

def neko(): 
    return random.choice(sfwNeko)

def jahy(): 
    return random.choice(jahyImages)

def slap(): 
    return random.choice(slapImages)

def lick():
    return random.choice(lickImages)

def depression():
    return random.choice(depressionImages)
class nsfw:
    def ass(): # Returns you ass Images ! #
        return random.choice(assImages)
    
    def bdsm(): # Returns you lewd ... and dirty ... BDSM Images ! #
        return random.choice(bdsmImages)
    
    def cum(): # Returns you cumshot and creampies Images ! #
        return random.choice(cumImages)
    
    def creampie(): # Returns a dirty creampie Images ! #
        return random.choice(creampieImages)
    
    def manga(): # Returns you Hentai-Manga Images ! #
        return random.choice(mangaImages)
    
    def femdom(): # Returns how Womans fucked Mans ! #
        return random.choice(femdomImages)
    
    def hentai(): # Returns you simple Hentai Images ! #
        return random.choice(hentaiImages)
    
    def incest(): # Returns you incest Images ! #
        return random.choice(incestImages)
    
    def ero(): # Returns you Erotic(ecchi) Images ! #
        return random.choice(eroImages)
    
    def orgy(): # Returns you lewd ... and dirty ... Orgy Images ! #
        return random.choice(orgyImages)
    
    def elves(): # Returns lewd ... and dirty ... Elves Images ! #
        return random.choice(elvesImages)
    
    def pantsu(): # Returns you panties Images ! #
        return random.choice(pantyImages)
    
    def cuckold(): # Return you a cuckold's moment ! #
        return random.choice(cuckoldImages)
    
    def blowjob(): # Returns you blowjobs Images ! #
        return random.choice(blowjobImages)
    
    def boobjob(): # Returns you boobjob Images ! #
        return random.choice(boobjobImages)
    
    def foot(): # Returns you lewd ... and dirty ... FootFetish Images ! #
        return random.choice(footImages)
    
    def vagina(): # Returns you lewd ... and dirty ... Pussy Images ! #
        return random.choice(pussyImages)
    
    def ahegao(): # Returns you lewd ... and dirty ... Ahegao Images ! #
        return random.choice(ahegaoImages)
    
    def uniform(): # Returns you NSFW Images with uniform ! #
        return random.choice(uniformImages)
    
    def gangbang(): # Returns you lewd ... and dirty ... GangBang Images ! #
        return random.choice(gangBangImages)
    
    def gif(): # Returns Hentai Gifs ! #
        return random.choice(hentaiGifs)
    
    def nsfwNeko(): # Returns you lewd ... and dirty ... Neko Images ! #
        return random.choice(nsfwNeko)
    
    def glasses(): # Returns you lewd ... and dirty ... Anime Girls with Glasses Images ! #
        return random.choice(glassesImages)
    
    def tentacles(): # Returns you lewd ... and dirty ... Tentacles Hentai Images ! #
        return random.choice(tentaclesImages)
    
    def thighs(): # Returns you sweet Thighs Images ! #
        return random.choice(thighsImages)
    
    def yuri(): # Returns you lewd ... two girls Images ! #
        return random.choice(yuriImages)
    
    def zettaiRyouiki(): # Returns you beatifull <3 ZettaiRyouiki Images ! #
        return random.choice(zettaiRyouikiImages)
    
    def masturbation(): # Returns you lewd masturbation Images ! #
        return random.choice(masturbationImages)
    
    def public(): # Returns you hentai on a Public Images ! #
        return random.choice(publicImages)
    
    def nsfwMobileWallpaper(): # Returns SFW Anime Wallpapers for Mobile Users ! #
        return random.choice(nsfwMobileWallpaper)
    

