from subprocess import Popen, PIPE


def run_script(script_name, args=[]):
    p = Popen(["python3", script_name] + args, stdout=PIPE)
    stdout, _ = p.communicate()
    print("Called")
    return p.returncode, stdout.decode()


def test_example_script_runs():
    """Check that this repo's example script runs without error."""
    return_code, output = run_script("example.py")
    assert return_code == 0
    assert output.count("Enigma machine rotors: I II III in positions") != 0
