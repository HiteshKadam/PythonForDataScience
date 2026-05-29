import uproot
import pandas as pd

file = uproot.open("mupar20130402.root")

print(file.values())


print(file.items())

tree = file["mupar"]

print(tree.keys())


arrays = tree.arrays(tree.keys(), library="np")

print(arrays)