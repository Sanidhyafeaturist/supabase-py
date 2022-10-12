import subprocess
    
def run_cmd(cmd):
    subprocess.call(cmd, shell=True, check=True)

def run_tests():
    # Install requirements
    run_cmd("poetry install")
    
    # Run pre-commit tests
    run_cmd("poetry run pre-commit run --all-files")

    # Generate coverage report
    run_cmd("poetry run pytest --cov=./ --cov-report=xml --cov-report=html -vv")
