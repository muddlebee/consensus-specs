from eth2spec.test.helpers.constants import PHASE0, ALTAIR, MERGE
from eth2spec.gen_helpers.gen_from_tests.gen import run_state_test_generators, combine_mods


if __name__ == "__main__":
    phase_0_mods = {key: 'eth2spec.test.phase0.sanity.test_' + key for key in [
        'blocks',
        'slots',
    ]}

    _new_altair_mods = {key: 'eth2spec.test.altair.sanity.test_' + key for key in [
        'blocks',
    ]}
    altair_mods = combine_mods(_new_altair_mods, phase_0_mods)

    _new_merge_mods = {key: 'eth2spec.test.merge.sanity.test_' + key for key in [
        'blocks',
    ]}
    merge_mods = combine_mods(_new_merge_mods, altair_mods)

    all_mods = {
        PHASE0: phase_0_mods,
        ALTAIR: altair_mods,
        MERGE: merge_mods,
    }

    run_state_test_generators(runner_name="sanity", all_mods=all_mods)
