import pandas as pd


def calc_avg_queue_time(file_path, rows):
    pd.options.display.max_rows = rows

    sheet = pd.read_csv(file_path)

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
    print(f"---Queue time: {avg_q}")


def total_task_count(file_path, rows):
    pd.options.display.max_rows = rows
    sheet = pd.read_csv(file_path)
    task_count = sum(sheet['Task Count'])
    print(f"---Total Tasks: {task_count}")
