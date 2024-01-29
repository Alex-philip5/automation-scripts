# Automation-scripts
This repo contains the scripts with automation of linux servers

## Hit the Star! ⭐
If you are planning to use this Automation script. Thanks!

## Setup

1. Prerequisites

    ```bash
    $ sudo apt-get install python3-pip
    $ pip install psutil
    ```

1. Test High CPU Load & kill the process using python script

    ```bash
    $ cd python-automation/high_cpu_load
    $ bash load.sh &
    $ python3 kill_process.py
    ```
2. Setup CronJob for logrotate
   ```bash
#logrotate for python process for high cpuload ps
0 0 */15 * * /bin/bash /root/python-script/log-rotate.sh
   ```

## License

This project is licensed under the [MIT License](LICENSE). You can find the full text of the license in the [LICENSE](LICENSE) file.
