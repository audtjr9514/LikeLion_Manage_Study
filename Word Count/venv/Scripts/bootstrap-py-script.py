#!"D:\3. ������ ����ó��\2019�� 7�� ���\��� ����\Word Count\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bootstrap-py==0.7.0','console_scripts','bootstrap-py'
__requires__ = 'bootstrap-py==0.7.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bootstrap-py==0.7.0', 'console_scripts', 'bootstrap-py')()
    )
