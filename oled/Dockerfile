# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Install package dependencies for add-on
RUN \
  apk add --no-cache \
    git \
    build-base \
    linux-headers \
    python3 \
    python3-dev \
    py3-pip \
    py3-pillow \
    libjpeg-turbo-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev

# Install PIP dependencies
RUN \
  pip3 install \
  wheel \
  paho-mqtt \
  luma.oled

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy root filesystem
COPY rootfs /
