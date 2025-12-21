# Contributing

## Basics

If you are new to SMRPG modding, it is strongly recommended to look around the game in the [Lazy Shell editor](https://github.com/Yakibomb/LAZYSHELL-UPDATED/releases). This is a powerful ROM-editing GUI specifically designed for SMRPG that will greatly help you visualize how some of the most important parts of the game work.

Much of the randomizer's foundations are based in the [smrpgpatchbuilder](https://github.com/pidgezero-one/smrpgpatchbuilder) library, which allows you to edit most of the randomizer-relevant game features as Python code and produces the bytes needed to patch those edits to the game. This library was designed to resemble the workflows and verbiage of Lazy Shell as much as possible.

The vast majority of things you will want to edit in this randomizer require no ASM knowledge.

### Settings

All randomizer settings are defined in randomizer/types/flags.py. You can see the breakdown of how different kinds of settings work, i.e. checkboxes vs selecting from a list.

### Tables

Most game data that doesn't affect progression logic is stored in tables, such as enemy stats, shop contents, weapon and armor stats, etc. Most of these things that are relevant to the randomizer are in the data folder. There are individual classes for each item/enemy/ally/etc with properties that represent their shuffle-able attributes, so they are pretty straightforward to interact with. These classes are based on smrpgpatchbuilder types so they have ROM-patching code built-in.

### Script System

Super Mario RPG's internal logic was originally designed around a **script system**. Scripts are more or less a series of ASM "shortcuts" in that they allow you do to memory operations in a safe, controlled, and simple manner. For example, adding an item to your inventory is just a single script command.

This design choice made it easy for anybody on the original development team to add easter eggs and funny non-required interactions to the game. It also makes it easy for us to mod the game! 

Most of what you will see happening in any world area or any battle is controlled by scripts. There are four kinds of scripts:

* **Event scripts**: These control the logic of just about anything that happens in a world area. Talk to a NPC? That's a script. Go from one room to another? That's a script. A new world area becomes accessible? Scripts did that. Start a boss battle? That's a script. Play Booster's curtain minigame? That's a complex series of scripts.
* **Action scripts**: These control how objects in a room are animated. These can be standalone scripts that are assigned as a property to a NPC, or they might be embedded inside an event script to force something to animate on the fly in response to another action, i.e. being talked to.
* **Monster AI**: These control the decision making of any enemy in battle, such as choosing spells, countering attacks, etc.
* **Battle Animation Scripts**: These control everything else in battle, such as weapon and spell animations, cutscenes, Super Jump logic, etc.

All of the progression logic and prize grants in SMRPG Randomizer are controlled by scripts. This is usually what you want to edit if you would like to add a feature that deals with progression logic (i.e. adding conditions to open a world area) or retrofitting exising game features to accommodate various states of the randomizer seed that were not expected in the original game (i.e. adding logic to determine what happens in the Valentina fight if you only have two characters). 

Scripts require no ASM knowledge whatsoever to edit.

To start off, check out gameworld.py to see how the game's scripts are adjusted according to what settings the end user has selected.

Edited scripts are assembled into a table and turned into patch bytes by smrpgpatchbuilder. This is built-in and you don't need to worry about how you're going to patch your script changes to the ROM.

### Etc

There are lots of other features in the game that are important to the randomizer, such as level exits, dialogs, etc. Look around in the Lazy Shell editor to see how these work. Most of these things you will find in the randomizer/data folder. It's recommended to explore the codebase for the randomizer a bit to see how these features are interacted with and modified.

## Design Philosophy

Follow these guidelines when developing for this randomizer:

### Stick to the spirit of the original game

The experience of playing SMRPG Randomizer should adhere to the experience of playing "the original game but shuffled" as much as possible, with some concessions in favour of scavenger hunt design. This means working with what the original game already offers us and avoiding adding things it never had. 

These are examples of things that generally should not be done:
* Inventing new spells that didn't exist originally, especially if replacing existing spells
* Adding prize checks to NPCs that never originally gave you anything
* Adding new characters or new enemies (i.e. from Paper Mario or M+L games or other SMRPG romhacks)
* Adding new items, unless it would make for a _really_ interesting progression feature (i.e. shuffling Garro's paint to unlock Nimbus Castle)

Adding concepts from the 2023 Switch remake is an exception to all of the above. References to other media in the form of character palettes or NPC dialogs are also completely fine.

A good way to think about changing what's canon to the original game is to consider bringing some utility to things that would otherwise be underused or never used (think the Ice Arrows in OOT being modified to act like Blue Fire, or the Spoon in FFIV becoming a weapon for Edward) or to restore some importance to items that could become fairly useless in a randomizer setting. In SMRPG Randomizer, there are some examples of this:
* A setting that infuses standard shop armors with certain immunities
* A setting that gives poison mushrooms a 1/8 chance of acting as a Red Essence
* A setting that turns two underserved locales into final boss warps
* A setting that makes the trade quest for the Monstro Town sealed door join the shuffle (as opposed to Shiny Stones being infinitely purchaseable in shops)

The important thing is to make sure these things are optional and disabled by default, so that players expecting the original game's experience will get that, but players who want to add some more depth to underused parts of the game have that choice.

If you are adding new options for progression logic, try to keep the conditions as close to the logic of the original game as possible. i.e. you can choose to unlock Bandit's Way by recruiting Mallow, clearing Mushroom Way, or defeating the Hammer Bros (wherever they might be), because these are all things that happen in the original game just before you go to Bandit's Way. Something like "Defeat Culex to unlock Forest Maze" would not make sense.

### Don't make the open world map annoying to use

The overworld map must **always** form a complete loop. No exceptions to this, it's the entire basis of the "open world" concept as applied to a game that doesn't have a freely explorable overworld map. 

If you want to gate an area that would break the overworld map loop, i.e. Land's End or Pipe Vault, consider adding non-intrusive features to the level that would prevent the player from proceeding beyond a certain point instead of shutting off the overworld map dot for that area. i.e. blocking a pipe, disabling a trampoline or a cannon, etc. 

Changing the shape of the level terrain (solidity mods) to accomplish this will usually not be approved unless it makes sense in-world. Example:
* locking the door to the entrance of Mushroom Kingdom Castle = ✅
* changing the height of the cliff in Land's End = ❌.

### Check-for-check

All prizes that could only be obtained once in the original game are item checks (i.e. treasure chests, boss battle prizes, hotel rewards, etc). 

Prizes that can be obtained infinitely are NOT item checks (i.e. Mushroom Boy's items, Marrymore tips other than the Flower Box).

(Exception: All treasure chests are checks, even the few that could originally be opened infinitely.)

However, a -sanity feature to add checks to these repeatable prize grants would probably be approved if designed well.

## Will players like my idea?

You can bring up the thing you plan to develop in the #snes-rando-feature-discussion channel of https://discord.smrpgspeedruns.com. Although, even if nobody would use the feature except you, you can still add it as long as it adheres to the above guidelines and does not upend any existing features. This randomizer is all about choice.

## Crediting

Add yourself to credits.py. This project is a labour of love that nobody gets paid for, everyone who contributes to it deserves recognition. 
* It's hard to tell from code alone how your changes to the credits screen will be aligned, so be sure to test the credits before submitting your PR.
* Only capital letters A-Z, spaces, periods, and underscores are supported.
* If you've just developed a new optional feature, i.e. adding Mushroom Boy as a check, add yourself to the "Development" list. If you've developed something foundational to how the randomizer works as a whole, i.e. creating an entrance randomizer, add yourself to the "Core Development" list.
* Credit anybody who helped you on the feature whether they contributed code or research.
* If you borrowed code from somebody else's romhack that was not explicitly developed for the randomizer, add them to the "Special Thanks" section.
  * If anybody else besides the developer helped you find such code, add them as well.