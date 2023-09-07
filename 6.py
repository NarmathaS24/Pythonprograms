class FindPair:
    def __init__(self, arr: list, target: int):
        self.arr = arr
        self.target = target

    def find_pair_indices(self) -> tuple:
        pair_indices = ()
        value_to_index_map = {}

        for i, num in enumerate(self.arr):
            complement = self.target - num

            if complement in value_to_index_map:
                pair_indices = (value_to_index_map[complement], i)
                break

            value_to_index_map[num] = i

        return pair_indices
find_pair = FindPair([100, 20, 30, 40, 50, 60], 150)
pair_indices = find_pair.find_pair_indices()
if pair_indices:
    print(f"Indices of pair whose sum equals {find_pair.target}: {pair_indices}")
else:
    print(f"No pair found in array {find_pair.arr} whose sum equals {find_pair.target}")
