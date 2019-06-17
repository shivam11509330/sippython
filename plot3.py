# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:10:01 2019

@author: aa
"""


name=['shivam','prakash','danish','sahil']
marks=[98,35,11,55]
index=np.arange(len(name))
plt.bar(index,marks)
plt.xlabel('student',fontsize=5)
plt.ylabel('total marks',fontsize=5)
plt.xticks(index,name,fontsize=5)
plt.bar(name,marks)
