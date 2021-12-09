from datetime import date, timedelta, datetime
import calendar


class Calendar:
    def __init__(self):
        self.year = 2021
        self.date_list = []

    def set_year(self, year):
        self.year = year

    # generate dates in format '20210316' into a list
    def date_range(self, start, end):
        delta = end - start
        date_lis = []
        for i in range(delta.days+1):
            date_lis.append(str(start+timedelta(days=i)))
        # if not os.path.exists('./current_dl'):
        #     os.mkdir('./current_dl')
        # with open('./current_dl/dl_date.txt', 'w') as f:
        #     for _ in date_lis:
        #         f.write('{}\n'.format(_))
        date_lis = [_.replace('-', '') for _ in date_lis]
        return date_lis


    def input_dates(self):
        while not self.date_list:
            date_in = [x for x in input('please input a date range (format: month or month/date/date or month/date/month/date for cross-months): ').split('/')]
            if len(date_in) == 1:
                if int(date_in[0]) != 12:
                    self.date_list = self.date_range(date(int('{}'.format(self.year)),
                                                          int('{:>2}'.format(date_in[0])),
                                                          int('{:>2}'.format(1))),
                                                     date(int('{}'.format(self.year)),
                                                          int('{:>2}'.format(date_in[0]))+1,
                                                          int('{:>2}'.format(1))))
                    self.date_list = self.date_list[:-1]
                else:
                    self.date_list = self.date_range(date(int('{}'.format(self.year)),
                                                          int('{:>2}'.format(date_in[0])),
                                                          int('{:>2}'.format(1))),
                                                     date(int('{}'.format(self.year)),
                                                          int('{:>2}'.format(date_in[0])),
                                                          int('{:>2}'.format(31))))
            elif len(date_in) == 3:
                self.date_list = self.date_range(date(int('{}'.format(self.year)),
                                                      int('{:>2}'.format(date_in[0])),
                                                      int('{:>2}'.format(date_in[1]))),
                                                 date(int('{}'.format(self.year)),
                                                      int('{:>2}'.format(date_in[0])),
                                                      int('{:>2}'.format(date_in[2]))))
            elif len(date_in) == 4:
                self.date_list = self.date_range(date(int('{}'.format(self.year)),
                                                      int('{:>2}'.format(date_in[0])),
                                                      int('{:>2}'.format(date_in[1]))),
                                                 date(int('{}'.format(self.year)),
                                                      int('{:>2}'.format(date_in[2])),
                                                      int('{:>2}'.format(date_in[3]))))
            else:
                print("Invalid Form !")
        print(self.date_list)
        return self.date_list


if __name__ == "__main__":
    # now = datetime.now()
    # nowdate = now.date()
    # then = date(2021, 7, 15)
    # delta = nowdate - then
    # print(now, then, delta)
    # print(calendar.calendar(2021))
    Calendar().input_dates()