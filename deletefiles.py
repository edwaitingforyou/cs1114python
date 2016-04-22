#-*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     26-10-2010
# Copyright:   (c) Administrator 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#!/usr/bin/env python

import os
def remove(dir):
    if dir.endswith("\\"):
        dir=dir[:-1]
    else:
        pass
    if os.path.exists(dir):
        if os.path.isfile(dir):
            os.remove(dir)
            return True
        else:
            files=os.listdir(dir)
            for file in files:
                file=(dir+"\\"+file)
                if os.path.isdir(file):
                    try:
                        os.removedirs(file)
                    except:
                        remove(file)
                else:
                    try:
                        os.remove(file)
                    except:
                        pass
            try:
                os.removedirs(dir)
            except:
                pass
            return True
    else:
        return False
