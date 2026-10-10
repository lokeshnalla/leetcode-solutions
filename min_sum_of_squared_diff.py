from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                          k1: int, k2: int) -> int:

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        freq = Counter(diff)

        max_diff = max(freq)

        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            if d not in freq:
                continue

            moves = min(freq[d], k)

            freq[d] -= moves
            freq[d - 1] += moves

            k -= moves

        ans = 0

        for d, count in freq.items():
            ans += d * d * count

        return ans