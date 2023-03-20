# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

SHELL ["/bin/ash", "-o", "pipefail", "-c"]

# Get Tempio
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
        "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

RUN \
    set -x \
    && apk add --no-cache \
        git \
        build-base \
        pkgconfig \
        alsa-lib-dev

ARG MIDIMONSTER_VERSION
RUN \
    git clone -b v${MIDIMONSTER_VERSION} --depth 1 \
        https://github.com/cbdevnet/midimonster /usr/src/midimonster \
    && cd /usr/src/midimonster/backends \
    && make libmmbackend.o \
    && make mqtt.so \
    && make midi.so \
    && cd .. \
    && make midimonster \
    && make install

# Copy root filesystem
COPY rootfs /