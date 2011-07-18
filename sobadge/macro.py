# Created by Michael Caron on 2010-01-20.
# Copyright (c) 2009 Michael Caron. All rights reserved.

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.util.html import html as tag

class SoBadgeMacro(WikiMacroBase):
    """A small maco for showing Stack Overflow (http://stackoverflow.com) statistics badges."""
    
    SCRIPT_LOCATION = 'http://stackoverflow.com/users/flair/%s.js'
    
    def render_macro(self, req, name, content):
        content = content.strip()
        if not content.isdigit():
            return system_message('Invalid Stackoverflow User', '%s is not a number'%content)
        return tag.script('', src=self.SCRIPT_LOCATION%content, type='text/javascript')



