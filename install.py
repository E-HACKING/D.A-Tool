import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install D.A-Tool [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/D.A-Tool"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/D.A-Tool")
          os.system(system.sudo+" cp -r modules core D.A-Tool.py "+system.conf_dir+"/D.A-Tool")
          os.system(system.sudo+" cp -r core/D.A-Tool "+system.bin)
          os.system(system.sudo+" cp -r core/DAtool "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/D.A-Tool")
          os.system(system.sudo+" chmod +x "+system.bin+"/DAtool")
          os.system("cd .. && "+system.sudo+" rm -rf D.A-Tool")
          if os.path.exists(system.bin+"/D.A-Tool") and os.path.exists(system.conf_dir+"/D.A-Tool"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}D.A-Tool{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}D.A-Tool{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/D.A-Tool"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/D.A-Tool")
          os.system("cp -r modules core D.A-Tool.py "+system.conf_dir+"/Tool-X")
          os.system("cp -r core/D.A-Tool"+system.bin)
          os.system("cp -r core/DAtool "+system.bin)
          os.system("chmod +x "+system.bin+"/D.A-Tool)
          os.system("chmod +x "+system.bin+"/DAtool")
          os.system("cd .. && rm -rf D.A-Tool")
          if os.path.exists(system.bin+"/D.A-Tool") and os.path.exists(system.conf_dir+"/D.A-Tool"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}D.A-Tool{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}D.A-Tool{nc}@{blue}space {yellow}$ {nc}")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
