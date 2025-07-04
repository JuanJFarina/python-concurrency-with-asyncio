import sys
import subprocess
import time

NUM_WORKERS = 3
LOCUSTFILE = sys.argv[1] if len(sys.argv) > 1 else "locustfile.py"


def run_master():
    return subprocess.Popen(
        [
            "locust",
            "-f",
            LOCUSTFILE,
            "--master",
        ]
    )


def run_worker(worker_id):
    return subprocess.Popen(
        [
            "locust",
            "-f",
            LOCUSTFILE,
            "--worker",
            "--logfile",
            f"worker_{worker_id}.log",
        ]
    )


if __name__ == "__main__":
    print(f"Running locust master with {NUM_WORKERS} workers using {LOCUSTFILE}")
    master = run_master()
    time.sleep(2)
    workers = [run_worker(i) for i in range(NUM_WORKERS)]

    try:
        master.wait()
    except KeyboardInterrupt:
        print("Stopping all processes...")
        master.terminate()
        for w in workers:
            w.terminate()
