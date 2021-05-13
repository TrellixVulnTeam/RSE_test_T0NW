import numpy as np

np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
data = np.load(open("musicnet_11khz.npz", "rb"), encoding="latin1")
np.load = np_load_old


test_IDs = ["2303", "2382", "1819"]
validation_IDs = ["2131", "2384", "1792", "2514", "2567", "1876"]
train_IDs = [ID for ID in data.files if ID not in (test_IDs + validation_IDs)]

print(f"length of train ID: {len(train_IDs)}")


for i in range(len(train_IDs)):
    x, y = data[train_IDs[i]]
    print(f"length of {i+1} data: {len(x)}, {len(y)}")