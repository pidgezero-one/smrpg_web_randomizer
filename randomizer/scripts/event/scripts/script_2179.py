# E2179_KEEP_GOOMBA_BATTLE_ROOM_SUMMON_4TH_BATTLE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_4, ["EVENT_2179_ret_26"]),
        SetBit(TEMP_7043_4),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=20, y=30, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASResetProperties(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=18, y=33, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2179_create_packet_at_npc_coords_7"]),
        RunEventAsSubroutine(E0941_KEEP_FIRST_BOSS_SET_SCRIPT),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_4,
            destinations=["EVENT_2179_create_packet_at_npc_coords_7"],
            identifier="EVENT_2179_create_packet_at_npc_coords_7",
        ),
        SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
        ActionQueueSync(target=MARIO, subscript=[ASPause(5), ASFaceSouthwest7D()]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASPause(40),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(50),
            ],
        ),
        StartBattleAtBattlefield(239, BF07_BOWSERS_KEEP),
        JmpIfBitClear(GAME_OVER, ["EVENT_2179_action_queue_sync_17"]),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        Return(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=17, y=31, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
            identifier="EVENT_2179_action_queue_sync_17",
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=19, y=35, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            mod_id=38,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            mod_id=6,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            mod_id=39,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            mod_id=7,
        ),
        FadeInFromBlack(sync=False),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_0,
            destinations=["EVENT_2179_create_packet_at_npc_coords_24"],
            identifier="EVENT_2179_create_packet_at_npc_coords_24",
        ),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_4,
            destinations=["EVENT_2179_create_packet_at_npc_coords_24"],
        ),
        Return(identifier="EVENT_2179_ret_26"),
    ]
)
