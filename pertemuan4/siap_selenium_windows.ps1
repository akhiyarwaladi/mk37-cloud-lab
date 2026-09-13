# Siapkan Selenium di Windows (Chrome desktop sudah cukup, lewati apt)
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install selenium requests boto3
(Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo.ProductVersion
