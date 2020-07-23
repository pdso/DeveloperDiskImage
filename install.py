import ssl
import json
import sys
import os

ssl._create_default_https_context = ssl._create_unverified_context

def getAllVersions():
  try: #python3
    from urllib.request import urlopen
  except: #python2
    from urllib2 import urlopen
  url = 'https://api.github.com/repos/pdso/DeveloperDiskImage/git/trees/master'
  data = urlopen(url).read()
  json_data = json.loads(data)
  return [item.get('path') for item in json_data.get('tree')][0:-3]

def downloadDiskImage(version):
  # https://raw.githubusercontent.com/user/repository/branch/filename
  # DeveloperDiskImage.dmg DeveloperDiskImage.dmg.signature
  xcodepath = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'
  os.chdir(xcodepath)
  os.system('mkdir {}'.format(version))
  os.chdir('{}/{}'.format(xcodepath, version))
  dmg = 'https://raw.githubusercontent.com/pdso/DeveloperDiskImage/master/{}/DeveloperDiskImage.dmg'.format(version)
  signature = 'https://raw.githubusercontent.com/pdso/DeveloperDiskImage/master/{}/DeveloperDiskImage.dmg.signature'.format(version)
  curl_dmg = 'curl -L {} -o DeveloperDiskImage.dmg'.format(dmg)
  curl_signature = 'curl -L {} -o DeveloperDiskImage.dmg.signature'.format(signature)
  print('Dowloading DeveloperDiskImage.dmg file')
  os.system(curl_dmg)
  print('\nDowloading DeveloperDiskImage.dmg.signature file')
  os.system(curl_signature)
  os.system('open .')
  
if __name__ == "__main__":
  versions = getAllVersions()
  s = '\n'.join(versions)
  print('Support iOS DeveloperDiskImage Versions: \n\n{}\n'.format(s))
  default = versions[-1]
  message = 'Please input the DeveloperDiskImage version your want, default is {}: '.format(default)
  try:
    input = raw_input
  except NameError:
    pass
  x = input(message)
  if x.isspace:
    downloadDiskImage(default)
  elif x in versions:
    downloadDiskImage(x)
  else:
    print('Not support version')