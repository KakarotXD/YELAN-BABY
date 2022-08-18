![Shikimori](https://telegra.ph/file/d0c1cd93423c66c099b48.jpg)

<h2 align="center">
    ──「 SHIKIMORI IS A MODULAR BOT WITH ANIME THEME 」──
</h2>

<p align="center">
  <a href="https://github.com/SOME-1HING/ShikimoriBot/blob/master/LICENSE"> <img src="https://img.shields.io/badge/License-GPLv3-blueviolet?style=for-the-badge" alt="License" /> </a>
  <a href="https://makeapullrequest.com"> <img src="https://img.shields.io/badge/PRs-Welcome-yellow?style=for-the-badge" alt="PRs" /></a></br>
  <a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Made%20With-Python-orange?style=for-the-badge&logo=python" alt="Python" /> </a>
  <a href="https://github.com/SOME-1HING/ShikimoriBot"> <img src="https://img.shields.io/badge/Maintained-Yes-lightgrey?style=for-the-badge" alt="Maintenance" /> </a>
</p>

<h2 align="center">
    ──「 DOCUMENTATION 」──
</h2>

<p align="center">
<p align="center"><a href="https://some1hing.gitbook.io/shikimori-bot/"> <img src="https://img.shields.io/badge/DOCUMENTATION-grey?style=for-the-badge&logo=gitbook" width="220" height="38.45"/></a>
</p>

<h2 align="center">
    ──「 SUPPORT 」──
</h2>

<p align="center">
<a href= "https://t.me/micchon_shikimori_bot"> <img src="https://img.shields.io/badge/Shikimori-Bot-green?style=for-the-badge&logo=telegram" alt=Yor_Forger on Telegram" /> </a>
<a href= "https://t.me/tyranteyeeee"> <img src="https://img.shields.io/badge/Support-Chat-green?style=for-the-badge&logo=telegram" alt="Support Chat" /> </a>
<a href="https://t.me/SOME1_HING"> <img src="https://img.shields.io/badge/SOME1HING-Channel-green?style=for-the-badge&logo=telegram" alt="Update Channel" /> </a>
</p>

<h2 align="center">
    ──「 CREDIT 」──
</h2>

<p align="center">
<a href="https://github.com/SOME-1HING"> <img src="https://img.shields.io/badge/SOME1HING-Github-magenta?style=for-the-badge&logo=github" alt="SOME-1HING Github" /> </a>
<a href="https://github.com/asadali32117"> <img src="https://img.shields.io/badge/asadali32117-Github-magenta?style=for-the-badge&logo=github" alt="Ryu120 Github" /> </a>
</p>

## How to setup/deploy.

### Read these notes carefully before proceeding 
 - Your code must be open source and a link to your fork's repository must be there in the start reply of the bot.

<details>
  <summary>Steps to deploy on Heroku !!</summary>

```
Fill in all the details, Deploy!
Now go to https://dashboard.heroku.com/apps/(app-name)/resources ( Replace (app-name) with your app name )
REMEMBER: Turn on worker dyno (Don't worry It's free :D) & Webhook
Now send the bot /start, If it doesn't respond go to https://dashboard.heroku.com/apps/(app-name)/settings and remove webhook and port.
```

  <h2 align="center">
    ──「 DEPLOY ON HEROKU 」──
</h2>

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/SOME-1HING/ShikimoriBot/tree/Stable-v1.3"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

</details>  
<details>
  <summary>Steps to self Host!! </summary>

  ## Setting up the bot (Read this before trying to use!):
Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older Python versions!
This is because markdown parsing is done by iterating through a dict, which is ordered by default in 3.6.

  ### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The preferred version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `Shikimori` folder, alongside the `__main__.py` file. 
This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of
your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all
defaults set in the sample_config, hence making it easier to upgrade.

An example `config.py` file could be:
```
from Shikimori.sample_config import Config

class Development(Config):
    OWNER_ID = 254318997  # your telegram ID
    OWNER_USERNAME = "SonOfLars"  # your telegram username
    API_KEY = "your bot api key"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    DRAGONS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
```

If you can't have a config.py file (EG on Heroku), it is also possible to use environment variables.
So just go and read the config sample file. 

  ### Python dependencies

Install the necessary Python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all the necessary python packages.

  ### Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes),
you'll need to have a database installed on your system. I use Postgres, so I recommend using it for optimal compatibility.

In the case of Postgres, this is how you would set up a database on a Debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the Postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you need to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever DB you're using (eg Postgres, MySQL, SQLite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and DB name.

  ## Modules
   ### Setting load order.

The module load order can be changed via the `LOAD` and `NO_LOAD` configuration settings.
These should both represent lists.

If `LOAD` is an empty list, all modules in `modules/` will be selected for loading by default.

If `NO_LOAD` is not present or is an empty list, all modules selected for loading will be loaded.

If a module is in both `LOAD` and `NO_LOAD`, the module will not be loaded - `NO_LOAD` takes priority.

   ### Creating your own modules.

Creating a module has been simplified as much as possible - but do not hesitate to suggest further simplification.

All that is needed is that your .py file is in the modules folder.

To add commands, make sure to import the dispatcher via

`from SungJinwooRobot import dispatcher`.

You can then add commands using the usual

`dispatcher.add_handler()`.

Assigning the `__help__` variable to a string describing this modules' available
commands will allow the bot to load it and add the documentation for
your module to the `/help` command. Setting the `__mod_name__` variable will also allow you to use a nicer, user-friendly name for a module.

The `__migrate__()` function is used for migrating chats - when a chat is upgraded to a supergroup, the ID changes, so 
it is necessary to migrate it in the DB.

The `__stats__()` function is for retrieving module statistics, eg number of users, number of chats. This is accessed 
through the `/stats` command, which is only available to the bot owner.

## Starting the bot.

Once you've set up your database and your configuration is complete, simply run the bat file(if on windows) or run (Linux):

`python3 -m Shikimori`

You can use [nssm](https://nssm.cc/usage) to install the bot as service on windows and set it to restart on /gitpull 
Make sure to edit the start and restart bats to your needs. 
Note: the restart bat requires that User account control be disabled.


## How to setup on Heroku 
For starters click on this button 

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/SOME-1HING/ShikimoriBot"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

