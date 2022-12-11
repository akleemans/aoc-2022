# Python: 2.2s
python3 run.py

# Nuitka: 1.3s
python3 -m nuitka run.py && ./run.bin

# Codon: 0.35s
# After removing 'typing' import and Removing '' around Monkey
codon run -release run.py
