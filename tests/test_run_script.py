from pathlib import PurePath
from tests.common import ContainerTester
from tests.runners import ScriptRunner
from tests.checkers import VcfChecker


def test_run_script():

    data_path = PurePath("assets/run_script/")

    tester = ContainerTester(ScriptRunner(), VcfChecker(), data_path)
    tester.runner.vols = [
        f"{str(tester.tmpdir.joinpath('golem', 'input').resolve())}:/golem/input",
        f"{str(tester.tmpdir.joinpath('golem', 'output').resolve())}:/golem/output"]
    tester.track_unexpected = False

    tester.run()