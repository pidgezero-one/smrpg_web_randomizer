# E2162_KEEP_TERRA_COTTA_BATTLE_ROOM_SUMMON_2ND_BATTLE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2162_ret_26"]),
        SetBit(TEMP_7043_2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=12, y=46, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASResetProperties(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=10, y=49, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2162_create_packet_at_npc_coords_7"]),
        RunEventAsSubroutine(E0941_KEEP_FIRST_BOSS_SET_SCRIPT),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_2,
            destinations=["EVENT_2162_create_packet_at_npc_coords_7"],
            identifier="EVENT_2162_create_packet_at_npc_coords_7",
        ),
        SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
        ActionQueueSync(target=MARIO, subscript=[ASPause(5), ASFaceSouthwest7D()]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASPause(40),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(60),
            ],
        ),
        StartBattleAtBattlefield(225, BF07_BOWSERS_KEEP),
        JmpIfBitClear(GAME_OVER, ["EVENT_2162_action_queue_sync_17"]),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        Return(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=9, y=47, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
            identifier="EVENT_2162_action_queue_sync_17",
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=11, y=51, z=0, direction=EAST),
                ASVisibilityOff(),
            ],
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            mod_id=34,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            mod_id=2,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            mod_id=35,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            mod_id=3,
        ),
        FadeInFromBlack(sync=False),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_0,
            destinations=["EVENT_2162_create_packet_at_npc_coords_24"],
            identifier="EVENT_2162_create_packet_at_npc_coords_24",
        ),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            object=NPC_2,
            destinations=["EVENT_2162_create_packet_at_npc_coords_24"],
        ),
        Return(identifier="EVENT_2162_ret_26"),
    ]
)
