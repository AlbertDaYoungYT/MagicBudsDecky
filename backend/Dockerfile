FROM ubuntu:22.04 AS system_stage

RUN apt-get update
RUN apt-get install cargo -y
RUN apt-get install libsystemd-dev -y
RUN apt-get install git -y
RUN apt-get install zlib1g-dev -y
RUN apt-get install bluez-libs -y
RUN apt-get install libpulse -y
RUN apt-get install dbus -y
RUN apt-get install python3 -y


FROM system_stage AS build_stage

ADD ./src/MagicPodsCore /app

WORKDIR /app

RUN cargo install earbuds

ENTRYPOINT [ "/backend/entrypoint.sh" ]