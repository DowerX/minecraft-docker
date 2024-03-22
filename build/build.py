#!/bin/env python3

import subprocess
from enum import Enum

class Action(Enum):
    PUSH = "--push"
    LOAD = "--load"

class Platform(Enum):
    amd64 = "linux/amd64"
    arm64 = "linux/arm64"
    armv6 = "linux/arm/v6"
    armv7 = "linux/arm/v7"

class PlatformConfig:
    def __init__(self, platform: Platform, dockerfile: str, directory: str, args: dict[str, str], tags: list[str]):
        self.platform = platform
        self.directory = directory
        self.dockerfile = dockerfile
        self.args = args
        self.tags = tags

    def run(self, registry: str, library: str, name:str, action: Action, repo: str) -> int:
        command = ["docker", "buildx", "build",
                   action.value,
                   "--platform", self.platform.value,
                   "-f", self.dockerfile]
        
        for tag in self.tags:
            command.append("--tag")
            command.append(f"{registry}/{library}/{name}:{tag}")

        for arg in self.args.items():
            command.append("--build-arg")
            command.append(f"{arg[0]}={arg[1]}")

        command.append(self.directory)

        return subprocess.run(command, cwd=repo).returncode

class Builder:
    def __init__(self, name: str, repo: str, platforms: list[PlatformConfig], action: Action, registry: str, library: str):
        self.name = name
        self.repo = repo
        self.platforms = platforms
        self.action = action
        self.registry = registry
        self.library = library

    def run(self):
        for platform in self.platforms:
            print(f"Building for {platform.platform}...", end="")
            if platform.run(self.registry, self.library, self.name, self.action, self.repo) != 0:
                raise Exception(f"failed to complete build for {platform.platform}")
            print("Done!")
    
    def tag(self, tag: str) -> int:
        command = ["docker", "buildx", "imagetools", "create",
                   "-t", f"{self.registry}/{self.library}/{self.name}:{tag}"]
        
        for platform in self.platforms:
            command.append(f"{self.registry}/{self.library}/{self.name}:{platform.tags[0]}")
        
        return subprocess.run(command).returncode

    def latest(self) -> int:
        return self.tag("latest")