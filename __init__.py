import os
from cudatext import *

fn_icon = os.path.join(os.path.dirname(__file__), 'fm.png')

def on_resize_ex(*args, **vargs):
  print('-- on resize')

class Command:
    
  def __init__(self):
    self.title = 'on_resize_fail'
    self.h_dlg = None

  def open(self):
    if not self.h_dlg:
        self.open_init()

    app_proc(PROC_SIDEPANEL_ACTIVATE, (self.title, True))
    
  def open_init(self):
    self.h_dlg = self.init_form()
        
    app_proc(PROC_SIDEPANEL_ADD_DIALOG, (self.title, self.h_dlg, fn_icon))
        
  def init_form(self):
    
    h = dlg_proc(0, DLG_CREATE)
    dlg_proc(h, DLG_PROP_SET, prop={
     
        ##### none of these work #####
    
        #'on_resize': lambda *args,**vargs: print('-- on resize'),
        #'on_resize': 'cuda_on_resize_fail.on_resize;',
        #'on_resize': 'module=cuda_on_resize_fail;cmd=on_resize;',
        'on_resize': 'module=cuda_on_resize_fail;func=on_resize_ex;',
        })
        
    return h
    
  def on_resize(self, *args, **vargs):
    print('-- on resize')
