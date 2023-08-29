#!/bin/bash

cd "$(dirname "$0")"

mkdir -p config mods world logs
touch ./config/server.properties
for i in banned-ips.json banned-players.json ops.json usercache.json whitelist.json; do
    echo '[]' > ./config/$i
done