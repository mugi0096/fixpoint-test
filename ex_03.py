import sys
import datetime
from statistics import mean

def check_errors(file_path, N, M, T):
    """
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
    """
    # 故障期間を計測するためのbool変数
    flg_error = False

    # エラー時の日時
    error_time = datetime.datetime(1, 1, 1)

    # 何回連続でタイムアウトしたかをカウントする変数
    cnt = 0

    # 受け取ったパラメータをintに処理
    N, M, T = map(int, [N, M, T])

    # M個の応答時間を確保するリスト
    logs_list = []

    # M個の確認日時を確保するリスト
    times_list = []

    with open(file_path) as f:
        for log in f:
            # ログを確認日時、サーバアドレス、応答結果に分割
            time, address, res = log.split(',')
            time = datetime.datetime(int(time[:4]),     #　年
                                     int(time[4:6]),    #　月
                                     int(time[6:8]),    #　日
                                     int(time[8:10]),   #　時
                                     int(time[10:12]),  #　分
                                     int(time[12:14]))  #　秒
            

            # 改行文字の除去
            res = res[:-1]
            
            # タイムアウトのチェック
            if  not flg_error and res == "-":
                flg_error = True
                error_time = time
                cnt += 1
            
            elif res == "-":
                cnt += 1
            
            elif flg_error and res != "-" and cnt >= N:
                time_str = time.strftime("%y-%m-%d %H:%M:%S")
                error_time_str = error_time.strftime("%y-%m-%d %H:%M:%S")
                print("Error Terms")
                print(error_time_str + " ~ " + time_str)
                flg_error = False
            
            else:
                cnt = 0
                flg_error = False

            # 過負荷状態のチェック
            if res != "-":
                logs_list.append(int(res))
                times_list.append(time)

            else:
                logs_list.append(0)
                times_list.append(time)
            
            if len(logs_list) >= M:
                if mean(logs_list) > T:
                    highpress_start_str = times_list[0].strftime("%y-%m-%d %H:%M:%S")
                    highpress_end_str = times_list[-1].strftime("%y-%m-%d %H:%M:%S")
                    print("Too Much Pressures")
                    print(highpress_start_str + " ~ " + highpress_end_str)
                
                logs_list.pop(0)
                times_list.pop(0)
            

if __name__ == "__main__":
    args = sys.argv
    check_errors(args[1], args[2], args[3], args[4])

