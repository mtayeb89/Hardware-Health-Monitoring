import psutil
import platform
import subprocess
import time
from typing import Dict, List, Union, Optional
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class HardwareMonitor:
    def __init__(self):
        self.system = platform.system()
        self.temp_paths = {
            "Linux": [
                "/sys/class/thermal/thermal_zone0/temp",
                "/sys/class/hwmon/hwmon0/temp1_input"
            ],
            "Windows": None,  # Windows requires additional libraries like OpenHardwareMonitor
            "Darwin": None  # macOS requires additional privileges
        }
        self.fan_paths = {
            "Linux": [
                "/sys/class/hwmon/hwmon0/fan1_input",
                "/sys/class/hwmon/hwmon1/fan1_input"
            ]
        }

    def _read_sensor_file(self, filepath: str) -> Optional[str]:
        """Safely read sensor files with error handling."""
        try:
            return Path(filepath).read_text().strip()
        except (FileNotFoundError, PermissionError, IOError) as e:
            logger.debug(f"Could not read sensor file {filepath}: {e}")
            return None

    def check_cpu_health(self) -> Dict[str, Union[float, str]]:
        """Check CPU temperature and usage with improved error handling."""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_temp = None

            if self.system in self.temp_paths and self.temp_paths[self.system]:
                for temp_path in self.temp_paths[self.system]:
                    temp_str = self._read_sensor_file(temp_path)
                    if temp_str:
                        try:
                            cpu_temp = float(temp_str) / 1000  # Convert from millidegrees
                            break
                        except ValueError:
                            continue

            return {
                "CPU Usage (%)": cpu_usage,
                "CPU Temperature (°C)": cpu_temp if cpu_temp is not None else "Not Available",
                "CPU Count": psutil.cpu_count(logical=True),
                "CPU Frequency (MHz)": psutil.cpu_freq().current if hasattr(psutil.cpu_freq(),
                                                                            'current') else "Not Available"
            }
        except Exception as e:
            logger.error(f"Error checking CPU health: {e}")
            return {"Error": str(e)}

    def check_memory_health(self) -> Dict[str, Union[float, str]]:
        """Check memory usage with enhanced metrics."""
        try:
            memory_info = psutil.virtual_memory()
            swap_info = psutil.swap_memory()

            return {
                "Memory Usage (%)": memory_info.percent,
                "Total Memory (GB)": round(memory_info.total / (1024 ** 3), 2),
                "Available Memory (GB)": round(memory_info.available / (1024 ** 3), 2),
                "Swap Usage (%)": swap_info.percent,
                "Swap Total (GB)": round(swap_info.total / (1024 ** 3), 2)
            }
        except Exception as e:
            logger.error(f"Error checking memory health: {e}")
            return {"Error": str(e)}

    def check_disk_health(self) -> List[Dict[str, str]]:
        """Check disk health with improved device detection and error handling."""
        disk_health = []
        try:
            partitions = psutil.disk_partitions()
            for partition in partitions:
                # Skip CD-ROM drives and network filesystems
                if "cdrom" in partition.opts or partition.fstype in ("nfs", "smbfs", "remote"):
                    continue

                device = partition.device
                usage = psutil.disk_usage(partition.mountpoint)

                health_info = {
                    "Disk": device,
                    "Mount Point": partition.mountpoint,
                    "File System": partition.fstype,
                    "Usage (%)": usage.percent,
                    "Health": "Unknown"
                }

                # Try SMART status on Linux/macOS if root
                if self.system in ("Linux", "Darwin") and "sd" in device or "nvme" in device:
                    try:
                        result = subprocess.run(
                            ["smartctl", "--health", device],
                            capture_output=True,
                            text=True,
                            timeout=5
                        )
                        health_info["Health"] = "PASS" if "PASSED" in result.stdout else "FAIL"
                    except (subprocess.SubprocessError, FileNotFoundError):
                        health_info["Health"] = "SMART check unavailable"

                disk_health.append(health_info)

        except Exception as e:
            logger.error(f"Error checking disk health: {e}")
            disk_health.append({"Error": str(e)})

        return disk_health

    def check_fan_speed(self) -> Dict[str, Union[int, str]]:
        """Check fan speed with multiple sensor path support."""
        if self.system not in self.fan_paths:
            return {"Fan Speed (RPM)": "Not supported on this platform"}

        for fan_path in self.fan_paths[self.system]:
            fan_speed = self._read_sensor_file(fan_path)
            if fan_speed:
                try:
                    return {"Fan Speed (RPM)": int(fan_speed)}
                except ValueError:
                    continue

        return {"Fan Speed (RPM)": "No fan sensor found"}

    def run_health_check(self) -> Dict[str, Dict]:
        """Run a complete hardware health check."""
        logger.info("Starting hardware health check...")

        health_report = {
            "CPU Health": self.check_cpu_health(),
            "Memory Health": self.check_memory_health(),
            "Disk Health": self.check_disk_health(),
            "Fan Health": self.check_fan_speed()
        }

        # Print health check results
        for component, status in health_report.items():
            print(f"\n{component}:")
            if isinstance(status, dict):
                for key, value in status.items():
                    print(f" - {key}: {value}")
            elif isinstance(status, list):
                for item in status:
                    for key, value in item.items():
                        print(f" - {key}: {value}")

        return health_report


def main():
    """Main function to run the hardware monitor."""
    monitor = HardwareMonitor()
    interval = 60  # seconds

    try:
        while True:
            monitor.run_health_check()
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()