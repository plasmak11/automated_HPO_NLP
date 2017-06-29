import json
import re
import requests
import os
from lxml import etree

### Iterate through list of CUI files
for filename in os.listdir('xml/'):

    print filename
    with open(os.path.join('xml/', filename), 'rb') as f:
        tree = etree.parse(f)
        root = tree.getroot()
        code_list = []
        for each in root.findall(".//code/.."):

            prt = each.getparent().getparent()

            # 'c' key contains Section Header information
            if 'c' in prt.attrib:

                # excludes Review of Systems section item
                if (prt.attrib['c'] != 'report review of systems item'):
                    HPO_code = []


                    for child in each:
                        if (child.attrib is None):
                            pass
                        else:
                            for grandchild in child.iter( ):
                                if 'v' in grandchild.attrib:
                                    if (grandchild.tag == 'certainty' or grandchild.tag == 'code'):

                                        HPO_code.append(grandchild.attrib['v'])

                            for pair in HPO_code:

                                if len ( HPO_code ) > 0:
                                    # Checks for 'certainty' = 'no' means that it's a negated concept.
                                    # Only add concepts to HPO_code if it's a non-negated concept.
                                    if (HPO_code[0] != 'no'):
                                        for item in HPO_code:
                                            if item.startswith ( 'HP:' ):
                                                code_list.append ( item )
            else:
                pass
        # Print all non-negated HPO concepts identified from the MedLEE XML
        print '\t'.join(('\n'.join(set(code_list))).split('_'))