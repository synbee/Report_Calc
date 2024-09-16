import pandas as pd
import math


def calc_avg_queue_time(file_path):
    sheet = pd.read_csv(file_path)

    sub_dt = pd.to_datetime(sheet["Submit Date Time"], errors="coerce")
    strt_dt = pd.to_datetime(sheet["Start Date Time"], errors="coerce")

    sheet["Queue Time"] = (sub_dt - strt_dt).abs()

    sheet.dropna(subset=["Queue Time"], inplace=True)

    total_seconds = sheet["Queue Time"].dt.total_seconds()

    avg_seconds = total_seconds.mean()

    avg_hr = int(avg_seconds // 3600)
    avg_min = int((avg_seconds % 3600) // 60)
    avg_sec = int(avg_seconds % 60)

    avg_q = f"{avg_hr:02}:{avg_min:02}:{avg_sec:02}"

    print(f"---Queue Time: {avg_q}")


def total_task_count(file_path):
    sheet = pd.read_csv(file_path)
    task_count = sheet["Task Count"][pd.notnull(sheet["Task Count"])].sum()
    print(f"---Total Tasks: {task_count:.0f}")


def total_frame_count(file_path):
    sheet = pd.read_csv(file_path)
    frame_count = sheet["Frame Count"][pd.notnull(sheet["Frame Count"])].sum()
    print(f"---Total Frames: {frame_count:.0f}")


def total_task_render_time(file_path):
    pd.options.display.max_rows = 9999
    sheet = pd.read_csv(file_path)

    sheet["Total Task Render Time"] = sheet["Total Task Render Time"].str.replace(
        r"(\d+):(\d+):(\d+):(\d+)", r"\1 days \2:\3:\4", regex=True
    )
    sheet["Total Task Render Time"] = pd.to_timedelta(
        sheet["Total Task Render Time"], errors="coerce"
    )

    total_render_time = sheet["Total Task Render Time"].sum()

    total_seconds = total_render_time.total_seconds()
    total_hours, remainder = divmod(total_seconds, 3600)
    total_minutes, total_seconds = divmod(remainder, 60)

    total_hours = int(total_hours)
    total_minutes = int(total_minutes)
    total_seconds = int(total_seconds)

    print(
        f"---Total Task Render Time: {total_hours:02}:{total_minutes:02}:{total_seconds:02}"
    )


def total_file_size(file_path):
    sheet = pd.read_csv(file_path)
    bytes = sheet["Total Output File Size (Bytes)"][
        pd.notnull(sheet["Total Output File Size (Bytes)"])
    ].sum()

    def convert_size(bytes):
        if bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB")
        i = int(math.floor(math.log(bytes, 1024)))
        power = math.pow(1024, i)
        size = round(bytes / power, 2)
        return f"---Total File Size: {size} {size_name[i]}"

    print(convert_size(bytes))

def total_jobs(file_path):
    sheet = pd.read_csv(file_path)
    x = len(sheet)
    formated_x = (x - 2)
    print(f"---Total Jobs {formated_x}")
