import subprocess

# Example: Send ReadDataByIdentifier request (service 0x22, DID 0xF190)
result = subprocess.run([
    'python', '-m', 'cli.main', 'send', '22', 'F190'
], capture_output=True, text=True)
print(result.stdout) 