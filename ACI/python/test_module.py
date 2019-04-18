from ansible.module_utils.basic import AnsibleModule
import json
argument_spec = dict(
	# List of Ansible required arguements passed from playbook
	vrf_list # Filepath
	site_list # Filepath
)
def menu_vrf():
  vrf_dict = {}
  i = 1
  list = ["WEB","DB","APP"]
#list = ("template/tenant_list.txt","r")
  for vrf in list:
    vrf_dict[i] = vrf
    i += 1
	print ('\n\n')
	print ("____VRF____")

  for key, value in vrf_dict.items():
	  print (key, value)
	vrf_num = input ("Please choose a vrf: ")
	x = int(vrf_num)
	vrf = vrf_dict.get(x)
	print ("Loading ",vrf)
	return vrf
#import ansible.modules.network.aci ??


def menu_site():
  site_dict = {}
  i = 1
  list = ["DC_MONT","DC_SATX","DC_OKCO"]
  for site in list:
    site_dict[i] = site
    i += 1
	print ("____SITE LIST____")
  for key, value in site_dict.items():
    print (key, value)
  site_num = input ("Please choose a site: ")
	x = int(site_num)
	site = site_dict.get(x)
	print("Loading ", site)
	return site

#__main__
s_rank = dict[menu_site())
sss_rank = menu_vrf()
menu_list = [s_rank,sss_rank]
#return this
