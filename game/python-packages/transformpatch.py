# Copyright 2019-2021 GanstaKingofSA
# Copyright 2004-2021 Tom Rothamel <pytom@bishoujo.us>
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###########################################################################

# Transforms.py (located in 'renpy/display/transforms.py') Patch 1.
#
# This patch addresses a bug in Ren'Py 7.4.6 for DDLC where the game
# will not show any transforms when being called by 'show sayori 1a at t11'.
# This bug is caused due to Ren'Py changing the code within the
# 'ATLTransform' class to not excecute the atl states after calling 'super'.

import renpy
from renpy.display.transform import Transform

class ATLTransform(renpy.atl.ATLTransformBase, Transform):

    def __init__(self, atl, child=None, context={}, parameters=None, **properties):
        renpy.atl.ATLTransformBase.__init__(self, atl, context, parameters)
        Transform.__init__(self, child=child, **properties)

        self.raw_child = self.child

    def update_state(self):
        """
        This updates the state to that at self.st, self.at.
        """

        self.hide_response = True
        self.replaced_response = True

        fr = self.execute(self, self.st, self.at)

        # Order a redraw, if necessary.
        if fr is not None:
            renpy.display.render.redraw(self, fr)

        self.active = True

    def __repr__(self):
        return "<ATL Transform {:x} {!r}>".format(id(self), self.atl.loc)

    def _show(self):
        super(ATLTransform, self)._show()
        self.execute(self, self.st, self.at)