# BoredDeveloperBot
This repo holds the source code for a discord bot used for the BoredDevelopers Discord server. This bot is hosted on [Docker Hub](https://hub.docker.com/repository/docker/hector7500/bored-developer-bot/general) and can be 
used for any server as long as you your own discord access token. It will need a .env file, which you can copy from the .env-example to run locally or via docker.


## Run Image locally 
To run this image locally:
1. you must first copy the `.env-example` file to a file named `.env` and replace the {values} with corrosponding values for your useage
1. run the following command `python src/main.py` from the root of this project. 


## Contributing to this Project
Please make desired changes and open a pull request to go to `master`. Someone with mainter access will review the code and either approve or 
leave comments in the MR.