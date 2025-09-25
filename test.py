#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡単なWebアプリケーション
基本的な計算機能をWebで提供します
"""

import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

def add(a, b):
    """二つの数を足し算する関数"""
    return a + b

def multiply(a, b):
    """二つの数を掛け算する関数"""
    return a * b

def is_even(n):
    """数が偶数かどうかを判定する関数"""
    return n % 2 == 0

# HTMLテンプレート
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test02 - 計算機能テスト</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; margin-bottom: 30px; }
        .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background: #fafafa; }
        .section h3 { color: #555; margin-top: 0; }
        input[type="number"] { padding: 8px; margin: 5px; border: 1px solid #ccc; border-radius: 3px; width: 100px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; margin: 5px; }
        button:hover { background: #0056b3; }
        .result { margin: 10px 0; padding: 10px; background: #e7f3ff; border-left: 4px solid #007bff; font-weight: bold; }
        .footer { text-align: center; margin-top: 30px; color: #666; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 Test02 - 計算機能テスト</h1>
        
        <div class="section">
            <h3>➕ 足し算テスト</h3>
            <input type="number" id="add1" placeholder="数値1" value="5">
            <span>+</span>
            <input type="number" id="add2" placeholder="数値2" value="3">
            <button onclick="testAdd()">計算</button>
            <div id="addResult" class="result" style="display:none;"></div>
        </div>
        
        <div class="section">
            <h3>✖️ 掛け算テスト</h3>
            <input type="number" id="mult1" placeholder="数値1" value="4">
            <span>×</span>
            <input type="number" id="mult2" placeholder="数値2" value="6">
            <button onclick="testMultiply()">計算</button>
            <div id="multResult" class="result" style="display:none;"></div>
        </div>
        
        <div class="section">
            <h3>🔢 偶数判定テスト</h3>
            <input type="number" id="evenNum" placeholder="数値" value="10">
            <button onclick="testEven()">判定</button>
            <div id="evenResult" class="result" style="display:none;"></div>
        </div>
        
        <div class="section">
            <h3>🧪 全テスト実行</h3>
            <button onclick="runAllTests()" style="background: #28a745;">全テスト実行</button>
            <div id="allTestsResult" class="result" style="display:none;"></div>
        </div>
        
        <div class="footer">
            <p>Created by obinson-consulting-mizutani | Deployed on Railway</p>
        </div>
    </div>

    <script>
        async function testAdd() {
            const a = parseFloat(document.getElementById('add1').value);
            const b = parseFloat(document.getElementById('add2').value);
            const response = await fetch('/api/add', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({a, b})
            });
            const result = await response.json();
            document.getElementById('addResult').innerHTML = `結果: ${a} + ${b} = ${result.result}`;
            document.getElementById('addResult').style.display = 'block';
        }

        async function testMultiply() {
            const a = parseFloat(document.getElementById('mult1').value);
            const b = parseFloat(document.getElementById('mult2').value);
            const response = await fetch('/api/multiply', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({a, b})
            });
            const result = await response.json();
            document.getElementById('multResult').innerHTML = `結果: ${a} × ${b} = ${result.result}`;
            document.getElementById('multResult').style.display = 'block';
        }

        async function testEven() {
            const n = parseInt(document.getElementById('evenNum').value);
            const response = await fetch('/api/is_even', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({n})
            });
            const result = await response.json();
            const evenText = result.result ? '偶数です' : '奇数です';
            document.getElementById('evenResult').innerHTML = `結果: ${n} は ${evenText}`;
            document.getElementById('evenResult').style.display = 'block';
        }

        async function runAllTests() {
            const response = await fetch('/api/run_all_tests');
            const result = await response.json();
            document.getElementById('allTestsResult').innerHTML = result.message;
            document.getElementById('allTestsResult').style.display = 'block';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    """ホームページ"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/add', methods=['POST'])
def api_add():
    """足し算API"""
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify({'result': result})

@app.route('/api/multiply', methods=['POST'])
def api_multiply():
    """掛け算API"""
    data = request.get_json()
    result = multiply(data['a'], data['b'])
    return jsonify({'result': result})

@app.route('/api/is_even', methods=['POST'])
def api_is_even():
    """偶数判定API"""
    data = request.get_json()
    result = is_even(data['n'])
    return jsonify({'result': result})

@app.route('/api/run_all_tests')
def api_run_all_tests():
    """全テスト実行API"""
    try:
        # 足し算のテスト
        result1 = add(5, 3)
        assert result1 == 8, "足し算テスト失敗"
        
        # 掛け算のテスト
        result2 = multiply(4, 6)
        assert result2 == 24, "掛け算テスト失敗"
        
        # 偶数判定のテスト
        assert is_even(10) == True, "偶数判定テスト失敗"
        assert is_even(7) == False, "奇数判定テスト失敗"
        
        return jsonify({
            'success': True,
            'message': '✅ 全てのテストが成功しました！<br>• 5 + 3 = 8<br>• 4 × 6 = 24<br>• 10は偶数、7は奇数'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'❌ テストに失敗しました: {str(e)}'
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

