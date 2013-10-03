######################################################################
#
# FSP3000R7OSCMib modeler pluginn
#
# Copyright (C) 2011 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
######################################################################

__doc__="""FSP3000R7OSCMib

FSP3000R7OSCMib maps OSC amplifiers on a FSP3000R7 system

"""

from ZenPacks.Merit.AdvaFSP3000R7.lib.FSP3000R7MibCommon import FSP3000R7MibCommon

class FSP3000R7OSCMib(FSP3000R7MibCommon):

    modname = "ZenPacks.Merit.AdvaFSP3000R7.FSP3000R7OSC"
    relname = "FSP3000R7Osc"

    componentModels = [ 'OSCM-PN', 'OSCM-V#1630', '2OSCM-V#1630']
