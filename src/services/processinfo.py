from terminaltables import AsciiTable
import psutil

def processInfo():
    table_data = [
        ["PID", "Process", "User"],
    ]
    for proc in psutil.process_iter(attrs=["pid", "name", "username"]):
        table_data.append([
            proc.info["pid"],
            proc.info["name"],
            proc.info["username"] or "-"
        ])
    table = AsciiTable(table_data)
    # print(table.table)
    return table.table



processInfo()