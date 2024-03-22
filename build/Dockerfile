FROM eclipse-temurin:17-jre-jammy as build

ARG MINECRAFT_VER=1.20.4
ARG FABRIC_VER=0.15.7
ARG FABRIC_INSTALLER_VER=1.0.0

RUN mkdir /minecraft && \
    wget -O /minecraft/server.jar https://meta.fabricmc.net/v2/versions/loader/$MINECRAFT_VER/$FABRIC_VER/$FABRIC_INSTALLER_VER/server/jar
WORKDIR /minecraft
RUN java -jar ./server.jar

FROM eclipse-temurin:17-jre-jammy

ARG EULA=false

RUN mkdir /minecraft && echo "eula=$EULA" > /minecraft/eula.txt

COPY --from=build /minecraft/server.jar /minecraft
COPY --from=build /minecraft/libraries /minecraft/libraries
COPY --from=build /minecraft/versions /minecraft/versions
COPY --from=build /minecraft/.fabric /minecraft/.fabric

EXPOSE 25565
EXPOSE 25575

ENV JAVA_FLAGS=-Xmx2G
WORKDIR /minecraft
ENTRYPOINT java $JAVA_FLAGS -jar /minecraft/server.jar nogui