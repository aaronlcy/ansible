# -*- mode: python -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}


DOCUMENTATION = '''
---
module: group_by
short_description: Create Ansible groups based on facts
description:
  - Use facts to create ad-hoc groups that can be used later in a playbook.
  - This module is also supported for Windows targets.
version_added: "0.9"
options:
  key:
    description:
    - The variables whose values will be used as groups
    required: true
  parents:
    description:
    - The list of the parent groups
    required: false
    default: "all"
    version_added: "2.4"
author: "Jeroen Hoekx (@jhoekx)"
notes:
  - Spaces in group names are converted to dashes '-'.
  - This module is also supported for Windows targets.
'''

EXAMPLES = '''
# Create groups based on the machine architecture
- group_by:
    key: machine_{{ ansible_machine }}

# Create groups like 'kvm-host'
- group_by:
    key: virt_{{ ansible_virtualization_type }}_{{ ansible_virtualization_role }}

# Create nested groups
- group_by:
    key: el{{ ansible_distribution_major_version }}-{{ ansible_architecture }}
    parents:
      - el{{ ansible_distribution_major_version }}

'''
