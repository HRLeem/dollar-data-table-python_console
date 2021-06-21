import execution.crawl as c

class Main_process:
    def __init__(self):
        self.power_unit()

    def power_unit(self):
        self.y_d_data()
        self.set_var()
        self.d_gap_rate()
        self.profit_rate()
        self.invest_suitability()
        self.print_side()

    def y_d_data(self):
        self.dw_list = c.main('dw')
        self.dxy_list = c.main('dxy')
        return

    def set_var(self):
        self.p_dw = self.dw_list[0]
        self.p_dxy = self.dxy_list[0]
        self.y_dw = self.dw_list[2]
        self.y_dxy = self.dxy_list[2]

    def d_gap_rate(self):
        # 달러갭비율 = 달러지수 / 원달러 * 100
        self.p_d_gap_rate = round(self.p_dxy / self.p_dw * 100, 2)
        self.y_d_gap_rate = round(self.y_dxy / self.y_dw * 100, 2)
        return

    def profit_rate(self):
        # 적정환율 = 현재 달러 지수 / 52주 평균 달러 갭 비율 * 100
        self.profit_rate = round(self.p_dxy / self.y_d_gap_rate * 100, 2)
        return

    def invest_suitability(self):
        #       52주             현재
        # 원달러           >
        # 달러지수          >
        # 달러갭           <
        # 적정환율          >
        if self.y_dw > self.p_dw:
            self.is_dw = 'ㅇ'
        else:
            self.is_dw = 'x'
        if self.y_dxy > self.p_dxy:
            self.is_dxy = 'ㅇ'
        else:
            self.is_dxy = 'x'
        if self.y_d_gap_rate < self.p_d_gap_rate:
            self.is_d_gap_rate = 'ㅇ'
        else:
            self.is_d_gap_rate = 'x'
        if self.profit_rate > self.p_dw:
            self.is_profit_rate = 'ㅇ'
        else:
            self.is_profit_rate = 'x'
        return

    def print_side(self):
        while True:
            print('-'*50)
            ip = input('간단하게 조회하기 = 1 | 숫자까지 표기하기 = 2 | 종료 = 0  : ')
            if ip == '0':
                break;
            elif ip == '1':
                print('투자 적합성')
                print(f'> 원달러 --- {self.is_dw}')
                print(f'> 달러 지수 --- {self.is_dxy}')
                print(f'> 달러 갭 비율 --- {self.is_d_gap_rate}')
                print(f'> 적정환율 비교 --- {self.is_profit_rate}')
            elif ip == '2':
                print('투자 적합성')
                print('-'*10, '52주 - 현재', '-'*10)
                print(f'o 원달러 --- {self.is_dw}  ( > )')
                print(f"> {format(self.y_dw, ',')} | {format(self.p_dw, ',')}")

                print(f'o 달러 지수 --- {self.is_dxy}  ( > )')
                print(f"> {format(self.y_dxy, ',')} | {format(self.p_dxy, ',')} ")

                print(f'o 달러 갭 비율 --- {self.is_d_gap_rate}  ( < )')
                print(f"> {format(self.y_d_gap_rate, ',')} | {format(self.p_d_gap_rate, ',')}")

                print('-'*10, '적정환율 - 현재 환율', '-'*10)
                print(f'o 적정환율 비교 --- {self.is_profit_rate}  ( > )')
                print(f"> {format(self.profit_rate, ',')} | {format(self.p_dw, ',')}")
                break
            else:
                print(f'\033[91m** 입력값을 확인하고 다시 입력해주세요.\n입력하신 값 >> {ip}\033[0m')
                continue