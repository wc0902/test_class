"""
practice1.py - Python 基礎練習：資料結構 + 函式 + 類別 + 錯誤處理
"""

# ── 1. 資料結構操作 ─────────────────────────────────────────────
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob",   "score": 78},
    {"name": "Carol", "score": 85},
    {"name": "Dave",  "score": 61},
    {"name": "Eve",   "score": 99},
]

# 用 sorted + lambda 依分數由高到低排列
ranked = sorted(students, key=lambda s: s["score"], reverse=True)

print("=== 成績排名 ===")
for i, s in enumerate(ranked, start=1):
    print(f"  {i}. {s['name']:<8} {s['score']} 分")


# ── 2. 函式：計算統計資料 ────────────────────────────────────────
def calc_stats(data: list[dict]) -> dict:
    """計算平均、最高、最低分"""
    scores = [s["score"] for s in data]
    return {
        "avg":  sum(scores) / len(scores),
        "max":  max(scores),
        "min":  min(scores),
        "pass": sum(1 for s in scores if s >= 60),  # 60 分以上算通過
    }

stats = calc_stats(students)
print(f"\n=== 統計 ===")
print(f"  平均分：{stats['avg']:.1f}")
print(f"  最高分：{stats['max']}")
print(f"  最低分：{stats['min']}")
print(f"  通過人數：{stats['pass']} / {len(students)}")


# ── 3. 類別：學生管理系統 ────────────────────────────────────────
class StudentManager:
    """簡易學生管理器"""

    GRADE_MAP = {
        "A": range(90, 101),
        "B": range(80, 90),
        "C": range(70, 80),
        "D": range(60, 70),
        "F": range(0,  60),
    }

    def __init__(self, students: list[dict]):
        # 建立一份副本，避免修改原始資料
        self._data = [s.copy() for s in students]
        self._assign_grades()

    def _assign_grades(self):
        for s in self._data:
            s["grade"] = self._score_to_grade(s["score"])

    def _score_to_grade(self, score: int) -> str:
        for grade, r in self.GRADE_MAP.items():
            if score in r:
                return grade
        return "?"

    def top_n(self, n: int = 3) -> list[dict]:
        """回傳前 n 名學生"""
        return sorted(self._data, key=lambda s: s["score"], reverse=True)[:n]

    def add_student(self, name: str, score: int):
        """新增一位學生，分數需介於 0–100"""
        if not (0 <= score <= 100):
            raise ValueError(f"分數 {score} 超出範圍（0–100）")
        entry = {"name": name, "score": score}
        entry["grade"] = self._score_to_grade(score)
        self._data.append(entry)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"StudentManager({len(self)} 位學生)"


manager = StudentManager(students)
print(f"\n=== 類別示範：{manager} ===")
print("前 3 名：")
for s in manager.top_n(3):
    print(f"  {s['name']:<8} {s['score']} 分  ({s['grade']})")


# ── 4. 錯誤處理 ─────────────────────────────────────────────────
print("\n=== 錯誤處理示範 ===")

test_cases = [
    ("Frank", 88),
    ("Grace", 150),   # 無效分數
    ("Heidi", -5),    # 無效分數
]

for name, score in test_cases:
    try:
        manager.add_student(name, score)
        print(f"  已新增：{name}（{score} 分）")
    except ValueError as e:
        print(f"  [錯誤] {e}")

print(f"\n最終學生數：{len(manager)} 人")


# ── 5. 生成器：費氏數列 ──────────────────────────────────────────
def fibonacci(limit: int):
    """產生不超過 limit 的費氏數列"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

fib_list = list(fibonacci(200))
print(f"\n=== 費氏數列（≤ 200）===")
print(f"  {fib_list}")
