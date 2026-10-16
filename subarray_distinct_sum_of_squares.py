class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores:
        # sum of distinct counts
        # sum of squares of distinct counts
        # lazy increment
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, x):
            length = r - l + 1

            sum2[node] += 2 * x * sum1[node] + x * x * length
            sum1[node] += x * length
            lazy[node] += x

            sum1[node] %= MOD
            sum2[node] %= MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            x = lazy[node]

            apply(node * 2, l, mid, x)
            apply(node * 2 + 1, mid + 1, r, x)

            lazy[node] = 0

        def update(node, l, r, ql, qr, x):
            if ql <= l and r <= qr:
                apply(node, l, r, x)
                return

            push(node, l, r)

            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, x)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, x)

            sum1[node] = (sum1[node * 2] +
                          sum1[node * 2 + 1]) % MOD

            sum2[node] = (sum2[node * 2] +
                          sum2[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)

            # Every subarray ending at r whose
            # starting point is in [prev + 1, r]
            # gets one new distinct element.
            update(1, 0, n - 1, prev + 1, r, 1)

            # Sum of squares of all subarrays ending at r
            ans = (ans + sum2[1]) % MOD

            last[x] = r

        return ans