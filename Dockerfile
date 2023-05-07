FROM alpine:latest

# Install java runtime
RUN apk add openjdk11-jre tar zstd
VOLUME /golem/input /golem/output /golem/entrypoint

# Install GATK
ARG GATK_VER=4.4.0.0
RUN wget https://github.com/broadinstitute/gatk/releases/download/${GATK_VER}/gatk-${GATK_VER}.zip && \
 unzip gatk-${GATK_VER}.zip && \
 mv gatk-${GATK_VER}/gatk-package-${GATK_VER}-local.jar /run/gatk-local.jar && \
 rm -rf gatk-${GATK_VER}*

# Add reference
COPY reference_HG38.tar.zst /run/reference_HG38.tar.zst

# Add run script
COPY run.sh /run/run.sh