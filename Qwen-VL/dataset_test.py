
from datasets import DatasetDict
local_dataset = DatasetDict.load_from_disk("./datasets")
print(local_dataset)