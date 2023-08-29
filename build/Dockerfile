FROM alpine AS build

ARG MINECRAFT_VER=1.20.1
ARG FABRIC_VER=0.14.22
ARG FABRIC_INSTALLER_VER=0.11.2

RUN apk add --no-cache wget
RUN wget -O /server.jar https://meta.fabricmc.net/v2/versions/loader/$MINECRAFT_VER/$FABRIC_VER/$FABRIC_INSTALLER_VER/server/jar

FROM eclipse-temurin:17-jre-jammy

ARG EULA=false

RUN mkdir /minecraft && echo "eula=$EULA" > /minecraft/eula.txt
COPY --from=build /server.jar /minecraft/server.jar

EXPOSE 25565
EXPOSE 25575

ENV JAVA_FLAGS=-Xmx2G
WORKDIR /minecraft
ENTRYPOINT java $JAVA_FLAGS -jar /minecraft/server.jar nogui