from utils import get_system_metrics, log_metrics, check_alert

def main():
    metrics = get_system_metrics()
    print(metrics)
    log_metrics(metrics)
    check_alert(metrics)

if __name__ == "__main__":
    main()

