\* China_coal_cost_problem *\
Minimize
OBJ: 350.131 directional_edge_('Australia___bin_1',_'Australia_out')
 + 500.131 directional_edge_('Australia___bin_2',_'Australia_out')
 + 700.131 directional_edge_('Australia___bin_3',_'Australia_out')
 + 60 directional_edge_('Australia_out',_'Caofeidian')
 + 54 directional_edge_('Australia_out',_'Guangdong')
 + 55.5 directional_edge_('Australia_out',_'Jiangsu')
 + 37.5 directional_edge_('Caofeidian',_'Guangdong')
 + 31.5 directional_edge_('Caofeidian',_'Hebei')
 + 39 directional_edge_('Caofeidian',_'Jiangsu')
 + 1058.5 directional_edge_('Inner_Mongolia',_'Caofeidian')
 + 927.5 directional_edge_('Inner_Mongolia',_'Hebei')
 + 413.1 directional_edge_('Shaanxi___bin_1',_'Shaanxi_out')
 + 513.1 directional_edge_('Shaanxi___bin_2',_'Shaanxi_out')
 + 813.1 directional_edge_('Shaanxi___bin_3',_'Shaanxi_out')
 + 262 directional_edge_('Shaanxi_out',_'Caofeidian')
 + 104.8 directional_edge_('Shaanxi_out',_'Hebei')
Subject To
_C1: - directional_edge_('Shaanxi___bin_1',_'Shaanxi_out') >= -4000
_C10: directional_edge_('Australia_out',_'Caofeidian')
 - directional_edge_('Caofeidian',_'Guangdong')
 - directional_edge_('Caofeidian',_'Hebei')
 - directional_edge_('Caofeidian',_'Jiangsu')
 + directional_edge_('Inner_Mongolia',_'Caofeidian')
 + directional_edge_('Shaanxi_out',_'Caofeidian') >= 0
_C11: directional_edge_('Caofeidian',_'Hebei')
 + directional_edge_('Inner_Mongolia',_'Hebei')
 + directional_edge_('Shaanxi_out',_'Hebei') >= 3000
_C12: directional_edge_('Australia_out',_'Guangdong')
 + directional_edge_('Caofeidian',_'Guangdong') >= 6000
_C13: directional_edge_('Australia_out',_'Jiangsu')
 + directional_edge_('Caofeidian',_'Jiangsu') >= 4000
_C2: - directional_edge_('Shaanxi___bin_2',_'Shaanxi_out') >= -5000
_C3: - directional_edge_('Shaanxi___bin_3',_'Shaanxi_out') >= -12000
_C4: - directional_edge_('Australia___bin_1',_'Australia_out') >= -4000
_C5: - directional_edge_('Australia___bin_2',_'Australia_out') >= -5000
_C6: - directional_edge_('Australia___bin_3',_'Australia_out') >= -12000
_C7: - directional_edge_('Inner_Mongolia',_'Caofeidian')
 - directional_edge_('Inner_Mongolia',_'Hebei') >= -10000
_C8: directional_edge_('Shaanxi___bin_1',_'Shaanxi_out')
 + directional_edge_('Shaanxi___bin_2',_'Shaanxi_out')
 + directional_edge_('Shaanxi___bin_3',_'Shaanxi_out')
 - directional_edge_('Shaanxi_out',_'Caofeidian')
 - directional_edge_('Shaanxi_out',_'Hebei') >= 0
_C9: directional_edge_('Australia___bin_1',_'Australia_out')
 + directional_edge_('Australia___bin_2',_'Australia_out')
 + directional_edge_('Australia___bin_3',_'Australia_out')
 - directional_edge_('Australia_out',_'Caofeidian')
 - directional_edge_('Australia_out',_'Guangdong')
 - directional_edge_('Australia_out',_'Jiangsu') >= 0
Bounds
0 <= directional_edge_('Australia___bin_1',_'Australia_out') <= 1000000000
0 <= directional_edge_('Australia___bin_2',_'Australia_out') <= 1000000000
0 <= directional_edge_('Australia___bin_3',_'Australia_out') <= 1000000000
0 <= directional_edge_('Australia_out',_'Caofeidian') <= 2000
0 <= directional_edge_('Australia_out',_'Guangdong') <= 4000
0 <= directional_edge_('Australia_out',_'Jiangsu') <= 2000
0 <= directional_edge_('Caofeidian',_'Guangdong') <= 2000
0 <= directional_edge_('Caofeidian',_'Hebei') <= 1000
0 <= directional_edge_('Caofeidian',_'Jiangsu') <= 2000
0 <= directional_edge_('Inner_Mongolia',_'Caofeidian') <= 3000
0 <= directional_edge_('Inner_Mongolia',_'Hebei') <= 2000
0 <= directional_edge_('Shaanxi___bin_1',_'Shaanxi_out') <= 1000000000
0 <= directional_edge_('Shaanxi___bin_2',_'Shaanxi_out') <= 1000000000
0 <= directional_edge_('Shaanxi___bin_3',_'Shaanxi_out') <= 1000000000
0 <= directional_edge_('Shaanxi_out',_'Caofeidian') <= 5000
0 <= directional_edge_('Shaanxi_out',_'Hebei') <= 1000
Generals
directional_edge_('Australia___bin_1',_'Australia_out')
directional_edge_('Australia___bin_2',_'Australia_out')
directional_edge_('Australia___bin_3',_'Australia_out')
directional_edge_('Australia_out',_'Caofeidian')
directional_edge_('Australia_out',_'Guangdong')
directional_edge_('Australia_out',_'Jiangsu')
directional_edge_('Caofeidian',_'Guangdong')
directional_edge_('Caofeidian',_'Hebei')
directional_edge_('Caofeidian',_'Jiangsu')
directional_edge_('Inner_Mongolia',_'Caofeidian')
directional_edge_('Inner_Mongolia',_'Hebei')
directional_edge_('Shaanxi___bin_1',_'Shaanxi_out')
directional_edge_('Shaanxi___bin_2',_'Shaanxi_out')
directional_edge_('Shaanxi___bin_3',_'Shaanxi_out')
directional_edge_('Shaanxi_out',_'Caofeidian')
directional_edge_('Shaanxi_out',_'Hebei')
End
