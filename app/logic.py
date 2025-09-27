# app/logic.py
import pandas as pd
import numpy as np

def generate_sample_csv(rows: int = 50) -> pd.DataFrame:
    """サンプルCSV用データフレームを生成"""
    np.random.seed(42)

    data = {
        "a": np.random.normal(15, 3, rows),
        "b": np.random.randint(4, 10, rows),
        "c": np.random.normal(5, 1, rows),
        "d": np.random.randint(18, 25, rows),
        "e": np.random.randint(45, 55, rows),
        "f": np.random.normal(100, 5, rows),
        "g": np.random.normal(200, 10, rows),
        "h": np.random.normal(300, 15, rows),
        "i": np.random.normal(400, 20, rows),
        "j": np.random.normal(500, 25, rows),
    }

    df = pd.DataFrame(data)

    # 外れ値挿入
    df.loc[9, "a"] = 100
    df.loc[20, "f"] = 200
    df.loc[35, "j"] = 1000

    return df
