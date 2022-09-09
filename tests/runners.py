import os
import docker
from tests.config import test_tag, test_name

client = docker.from_env()
cons = client.containers

class DecompressRunner:

    def __init__(self):
        self.vols = []

    def run(self):
        logs = cons.run(
            test_tag,
            command=[
                "tar",
                "xf",
                "/run/reference_HG38.tar.zst",
                "-C",
                "/golem/entrypoint"
            ],
            name=test_name,
            volumes=self.vols
            ).decode('utf-8')

class ScriptRunner:

    def __init__(self):
        self.vols = []

    def run(self):
        logs = cons.run(
            test_tag,
            command=[
                "/bin/sh",
                "/golem/entrypoint/run.sh",
                "/golem/input/HG03633_chr21.cram",
                "chr21",
                "/golem/output/HG03633_chr21.g.vcf.gz"
            ],
            name=test_name,
            volumes=self.vols
            ).decode('utf-8')

# class HaplotypeCallerRunner:

#     def __init__(self):
#         self.vols = []

#     def run(self):
#         logs = cons.run(
#             test_tag,
#             command=[
#                 "java",
#                 "-jar",
#                 "/run/gatk-local.jar",
#                 "HaplotypeCaller",
#                 "-I",
#                 "$ALIGN_IN",
#                 "-O",
#                 "$VCF_OUT",
#                 "-R",
#                 "/golem/entrypoint/reference/resources_broad_hg38_v0_Homo_sapiens_assembly38.fasta",
#                 "-L",
#                 "$REG",
#                 "-ERC",
#                 "GVCF"
#             ],
#             name=test_name,
#             volumes=self.vols
#             ).decode('utf-8')
