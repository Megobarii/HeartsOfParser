# HeartsOfParser

A Python parser for *Hearts of Iron III* savegames that reconstructs the order of battle hierarchy from theatre to regiment.

It detects units through indentation and keywords, links them to their commanders, and enforces game rules such as the maximum of five subordinates per HQ for structured analysis.

---

## Overview

There are several aspects that can be improved, such as reducing code repetition and increasing overall efficiency.

Some features are already implemented but not fully used. For example, each unit object can store its commander, but currently the hierarchy is represented only through indentation.

This unused structure could later be used to:
- search for specific units
- build an interactive reorganization tool
- support automatic order-of-battle optimization

---

## How to use

1. Place a *Hearts of Iron III* savegame in the same directory as the script  
2. Rename it to:
  savegame.txt

3. Run the Python script  
4. Enter a country tag when prompted

---

## Country tags example

- Germany → GER  
- United Kingdom → ENG  
- Italy → ITA  
- Japan → JAP  

---

## Output

After entering a valid country tag, the script outputs the full land unit order of battle.

The hierarchy is displayed using indentation to represent command structure (who commands whom and who is subordinate).

> Note: Only land units are currently supported. Ships and air units are not included.
