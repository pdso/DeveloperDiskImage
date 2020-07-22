import urllib.request
import ssl
import json
import os

ssl._create_default_https_context = ssl._create_unverified_context

def getAllVersions():
  url = 'https://api.github.com/repos/pdso/DeveloperDiskImage/git/trees/master'
  data = urllib.request.urlopen(url).read()
  json_data = json.loads(data)
  return [item.get('path') for item in json_data.get('tree')][0:-3]

def downloadDiskImage(version):
  # https://raw.githubusercontent.com/user/repository/branch/filename
  # DeveloperDiskImage.dmg DeveloperDiskImage.dmg.signature
  xcodepath = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'
  os.chdir(xcodepath)
  os.system(f'mkdir {version}')
  os.chdir(f'{xcodepath}/{version}')
  dmg = f'https://raw.githubusercontent.com/pdso/DeveloperDiskImage/master/{version}/DeveloperDiskImage.dmg'
  signature = f'https://raw.githubusercontent.com/pdso/DeveloperDiskImage/master/{version}/DeveloperDiskImage.dmg.signature'
  curl_dmg = f'curl -L {dmg} -o DeveloperDiskImage.dmg'
  curl_signature = f'curl -L {signature} -o DeveloperDiskImage.dmg.signature'
  print('Dowloading DeveloperDiskImage.dmg file')
  os.system(curl_dmg)
  print('\nDowloading DeveloperDiskImage.dmg.signature file')
  os.system(curl_signature)
  os.system('open .')

if __name__ == "__main__":
  versions = getAllVersions()
  s = '\n'.join(versions)
  print(f'Support iOS DeveloperDiskImage Versions: \n\n{s}\n')
  default = versions[-1]
  print(f"Please input the DeveloperDiskImage version your want, default is {default}: ")
  default = 14.0
  x = input()
  if x == "":
    downloadDiskImage(default)
  elif x in ['14.0']:
    downloadDiskImage(x)
  else:
    print('Not support version')