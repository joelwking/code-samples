# Dynamic inventory
Example of using a CSV file as input to a Python module which creates a dynamic inventory for Ansible. The column headers in the file are the host variable names, the values of the column are the value of the host_vars.  The program does not return group_vars.

## Sample playbook
The file `get_invy.yml` is a sample playbook

## Sample output
Standard out of a sample execution
```
administrator@flint:~/ansible/playbooks$ ansible-playbook -i get_inventory.py get_invy.yml

PLAY [test dynamic inventory] **************************************************

TASK [Debug] *******************************************************************
ok: [STUDENT_POD_1] => {
    "msg": "STUDENT_POD_1 10.255.111.221 GISFP-CAT-SERQY-IVNUG-WGSZWAP"
}
ok: [STUDENT_POD_2] => {
    "msg": "STUDENT_POD_2 10.255.111.223 GISFP-CAT-SERQY-IVNUG-WGSZWAP"
}

PLAY RECAP *********************************************************************
STUDENT_POD_1              : ok=1    changed=0    unreachable=0    failed=0
STUDENT_POD_2              : ok=1    changed=0    unreachable=0    failed=0
```