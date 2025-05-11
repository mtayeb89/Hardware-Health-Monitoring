# Hardware-Health-Monitoring
a Python script for a Hardware Health Check that monitors key hardware components like CPU temperature, disk health, and fan speed. 
# Hardware Health Monitor
# مراقب صحة الأجهزة

[English](#english) | [العربية](#arabic).

<a name="english"></a>
## English

### Description
Hardware Health Monitor is a Python-based system monitoring tool that provides real-time information about your computer's hardware components. It monitors CPU, memory, disk usage, and fan speeds, providing detailed health reports and alerts.

### Features
- Real-time CPU monitoring (usage and temperature)
- Memory usage tracking
- Disk health status and usage statistics
- Fan speed monitoring (on supported systems)
- Cross-platform support (Linux, Windows, MacOS)
- Detailed logging system
- Error handling and recovery

### Requirements
- Python 3.7 or higher
- psutil library
- smartmontools (for disk health monitoring)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/hardware-monitor.git
cd hardware-monitor
```

2. Install required Python packages:
```bash
pip install psutil
```

3. Install smartmontools (for disk health monitoring):
```bash
# Ubuntu/Debian
sudo apt-get install smartmontools

# CentOS/RHEL
sudo yum install smartmontools

# MacOS
brew install smartmontools

# Windows
# Download and install smartmontools from the official website
```

### Usage
Run the script with Python:
```bash
python hardware_monitor.py
```

To run with elevated privileges (for full functionality):
```bash
sudo python hardware_monitor.py
```

### Configuration
The monitoring interval can be adjusted by modifying the `interval` variable in the main function. Default is 60 seconds.

### Output Example
```
CPU Health:
 - CPU Usage (%): 25.3
 - CPU Temperature (°C): 45.6
 - CPU Count: 8
 - CPU Frequency (MHz): 2400

Memory Health:
 - Memory Usage (%): 65.4
 - Total Memory (GB): 16.0
 - Available Memory (GB): 5.5
 - Swap Usage (%): 10.2
 - Swap Total (GB): 8.0
```

---

<a name="arabic"></a>
## العربية

### الوصف
مراقب صحة الأجهزة هو أداة مراقبة نظام تعتمد على Python وتوفر معلومات في الوقت الفعلي حول مكونات جهاز الكمبيوتر. يراقب وحدة المعالجة المركزية والذاكرة واستخدام القرص وسرعات المروحة، ويقدم تقارير صحية وتنبيهات مفصلة.

### المميزات
- مراقبة المعالج في الوقت الفعلي (الاستخدام ودرجة الحرارة)
- تتبع استخدام الذاكرة
- حالة صحة القرص وإحصاءات الاستخدام
- مراقبة سرعة المروحة (على الأنظمة المدعومة)
- دعم متعدد المنصات (Linux، Windows، MacOS)
- نظام تسجيل مفصل
- معالجة الأخطاء والتعافي منها

### المتطلبات
- Python 3.7 أو أحدث
- مكتبة psutil
- smartmontools (لمراقبة صحة القرص)

### التثبيت
1. استنساخ المستودع:
```bash
git clone https://github.com/yourusername/hardware-monitor.git
cd hardware-monitor
```

2. تثبيت حزم Python المطلوبة:
```bash
pip install psutil
```

3. تثبيت smartmontools (لمراقبة صحة القرص):
```bash
# Ubuntu/Debian
sudo apt-get install smartmontools

# CentOS/RHEL
sudo yum install smartmontools

# MacOS
brew install smartmontools

# Windows
# قم بتحميل وتثبيت smartmontools من الموقع الرسمي
```

### الاستخدام
قم بتشغيل السكريبت باستخدام Python:
```bash
python hardware_monitor.py
```

للتشغيل بصلاحيات مرتفعة (للوظائف الكاملة):
```bash
sudo python hardware_monitor.py
```

### الإعدادات
يمكن تعديل فترة المراقبة عن طريق تغيير متغير `interval` في الدالة الرئيسية. القيمة الافتراضية هي 60 ثانية.

### مثال على المخرجات
```
صحة المعالج:
 - استخدام المعالج (%): 25.3
 - درجة حرارة المعالج (°C): 45.6
 - عدد المعالجات: 8
 - تردد المعالج (MHz): 2400

صحة الذاكرة:
 - استخدام الذاكرة (%): 65.4
 - إجمالي الذاكرة (GB): 16.0
 - الذاكرة المتاحة (GB): 5.5
 - استخدام الذاكرة الافتراضية (%): 10.2
 - إجمالي الذاكرة الافتراضية (GB): 8.0
```

### المساهمة
نرحب بالمساهمات! يرجى إرسال pull request أو فتح issue لأي اقتراحات أو تحسينات.

### الترخيص
هذا المشروع مرخص تحت رخصة MIT. راجع ملف `LICENSE` للمزيد من المعلومات.
