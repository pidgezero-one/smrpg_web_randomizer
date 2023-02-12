# E2168_KEEP_ALLEY_RAT_BATTLE_ROOM_SUMMON_3RD_BATTLE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2168_ret_26"]),
        SetBit(TEMP_7043_3),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=16, y=38, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASResetProperties(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=14, y=41, z=1, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2168_create_packet_at_npc_coords_7"]),
        RunEventAsSubroutine(E0941_KEEP_FIRST_BOSS_SET_SCRIPT),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_3,
            destinations=["EVENT_2168_create_packet_at_npc_coords_7"],
            identifier="EVENT_2168_create_packet_at_npc_coords_7",
        ),
        SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
        ActionQueueSync(target=MARIO, subscript=[ASPause(5), ASFaceSouthwest7D()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASPause(40),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(60),
            ],
        ),
        StartBattleAtBattlefield(230, BF07_BOWSERS_KEEP),
        JmpIfBitClear(GAME_OVER, ["EVENT_2168_action_queue_sync_17"]),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        Return(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=13, y=39, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
            identifier="EVENT_2168_action_queue_sync_17",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=15, y=43, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            mod_id=36,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            mod_id=4,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            mod_id=37,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            mod_id=5,
        ),
        FadeInFromBlack(sync=False),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_0,
            destinations=["EVENT_2168_create_packet_at_npc_coords_24"],
            identifier="EVENT_2168_create_packet_at_npc_coords_24",
        ),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_3,
            destinations=["EVENT_2168_create_packet_at_npc_coords_24"],
        ),
        Return(identifier="EVENT_2168_ret_26"),
    ]
)
