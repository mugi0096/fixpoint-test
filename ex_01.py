import sys
import datetime

def check_errors(file_path):
    """
    ログファイルから一行ずつログをチェックし、故障期間を出力する。

    Parameters
    ----------
    file_path : string
        対象ファイルのパス
    
    """
    # 故障期間を計測するためのbool変数
    flg_error = False

    # エラー時の日時
    error_time = ""

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

            if res == "-":
                flg_error = True
                error_time = time
            
            if flg_error and res != "-":
                time_str = time.strftime("%y-%m-%d %H:%M:%S")
                error_time_str = error_time.strftime("%y-%m-%d %H:%M:%S")
                print(error_time_str + " ~ " + time_str)
                flg_error = False
            

if __name__ == "__main__":
    args = sys.argv
    check_errors(args[1])

