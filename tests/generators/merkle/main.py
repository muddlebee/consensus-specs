from eth2spec.test.helpers.constants import ALTAIR, MERGE
from eth2spec.gen_helpers.gen_from_tests.gen import run_state_test_generators


if __name__ == "__main__":
    altair_mods = {key: 'eth2spec.test.altair.merkle.test_' + key for key in [
        'single_proof',
    ]}
    merge_mods = altair_mods

    all_mods = {
        ALTAIR: altair_mods,
        MERGE: merge_mods,
    }

    run_state_test_generators(runner_name="merkle", all_mods=all_mods)
