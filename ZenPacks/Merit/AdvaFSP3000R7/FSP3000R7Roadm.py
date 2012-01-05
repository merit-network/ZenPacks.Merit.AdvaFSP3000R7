######################################################################
#
# FSP3000R7Roadm object class
#
# Copyright (C) 2011 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
######################################################################

__doc__="""FSP3000R7Roadm

FSP3000R7Roadm is a component of a FSP3000R7Device Device

"""

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity

import logging
log = logging.getLogger('FSP3000R7Roadm')

class FSP3000R7Roadm(DeviceComponent, ManagedEntity, ZenPackPersistence):
    """FSP3000R7Roadm object"""

    portal_type = meta_type = 'FSP3000R7Roadm'

    # set default _properties
    EntityIndex           = -1
    inventoryUnitName     = 'Not set by modeler'
    entityIndexAid        = 'Not set by modeler'
    sortKey               = '000000000'
    entityAssignmentState = 'Not set by modeler'

    _properties = (
        # from ADVA inventory entityTable
        {'id':'EntityIndex',           'type':'int',    'mode':''},
        # from ADVA inventory MIB
        {'id':'inventoryUnitName',     'type':'string', 'mode':''},
        # human readable physical location of ROADM in shelf
        {'id':'entityIndexAid',        'type':'string', 'mode':''},
        # string used to sort names in GUI
        {'id':'sortKey',               'type':'string', 'mode':''},
        {'id':'entityAssignmentState', 'type':'string', 'mode':''},
        )

    _relations = (
        ("FSP3000R7Dev", ToOne(ToManyCont,
             "ZenPacks.Merit.AdvaFSP3000R7.FSP3000R7Device", "FSP3000R7Road")),
        )

    factory_type_information = (
        {
          'id'             : 'FSP3000R7Roadm',
          'meta_type'      : 'FSP3000R7Roadm',
          'description'    : """ROADM info""",
          'product'        : 'AdvaFSP3000R7',
          'immediate_view' : 'objTemplates',
          'actions'        :
          (
              { 'id'            : 'perfConf',
                'name'          : 'Roadm Template',
                'action'        : 'objTemplates',
                'permissions'   : (ZEN_CHANGE_SETTINGS, )
              },
              { 'id'            : 'viewHistory',
                'name'          : 'Modifications',
                'action'        : 'viewHistory',
                'permissions'   : (ZEN_VIEW, )
              },
          )
         },
        )

    isUserCreatedFlag = True

    def isUserCreated(self):
        """
        Returns the value of isUserCreated. True adds SAVE & CANCEL buttons to Details menu
        """
        return self.isUserCreatedFlag

    def viewName(self):
        """Human readable version of this object"""
        if self.inventoryUnitName == 'Not set by modeler' or self.EntityIndex == '-1':
            return "Unknown"
        return(self.entityIndexAid)

    # use viewName as titleOrId because that method is used to display a human
    # readable version of the object in the breadcrumbs
    name = viewName

    def primarySortKey(self):
        return self.sortKey

    def device(self):
        return self.FSP3000R7Dev()

    def monitored(self):
        """Monitor amplifier if it's provisioned (same thing as assigned)"""
# Not sure why this always returns False.  It's cosmetic so force True
#        if self.entityAssignmentState == '1':
#            return True
#        else:
#            return False
        return True


InitializeClass(FSP3000R7Roadm)
