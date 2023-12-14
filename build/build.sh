#!/bin/bash

# MINECRAFT_VER=1.20.2
# FABRIC_VER=0.14.23
# FABRIC_INSTALLER_VER=0.11.2

docker buildx build \
  --push \
  --platform linux/arm/v7,linux/arm64,linux/amd64 \
  --build-arg "MINECRAFT_VER=$MINECRAFT_VER" \
  --build-arg "FABRIC_VER=$FABRIC_VER" \
  --build-arg "FABRIC_INSTALLER_VER=$FABRIC_INSTALLER_VER" \
  --tag "dowerx/minecraft:${MINECRAFT_VER}-${FABRIC_VER}-${FABRIC_INSTALLER_VER}" \
  --tag "dowerx/minecraft:${MINECRAFT_VER}" \
  --tag "dowerx/minecraft:latest" \
  -f Dockerfile \
  .