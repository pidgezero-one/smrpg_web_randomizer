# Super Mario RPG Open World Randomizer

New web-based randomizer for Super Mario RPG based on the original command line [Gentle Beauty and Raw Power](https://github.com/abyssonym/smrpg_gbarp) randomizer by abyssonym.

This web version is a Django-powered site in a Docker container.  It is assumed you know how to deploy Django and Docker to use this.

If you came here just looking to use the randomizer to generate games, head to [the official community website](http://randomizer.smrpgspeedruns.com) where we host this for everyone.  This repository is only needed if you want to contribute to the development of the randomizer.

## Install Docker

You will need to install Docker on your system.  Instructions for this are available on the [official Docker site](https://docs.docker.com/get-docker/).

## Developing locally

Once you've installed Docker (either the desktop client or command line interface), run the main `docker-compose.yml` file to build and run the development container:

```> docker compose up --build```

The development environment files are `.env.dev` and `.env.dev.db`.  These are set up to use testing values and run the Django development server on localhost port 8000.  You can change these as needed.

## Deploying to production

1. Make a copy of the example production environment files:

   ```> cp example.env.prod .env.prod```

   ```> cp example.env.prod.db .env.prod.db```

   ```> cp example.env.prod.nginx .env.prod.nginx```

1. Change the production environment settings as needed.  You should generate a proper Django secret value and more secure database password at the very least.

1. Run the `docker-compose.prod.yml` file to build and run the production container:

   ```> docker compose -f docker-compose.prod.yml up --build -d```

This will run the production server in detached mode.  You can check the logs with:

```> docker compose -f docker-compose.prod.yml logs -f```

This will run a production Nginx web server on port 80 which forwards to the Django app using gunicorn, and also serves the static files through the web server.  You can change this in the `.env.prod.nginx` file if needed.

## Space optimization

The randomizer's patcher will attempt to allocate any unused space left over after encoding dialogs, event scripts, action scripts, battle events, or monster AI and repurpose it for sprite animation data. This is to make more room for sprite tiles.

Bank 0x35 for battle animations is also tightly packed, so adding new animations is difficult due to lack of space.

Some helpful scripts you can run (in the `scripts` folder):
- `analyze_repeated_sequences.py` - This will show you a list of command sequences in battle animation banks 0x35xxxx and 0x3Axxxx that are repeated in multiple places and would encode to 3 or more bytes. Consider giving the first command in one such instance a unique identifier, and replace all other instances with a `Jmp` to that identifier (which is 3 bytes). This will free up battle animation space. (If the sequence does not already end in `ReturnSubroutine` or `ReturnSpriteQueue`, you may have to extract the sequence elsewhere, end it it a return command, replace all original instances with a `Jmp` to your moved sequence, and test your ROM thoroughly to make sure it is not breaking anything. SMRPG can be volatile about nested subroutines.) Produces `repeated_sequences_report.txt`
- `show_3a_free_space.py` - This details how much space in each script within animation data bank 0x3Axxxx is actually being used by animation code. Consider moving code around between scripts to create as many large contiguous empty blocks as possible to be repurposed for sprite code.
- `find_referenced_empty_dialogs.py` - This will find dialogs that are used in event scripts but have no content. Use this to fix dialog bugs.
- `find_unreferenced_dialogs_with_content.py` - This will find dialogs that are not used anywhere but have non-empty content, and do not share data with dialogs that are used somewhere. Produces `unreferenced_dialogs.txt`
- `empty_dialog.py` - Run this against a dialog ID that you know is not used anywhere (usually the results of `find_unreferenced_dialogs_with_content.py`). It will empty the dialog's data and replace it with `[await]`. Be careful not to run it against unused dialogs that share data with used dialogs.
- `compress_dialogs.py` - Removes every empty `[await]` dialog in your dialog table data files and shifts dialog pointers accordingly. Each `[await]` is a single byte, and this adds up when there are a lot of them, so this will condense your dialog data such that it leaves a large contiguous empty block at the end to be repurposed for sprite code.


## Adding user submissions

Make sure you've installed the GitHub CLI and authed to it.

### Wish Text

```bash
python scripts/add_submission.py --type wish --issue GITHUB_ISSUE_ID
```

### Quiz questions (SMRPG-related)

```bash
python scripts/add_submission.py --type quiz --issue GITHUB_ISSUE_ID
```

### Quiz questions (non-SMRPG, extended pool only)

```bash
python scripts/add_submission.py --type quiz --issue GITHUB_ISSUE_ID --non-smrpg
```

### Ship passwords
```bash
python scripts/add_submission.py --type password --issue GITHUB_ISSUE_ID
```

### Melody Bay songs
```bash
python scripts/add_submission.py --type song --issue GITHUB_ISSUE_ID
```

### Dry run (parse only, don't modify files)
```bash
python scripts/add_submission.py --type TYPE --issue GITHUB_ISSUE_ID --dry-run
```