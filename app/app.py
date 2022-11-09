from monitoring.embassy_adapter import monitoring as embassy_monitoring
from monitoring.foreign_adapter import monitoring as foreign_monitoring


if __name__ == '__main__':
    embassy_monitoring()
    foreign_monitoring()
