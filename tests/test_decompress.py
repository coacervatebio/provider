from pathlib import PurePath
from tests.common import ContainerTester
from tests.runners import DecompressRunner
from tests.checkers import SimpleChecker


def test_decompress():

    data_path = PurePath("assets/decompress/")

    tester = ContainerTester(DecompressRunner(), SimpleChecker(), data_path)
    tester.runner.vols = [f"{str(tester.tmpdir.resolve())}:/golem/entrypoint"]

    tester.run()
    