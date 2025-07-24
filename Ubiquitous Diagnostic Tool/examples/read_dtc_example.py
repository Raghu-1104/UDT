import subprocess

# Example: Send ReadDTC request (service 0x19, subfunction 0x01)
result = subprocess.run([
    'python', '-m', 'cli.main', 'send', '19', '01'
], capture_output=True, text=True)
print(result.stdout) 