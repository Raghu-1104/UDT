import subprocess

# Example: Send ECUReset request (service 0x11, reset type 0x01)
result = subprocess.run([
    'python', '-m', 'cli.main', 'send', '11', '01'
], capture_output=True, text=True)
print(result.stdout) 