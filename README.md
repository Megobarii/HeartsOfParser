# HeartsOfParser
Python parser for Hearts of Iron III savegames that reconstructs the order of battle hierarchy from theatre to regiment. It detects units by indentation and keywords links them to their commanders and enforces game rules like five subordinates per HQ for clear structured analysis.

------------------------------------------------------------------------------------------------------------------------------------------

There are many aspects that can be improved such as reducing code repetition and increasing overall efficiency. Some features are already implemented but not yet used for example each unit object can store its commander but at the moment the hierarchy is represented only through indentation. This unused structure could become useful in the future to allow searching for specific units or to turn the parser into an interactive tool for reorganization. It could even support automatic organization of the order of battle.

------------------------------------------------------------------------------------------------------------------------------------------

# How to use:

Place a Hearts of Iron III savegame in the same directory as the Python script and rename it to savegame.txt. Then run the script. The program will prompt you to enter a country tag for the nation whose order of battle you want to view. For example

Germany = GER

United Kingdom = ENG

Italy = ITA

Japan = JAP

After entering the tag and pressing enter the script will output the full land unit order of battle. The hierarchy will be shown with indentation to indicate command structure who commands whom and who is subordinate. Note that the current version only includes land units, ships and planes are not displayed.
