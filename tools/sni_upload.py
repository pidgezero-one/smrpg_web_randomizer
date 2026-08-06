#!/usr/bin/env python3
"""Upload a ROM to FxPakPro via SNI and boot it.

Usage:
    python tools/sni_upload.py path/to/rom.sfc --host 172.26.240.1:8191
"""

import argparse
import sys
from pathlib import Path

import grpc
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload ROM to FxPakPro via SNI")
    parser.add_argument("rom", help="Path to the ROM file to upload")
    parser.add_argument("--host", default="localhost:8191", help="SNI host:port")
    parser.add_argument("--dest", default=None,
                        help="Destination path on FxPakPro SD card (default: use ROM filename)")
    parser.add_argument("--no-boot", action="store_true", help="Upload only, don't boot")
    args = parser.parse_args()

    rom_str = args.rom
    # Convert Windows paths to WSL paths (C:\Users\... → /mnt/c/Users/...)
    if len(rom_str) >= 2 and rom_str[1] == ":" and rom_str[0].isalpha():
        drive = rom_str[0].lower()
        rom_str = f"/mnt/{drive}" + rom_str[2:].replace("\\", "/")
    rom_path = Path(rom_str)
    if not rom_path.exists():
        print(f"ROM not found: {rom_path}")
        sys.exit(1)

    rom_data = rom_path.read_bytes()
    if args.dest is None:
        args.dest = "/" + rom_path.name
    print(f"ROM: {rom_path.name} ({len(rom_data) // 1024} KB)")

    with grpc.insecure_channel(args.host) as ch:
        # Find device
        devices_stub = sni.DevicesStub(ch)
        resp = devices_stub.ListDevices(pb.DevicesRequest(kinds=[]))
        if not resp or not resp.devices:
            print("No device found. Is SNI running?")
            sys.exit(1)
        uri = resp.devices[0].uri
        print(f"Device: {uri}")

        # Upload
        fs_stub = sni.DeviceFilesystemStub(ch)
        print(f"Uploading to {args.dest}...")
        put_resp = fs_stub.PutFile(pb.PutFileRequest(
            uri=uri,
            path=args.dest,
            data=rom_data,
        ))
        print(f"Uploaded {len(rom_data) // 1024} KB")

        # Boot
        if not args.no_boot:
            print("Booting...")
            fs_stub.BootFile(pb.BootFileRequest(uri=uri, path=args.dest))
            print("Done! ROM is running.")
        else:
            print("Uploaded (not booted).")


if __name__ == "__main__":
    main()
