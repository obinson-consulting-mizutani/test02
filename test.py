#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡単なテストコード
基本的な計算機能をテストします
"""

def add(a, b):
    """二つの数を足し算する関数"""
    return a + b

def multiply(a, b):
    """二つの数を掛け算する関数"""
    return a * b

def is_even(n):
    """数が偶数かどうかを判定する関数"""
    return n % 2 == 0

def main():
    """メイン関数 - 簡単なテストを実行"""
    print("=== 簡単なテストコード実行 ===")
    
    # 足し算のテスト
    result1 = add(5, 3)
    print(f"5 + 3 = {result1}")
    assert result1 == 8, "足し算テスト失敗"
    
    # 掛け算のテスト
    result2 = multiply(4, 6)
    print(f"4 × 6 = {result2}")
    assert result2 == 24, "掛け算テスト失敗"
    
    # 偶数判定のテスト
    print(f"10は偶数？ {is_even(10)}")
    print(f"7は偶数？ {is_even(7)}")
    assert is_even(10) == True, "偶数判定テスト失敗"
    assert is_even(7) == False, "奇数判定テスト失敗"
    
    print("全てのテストが成功しました！✓")

if __name__ == "__main__":
    main()

