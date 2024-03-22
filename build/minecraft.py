#!/bin/env python3

from build import *

MINECRAFT_VER = input("MINECRAFT_VER=")
FABRIC_VER = input("FABRIC_VER=")
FABRIC_INSTALLER_VER = input("FABRIC_INSTALLER_VER=")

builder = Builder(
    "minecraft",
    ".",
    [
        PlatformConfig(Platform.arm64, "Dockerfile", ".",
            {"MINECRAFT_VER":        MINECRAFT_VER,
             "FABRIC_VER":           FABRIC_VER,
             "FABRIC_INSTALLER_VER": FABRIC_INSTALLER_VER },
            [f"{MINECRAFT_VER}-{FABRIC_VER}-{FABRIC_INSTALLER_VER}-arm64",
             f"{MINECRAFT_VER}-arm64", "arm64"]),
        PlatformConfig(Platform.amd64, "Dockerfile", ".",
            {"MINECRAFT_VER":        MINECRAFT_VER,
             "FABRIC_VER":           FABRIC_VER,
             "FABRIC_INSTALLER_VER": FABRIC_INSTALLER_VER },
            [f"{MINECRAFT_VER}-{FABRIC_VER}-{FABRIC_INSTALLER_VER}-amd64",
             f"{MINECRAFT_VER}-amd64", "amd64"]),
    ],
    Action.PUSH, "registry.tek.govt.hu", "dowerx")

builder.run()
builder.tag(f"{MINECRAFT_VER}-{FABRIC_VER}-{FABRIC_INSTALLER_VER}")
builder.tag(f"{MINECRAFT_VER}")
builder.latest()