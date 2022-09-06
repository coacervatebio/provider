FROM alpine:latest

# Install java runtime
RUN apk add openjdk11-jre
VOLUME /golem/input /golem/output /golem/entrypoint

# Copy GATK assets
COPY gatk_release/gatk-package-4.2.6.1-local.jar /run/gatk-local.jar
COPY reference_HG38.tar.zst /run/reference_HG38.tar.zst

WORKDIR /golem/entrypoint