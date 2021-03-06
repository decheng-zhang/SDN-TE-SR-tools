import os


def single_execution(): 

	base_filename = "flow_cata_topo_%s_%s_%s_%s_%s_%s_seed%s" \
	%(topology, access_node_prob, t_rel_prob, mean_num_flows, max_num_flows, link__to_t_rel_ratio, my_seed)

#	command = "python ste-test.py %s --in %s --out t3d --access_node_prob %s --t_rel_prob %s --mean_num_flows %s --max_num_flows %s --link__to_t_rel_ratio %s --seed %s > %s/%s.info" \
	command = "python ste-test.py %s --in %s --out t3d --access_node_prob %s --t_rel_prob %s --mean_num_flows %s --max_num_flows %s --link__to_t_rel_ratio %s --seed %s > %s/%s.info" \
	%(file_in_name, file_in_type, access_node_prob, t_rel_prob, mean_num_flows, max_num_flows, link__to_t_rel_ratio, my_seed, folder, base_filename)

	print command

	os.system (command)
	command2 = "cp flow_catalogue.json %s/%s.json" %(folder, base_filename)

	print command2

	os.system (command2)



folder = "flow_catalogues"

num_nodes = 153
connection = 1
seed = 69

command0 = "python topologybuilder.py --model barabasi-albert --nodes %s --connection %s --seed %s" \
%(num_nodes, connection,seed)
print command0
os.system (command0)

base_topo_filename = "BA_%s_%s_%s" %(num_nodes, connection,seed)
command01 = "cp nodes.json %s/%s.nodes.json" %(folder, base_topo_filename)
print command01
os.system (command01)

command01 = "cp links.json %s/%s.links.json" %(folder, base_topo_filename)
print command01
os.system (command01)



#file_in_type = "graphml"
#file_in_name = "--f graphml/Colt_2010_08-153N.graphml"

file_in_type = "nx_json"
file_in_name = ""

#topology = "colt153"
topology = "BA_%s_%s_69" %(num_nodes,connection)

my_seed = 69

access_node_prob = 0.4
t_rel_prob = 0.2
mean_num_flows = 4
max_num_flows = 10
link__to_t_rel_ratio = 10


for i in [10, 20, 40, 80]:    #first set
#for i in [60, 70, 80]:         #second set
	link__to_t_rel_ratio = i
	#for j in [69, 70, 71]:
	for j in [69]:
		my_seed = j
#		single_execution()

access_node_prob = 0.8
#for i in [10, 20, 40, 80, 160, 320]:   #first set
for i in [40, 60, 80, 120, 160, 200, 240, 280, 320, 360, 400, 520, 640]:               #second set
	link__to_t_rel_ratio = i
	#for j in [69, 70, 71]:
	for j in [69]:
		my_seed = j
		single_execution()


# python multi-traffic-demand-generator.py
# the generated topology and flows are available in flow_catalogue subfolder


#	python ste-test.py --f graphml/Colt_2010_08-153N.graphml --in graphml --out t3d --access_node_prob 0.4 --t_rel_prob 0.2 --mean_num_flows 4 --max_num_flows 10 --link__to_t_rel_ratio 10 > flow_catalogues/blabla.info 

