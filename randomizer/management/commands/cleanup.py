with open("randomizer/management/commands/battledisassembler.py", 'r') as infile:
    hw = infile.readlines().replace(chr(0), '')