# Test for compiling code (11) using nuitka
python3 -m nuitka --follow-imports parts.py
./parts.bin

# Timing: Both around 10s
