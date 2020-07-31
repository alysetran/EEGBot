20- README explaining solution and purpose
20- installation and execution instructions (in README file)

# circuit2020_BYTES_OrderOfThePhoenix_hogwarts_hippopotami

#Documentation for Reconchess Challenge:

#Final Bot for Reconchess: OmnipotentBot_1

The strategy for the OmnipotentBot is primarily based upon a set of pre-defined moves. The purpose of the bot is to iterate through the set of moves to lead to a 
fast and decisive victory where the other king is taken. The strategies that were selected for the bot are arranged based upon priority. The initial priority it to 
try and take the opposition's king while protecting our own. Initially, we are trying to protect the weakest spot on the board that only the king defends, then 
moving knights and the scholar's mate to attack the other king. Then, we choose to castle to protect our own king. 

The installation and execution for the OmnipotentBot just requires installation of reconchess through the terminal followed by copying and pasting the code into 
pycharm or a gitpull. You use the rc-bot play command in the terminal to run OmnipotentBot against other bots. 

#Documentation for BCI Challege:

#Final Bot for BCI: EEG_Final

The strategy for the BCI challenge is primarily to modify a pre-existing bot for the challenge. The strategy behind the bot is to look at the training data and 
assign them by a linear regression model. Due to many issues with reading the data for the challenge and finding the path, Hogwarts Hippoptomi has included a part 
to the code to locate the correct CSV files and path to run in the program. Additionally, a butter filter was added with bandpass, lowpass, and highpass that was
used dependent upon the critical frequency and outputs an numpy array. The overall strategy was to classify the training data through a combination of linear
regression and a butter filter. 

The installation and execution of the bot occurs in Jupyter Notebook. The installation requires that the files from Kaggle are downloaded properly. The first few 
lines of code finds the filepath of the csv files to make it easier in the execution. Once the files have been properly read, the program can be run. 
