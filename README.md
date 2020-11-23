# fixpoint-test

## 実行方法
### 設問1
```
python3 ex_01.py log.txt
```
### 設問2
```
python3 ex_02.py log.txt N
```
### 設問3
```
python3 ex_03.py log.txt N M T
```
### 設問4
未解答

## プログラム内容
ログファイルから一行ずつログをチェックし、故障期間を出力する。

    Parameters
    ----------
    file_path : string
        対象ファイルのパス

    N : str
        エラーと見なす時の連続タイムアウト数
    
    M : str
        平均応答時間を測るときのログ数
    
    T : str
        過負荷状態になる平均応答時間の閾値
