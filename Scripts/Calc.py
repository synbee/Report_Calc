import pandas as pd


def calc_avg_queue_time(csv_file):
    pd.options.display.max_rows = 9999

    sheet = pd.read_csv(csv_file)

    sub_dt = pd.to_datetime(sheet['Submit Date Time'],
                            format="%Y/%m/%d %H:%M:%S",
                            errors='coerce')
    strt_dt = pd.to_datetime(sheet['Start Date Time'],
                             format="%Y/%m/%d %H:%M:%S",
                             errors='coerce')

    sheet['Queue Time'] = (sub_dt - strt_dt).abs()

    sheet['Q_hr'] = sheet['Queue Time'].apply(
        lambda x: x.components.hours if pd.notnull(x) else 0
    )
    sheet['Q_min'] = sheet['Queue Time'].apply(
        lambda x: x.components.minutes if pd.notnull(x) else 0
    )
    sheet['Q_sec'] = sheet['Queue Time'].apply(
        lambda x: x.components.seconds if pd.notnull(x) else 0
    )

    diff = sheet[['Submit Date Time',
                  'Start Date Time',
                  'Q_hr',
                  'Q_min',
                  'Q_sec'
                  ]]

    avg_hr = sheet['Q_hr'].mean()
    avg_min = sheet['Q_min'].mean()
    avg_sec = sheet['Q_sec'].mean()

    avg_q = f"{int(avg_hr):02}:{int(avg_min):02}:{int(avg_sec):02}"

    print(diff)
    print(avg_q)

calc_avg_queue_time("CSVs/Job_rep_sample.csv")
