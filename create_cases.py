"""Create two cases with small differences
"""
import pypowsybl.network as pn
n = pn.create_ieee9()
# XIIDM is the internal xml format
n.save('case1/case1.xml', format='CGMES')

n.update_lines(id='L7-8-0', r='3.14', x='1.59')
n.save('case2/case2.xml', format='CGMES')