import subprocess

# Example: Send ClearDTC request (service 0x14, no data)
result = subprocess.run([
    'python', '-m', 'cli.main', 'send', '14', ''
], capture_output=True, text=True)
print(result.stdout) 