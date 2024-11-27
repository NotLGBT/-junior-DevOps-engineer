from flask import Flask, jsonify, render_template, request
import psutil
import re

def stat_extract(method_stat, pattern, interval=20):
    try:
        match method_stat:
            case "IO":
                for proc in psutil.process_iter(attrs=["pid", "name", "io_counters"]):
                    if re.search(pattern, proc.info["name"], re.IGNORECASE):
                        io_counters = proc.info["io_counters"]
                        if io_counters:
                            return {
                                "pid": proc.info["pid"],
                                "name": proc.info["name"],
                                "read_bytes": io_counters.read_bytes,
                                "write_bytes": io_counters.write_bytes,
                            }
            case "Memory":
                for proc in psutil.process_iter(attrs=["pid", "name", "memory_info", "memory_percent"]):
                    if re.search(pattern, proc.info["name"], re.IGNORECASE):
                        memory_info = proc.info["memory_info"]
                        memory_percent = proc.info["memory_percent"]
                        if memory_info and memory_percent:
                            return {
                                "pid": proc.info["pid"],
                                "name": proc.info["name"],
                                "rss_mb": memory_info.rss / (1024 ** 2),
                                "memory_percent": memory_percent,
                            }
            case "CPU":
                for proc in psutil.process_iter(attrs=["pid", "name", "cpu_num", "cpu_percent"]):
                    if re.search(pattern, proc.info["name"], re.IGNORECASE):
                        cpu_num = proc.info["cpu_num"]
                        cpu_percent = proc.info["cpu_percent"]
                        if cpu_num is not None and cpu_percent is not None:
                            return {
                                "pid": proc.info["pid"],
                                "name": proc.info["name"],
                                "cpu_num": cpu_num,
                                "cpu_percent": cpu_percent,
                            }
            case _:
                raise ValueError("Invalid method_stat. Specify 'IO', 'Memory', or 'CPU'.")
    except (psutil.NoSuchProcess, psutil.AccessDenied) as error:
        return {"error": f"Access issue's: {str(error)}"}
    except Exception as error:
        return {"error": f"Unexpected error: {str(error)}"}

    return {"error": "No matching processes has found."}