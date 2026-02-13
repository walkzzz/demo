import subprocess
import os
import sys
import shutil


def clean_allure_results():
    results_dir = 'allure-results'
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
        print(f'Cleaned {results_dir} directory')


def run_tests(marker=None):
    cmd = ['pytest', '-v', '--alluredir=./allure-results', '--clean-alluredir']
    
    if marker:
        cmd.extend(['-m', marker])
    
    print(f'Running tests with command: {" ".join(cmd)}')
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def generate_report():
    cmd = ['allure', 'generate', './allure-results', '-o', './allure-report', '--clean']
    print(f'Generating report with command: {" ".join(cmd)}')
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def serve_report():
    cmd = ['allure', 'serve', './allure-results']
    print(f'Serving report with command: {" ".join(cmd)}')
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def main():
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python run_tests.py test [marker]  - Run tests (optional marker filter)')
        print('  python run_tests.py report         - Generate HTML report')
        print('  python run_tests.py serve          - Serve report (opens in browser)')
        print('  python run_tests.py all            - Run tests and serve report')
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'test':
        marker = sys.argv[2] if len(sys.argv) > 2 else None
        exit_code = run_tests(marker)
        sys.exit(exit_code)
    
    elif command == 'report':
        exit_code = generate_report()
        sys.exit(exit_code)
    
    elif command == 'serve':
        exit_code = serve_report()
        sys.exit(exit_code)
    
    elif command == 'all':
        exit_code = run_tests()
        if exit_code == 0:
            print('\nTests passed! Serving report...')
            serve_report()
        sys.exit(exit_code)
    
    else:
        print(f'Unknown command: {command}')
        print('Available commands: test, report, serve, all')
        sys.exit(1)


if __name__ == '__main__':
    main()
