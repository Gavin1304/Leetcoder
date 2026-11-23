# Leetcoder

用 Python 练习 LeetCode。解法保留平台的 `Solution` 接口，可以直接复制到对应题目的编辑器。

| 题目 | 解法 | 思路与复杂度 |
| --- | --- | --- |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | [p0001_two_sum.py](solutions/p0001_two_sum.py) | 哈希表记录已访问的下标。时间 O(n)，空间 O(n)。 |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [p0020_valid_parentheses.py](solutions/p0020_valid_parentheses.py) | 栈匹配括号。时间 O(n)，空间 O(n)。 |

## 本地校验

需要 Python 3.12，无第三方依赖。在仓库根目录运行：

```sh
python -m unittest discover -s tests -v
```

## 添加新题

在 `solutions/` 添加 `p<四位题号>_<题名>.py`，在 `tests/` 添加对应的 `test_*.py`，并更新上方索引。测试直接调用 `Solution` 方法，覆盖典型输入和边界输入。GitHub Actions 在推送和拉取请求时运行同一条命令。
