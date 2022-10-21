import subprocess
import requests
from shutil import copy, Error
import os
from zipfile import ZipFile, BadZipFile
from pathlib import Path
from requests.exceptions import RequestException

WEB_DRIVER_PATH = 'C:/bin'
DOWNLOADS_FOLDER = os.path.join(Path.home(), 'Downloads')

EDGE_BROWSER_VERSION = ''
EDGE_DRIVER_VERSION = ''

def isEdgeWebDriverUpdated():
  EDGE_BROWSER_VERSION = subprocess.run(["powershell.exe", "(Get-AppxPackage -Name 'Microsoft.MicrosoftEdge.Stable').Version"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
  EDGE_DRIVER_VERSION = subprocess.run([os.path.join(WEB_DRIVER_PATH, "msedgedriver.exe"), "-version"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
  return EDGE_BROWSER_VERSION in EDGE_DRIVER_VERSION

def updateEdgeWebDriver(version: str):
  updateUrl = f'https://msedgedriver.azureedge.net/{version}/edgedriver_win64.zip'
  downloadFile = 'driver_update.zip'
  try:
    # download zip file to downloads folder
    res = requests.get(updateUrl, allow_redirects=True)
    open(os.path.join(DOWNLOADS_FOLDER, downloadFile), 'wb').write(res.content)
    
    # unzip file into web driver folder
    ZipFile(os.path.join(DOWNLOADS_FOLDER, downloadFile), 'r').extract('msedgedriver.exe', WEB_DRIVER_PATH)
    
    # copy and rename downloaded file
    copy(os.path.join(WEB_DRIVER_PATH, 'msedgedriver.exe'), os.path.join(WEB_DRIVER_PATH, 'MicrosoftWebDriver.exe'))
  except (RequestException, BadZipFile, Error, OSError) as e:
    print(f'Failed to get {version} update. Manual update is needed:\n', e)

def checkUpdate():
  if isEdgeWebDriverUpdated():
    print(f'Driver Up-To-Date: {EDGE_DRIVER_VERSION}')
  else:
    print('Browser/Web Driver not compatible')
    print(f'Updating Driver to: {EDGE_BROWSER_VERSION}')
    updateEdgeWebDriver()

checkUpdate()  