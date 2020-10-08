\* China_coal_cost_problem *\
Minimize
OBJ: 800 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 + 1000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 + 350 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + 500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + 400 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + 500 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + 13.1 flow_total_('Australia',_'Caofeidian')
 + 0.131 flow_total_('Beijing',_'Tianjin')
 + 0.131 flow_total_('Caofeidian',_'Beijing')
 + 0.131 flow_total_('Hebei',_'Beijing')
 + 0.131 flow_total_('Indonesia',_'Caofeidian')
 + 13.1 flow_total_('Inner_Mongolia',_'Hebei')
 + 13.1 flow_total_('Shaanxi',_'Hebei')
Subject To
_C1: - flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + supply_coaltype_by_node_('Shaanxi',_'SX_A') >= 0
_C10: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 + supply_coaltype_by_node_('Inner_Mongolia',_'AUS_A') >= 0
_C11: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 + supply_coaltype_by_node_('Inner_Mongolia',_'AUS_B') >= 0
_C12: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 + supply_coaltype_by_node_('Inner_Mongolia',_'IND_A') >= 0
_C13: - flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 + supply_coaltype_by_node_('Australia',_'SX_A') >= 0
_C14: - flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Australia',_'SX_B') >= 0
_C15: - flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 + supply_coaltype_by_node_('Australia',_'IM_A') >= 0
_C16: - flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 + supply_coaltype_by_node_('Australia',_'AUS_A') >= 0
_C17: - flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 + supply_coaltype_by_node_('Australia',_'AUS_B') >= 0
_C18: - flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 + supply_coaltype_by_node_('Australia',_'IND_A') >= 0
_C19: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 + supply_coaltype_by_node_('Indonesia',_'SX_A') >= 0
_C2: - flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Shaanxi',_'SX_B') >= 0
_C20: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Indonesia',_'SX_B') >= 0
_C21: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 + supply_coaltype_by_node_('Indonesia',_'IM_A') >= 0
_C22: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 + supply_coaltype_by_node_('Indonesia',_'AUS_A') >= 0
_C23: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 + supply_coaltype_by_node_('Indonesia',_'AUS_B') >= 0
_C24: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + supply_coaltype_by_node_('Indonesia',_'IND_A') >= 0
_C25: flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 + supply_coaltype_by_node_('Caofeidian',_'SX_A') >= 0
_C26: flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Caofeidian',_'SX_B') >= 0
_C27: flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 + supply_coaltype_by_node_('Caofeidian',_'IM_A') >= 0
_C28: flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 + supply_coaltype_by_node_('Caofeidian',_'AUS_A') >= 0
_C29: flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 + supply_coaltype_by_node_('Caofeidian',_'AUS_B') >= 0
_C3: - flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 + supply_coaltype_by_node_('Shaanxi',_'IM_A') >= 0
_C30: flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + supply_coaltype_by_node_('Caofeidian',_'IND_A') >= 0
_C31: - flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + supply_coaltype_by_node_('Hebei',_'SX_A') >= 0
_C32: - flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Hebei',_'SX_B') >= 0
_C33: - flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 + supply_coaltype_by_node_('Hebei',_'IM_A') >= 0
_C34: - flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 + supply_coaltype_by_node_('Hebei',_'AUS_A') >= 0
_C35: - flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 + supply_coaltype_by_node_('Hebei',_'AUS_B') >= 0
_C36: - flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 + supply_coaltype_by_node_('Hebei',_'IND_A') >= 0
_C37: - flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 + supply_coaltype_by_node_('Beijing',_'SX_A') >= 0
_C38: - flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + supply_coaltype_by_node_('Beijing',_'SX_B') >= 0
_C39: - flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 + supply_coaltype_by_node_('Beijing',_'IM_A') >= 0
_C4: - flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 + supply_coaltype_by_node_('Shaanxi',_'AUS_A') >= 0
_C40: - flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 + supply_coaltype_by_node_('Beijing',_'AUS_A') >= 0
_C41: - flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 + flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 + supply_coaltype_by_node_('Beijing',_'AUS_B') >= 0
_C42: - flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 + supply_coaltype_by_node_('Beijing',_'IND_A') >= 0
_C43: flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 + supply_coaltype_by_node_('Tianjin',_'SX_A') >= 0
_C44: flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + supply_coaltype_by_node_('Tianjin',_'SX_B') >= 0
_C45: flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 + supply_coaltype_by_node_('Tianjin',_'IM_A') >= 0
_C46: flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 + supply_coaltype_by_node_('Tianjin',_'AUS_A') >= 0
_C47: flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 + supply_coaltype_by_node_('Tianjin',_'AUS_B') >= 0
_C48: flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 + supply_coaltype_by_node_('Tianjin',_'IND_A') >= 0
_C49: - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 - 3500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 - 2500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 - 5500 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + 7000 supply_coaltype_by_node_('Shaanxi',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Shaanxi',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Shaanxi',_'IM_A')
 + 2500 supply_coaltype_by_node_('Shaanxi',_'IND_A')
 + 5500 supply_coaltype_by_node_('Shaanxi',_'SX_A')
 + 7000 supply_coaltype_by_node_('Shaanxi',_'SX_B') >= 0
_C5: - flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 + supply_coaltype_by_node_('Shaanxi',_'AUS_B') >= 0
_C50: - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 - 3500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 - 2500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 - 5500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + 7000 supply_coaltype_by_node_('Inner_Mongolia',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Inner_Mongolia',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Inner_Mongolia',_'IM_A')
 + 2500 supply_coaltype_by_node_('Inner_Mongolia',_'IND_A')
 + 5500 supply_coaltype_by_node_('Inner_Mongolia',_'SX_A')
 + 7000 supply_coaltype_by_node_('Inner_Mongolia',_'SX_B') >= 0
_C51: - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 - 3500 flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 - 2500 flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 - 5500 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 + 7000 supply_coaltype_by_node_('Australia',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Australia',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Australia',_'IM_A')
 + 2500 supply_coaltype_by_node_('Australia',_'IND_A')
 + 5500 supply_coaltype_by_node_('Australia',_'SX_A')
 + 7000 supply_coaltype_by_node_('Australia',_'SX_B') >= 0
_C52: - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 - 3500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 - 2500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 - 5500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + 7000 supply_coaltype_by_node_('Indonesia',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Indonesia',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Indonesia',_'IM_A')
 + 2500 supply_coaltype_by_node_('Indonesia',_'IND_A')
 + 5500 supply_coaltype_by_node_('Indonesia',_'SX_A')
 + 7000 supply_coaltype_by_node_('Indonesia',_'SX_B') >= 0
_C53: 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 + 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 + 3500 flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 + 2500 flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 + 5500 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 + 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 - 3500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 - 2500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 - 5500 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 + 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 + 3500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 + 2500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + 5500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 + 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + 7000 supply_coaltype_by_node_('Caofeidian',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Caofeidian',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Caofeidian',_'IM_A')
 + 2500 supply_coaltype_by_node_('Caofeidian',_'IND_A')
 + 5500 supply_coaltype_by_node_('Caofeidian',_'SX_A')
 + 7000 supply_coaltype_by_node_('Caofeidian',_'SX_B') >= 0
_C54: - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 - 3500 flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 - 2500 flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 - 5500 flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 + 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 + 3500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + 2500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 + 5500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 + 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 + 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 + 3500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 + 2500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 + 5500 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + 7000 supply_coaltype_by_node_('Hebei',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Hebei',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Hebei',_'IM_A')
 + 2500 supply_coaltype_by_node_('Hebei',_'IND_A')
 + 5500 supply_coaltype_by_node_('Hebei',_'SX_A')
 + 7000 supply_coaltype_by_node_('Hebei',_'SX_B') >= 0
_C55: - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 - 3500 flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 - 2500 flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 - 5500 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 + 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 + 3500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 + 2500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 + 5500 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 + 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 + 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 + 3500 flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 + 2500 flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 + 5500 flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 + 7000 flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + 7000 supply_coaltype_by_node_('Beijing',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Beijing',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Beijing',_'IM_A')
 + 2500 supply_coaltype_by_node_('Beijing',_'IND_A')
 + 5500 supply_coaltype_by_node_('Beijing',_'SX_A')
 + 7000 supply_coaltype_by_node_('Beijing',_'SX_B') >= 4000000
_C56: 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 + 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 + 3500 flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 + 2500 flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 + 5500 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 + 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + 7000 supply_coaltype_by_node_('Tianjin',_'AUS_A')
 + 7000 supply_coaltype_by_node_('Tianjin',_'AUS_B')
 + 3500 supply_coaltype_by_node_('Tianjin',_'IM_A')
 + 2500 supply_coaltype_by_node_('Tianjin',_'IND_A')
 + 5500 supply_coaltype_by_node_('Tianjin',_'SX_A')
 + 7000 supply_coaltype_by_node_('Tianjin',_'SX_B') >= 2000000
_C57: - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 - 3500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 - 2500 flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 - 5500 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 - 7000 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Shaanxi',_'AUS_A')
 + 2 supply_coaltype_by_node_('Shaanxi',_'IM_A')
 + 5 supply_coaltype_by_node_('Shaanxi',_'IND_A')
 + 3 supply_coaltype_by_node_('Shaanxi',_'SX_A')
 + supply_coaltype_by_node_('Shaanxi',_'SX_B') <= 0
_C58: - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 - 3500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 - 2500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 - 5500 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 - 7000 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Inner_Mongolia',_'AUS_A')
 + 2 supply_coaltype_by_node_('Inner_Mongolia',_'IM_A')
 + 5 supply_coaltype_by_node_('Inner_Mongolia',_'IND_A')
 + 3 supply_coaltype_by_node_('Inner_Mongolia',_'SX_A')
 + supply_coaltype_by_node_('Inner_Mongolia',_'SX_B') <= 0
_C59: - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 - 3500 flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 - 2500 flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 - 5500 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 - 7000 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Australia',_'AUS_A')
 + 2 supply_coaltype_by_node_('Australia',_'IM_A')
 + 5 supply_coaltype_by_node_('Australia',_'IND_A')
 + 3 supply_coaltype_by_node_('Australia',_'SX_A')
 + supply_coaltype_by_node_('Australia',_'SX_B') <= 0
_C6: - flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 + supply_coaltype_by_node_('Shaanxi',_'IND_A') >= 0
_C60: - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 - 3500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 - 2500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 - 5500 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 - 7000 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Indonesia',_'AUS_A')
 + 2 supply_coaltype_by_node_('Indonesia',_'IM_A')
 + 5 supply_coaltype_by_node_('Indonesia',_'IND_A')
 + 3 supply_coaltype_by_node_('Indonesia',_'SX_A')
 + supply_coaltype_by_node_('Indonesia',_'SX_B') <= 0
_C61: flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 + 2 flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 + 5 flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 + 3 flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 - 3500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 - 2500 flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 - 5500 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 - 7000 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 + 2 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 + 5 flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + 3 flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + supply_coaltype_by_node_('Caofeidian',_'AUS_A')
 + 2 supply_coaltype_by_node_('Caofeidian',_'IM_A')
 + 5 supply_coaltype_by_node_('Caofeidian',_'IND_A')
 + 3 supply_coaltype_by_node_('Caofeidian',_'SX_A')
 + supply_coaltype_by_node_('Caofeidian',_'SX_B') <= 0
_C62: - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 - 3500 flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 - 2500 flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 - 5500 flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 - 7000 flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 + 2 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + 5 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 + 3 flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 + 2 flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 + 5 flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 + 3 flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Hebei',_'AUS_A')
 + 2 supply_coaltype_by_node_('Hebei',_'IM_A')
 + 5 supply_coaltype_by_node_('Hebei',_'IND_A')
 + 3 supply_coaltype_by_node_('Hebei',_'SX_A')
 + supply_coaltype_by_node_('Hebei',_'SX_B') <= 0
_C63: - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 - 3500 flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 - 2500 flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 - 5500 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 - 7000 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 + 2 flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 + 5 flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 + 3 flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 + 2 flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 + 5 flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 + 3 flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + supply_coaltype_by_node_('Beijing',_'AUS_A')
 + 2 supply_coaltype_by_node_('Beijing',_'IM_A')
 + 5 supply_coaltype_by_node_('Beijing',_'IND_A')
 + 3 supply_coaltype_by_node_('Beijing',_'SX_A')
 + supply_coaltype_by_node_('Beijing',_'SX_B') <= 5000
_C64: flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 + 2 flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 + 5 flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 + 3 flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + supply_coaltype_by_node_('Tianjin',_'AUS_A')
 + 2 supply_coaltype_by_node_('Tianjin',_'IM_A')
 + 5 supply_coaltype_by_node_('Tianjin',_'IND_A')
 + 3 supply_coaltype_by_node_('Tianjin',_'SX_A')
 + supply_coaltype_by_node_('Tianjin',_'SX_B') <= 0
_C65: flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 + flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B') <= 350
_C66: flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 + flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B') <= 250
_C67: flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 + flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B') <= 400
_C68: flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 + flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B') <= 60000
_C69: flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 + flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Hebei',_'Beijing',_'SX_B') <= 500
_C7: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 + supply_coaltype_by_node_('Inner_Mongolia',_'SX_A') >= 0
_C70: flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 + flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B') <= 500
_C71: flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 + flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B') <= 1000
_C72: - flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_A')
 - flow_by_coaltype_('Shaanxi',_'Hebei',_'AUS_B')
 - flow_by_coaltype_('Shaanxi',_'Hebei',_'IM_A')
 - flow_by_coaltype_('Shaanxi',_'Hebei',_'IND_A')
 - flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_A')
 - flow_by_coaltype_('Shaanxi',_'Hebei',_'SX_B')
 + flow_total_('Shaanxi',_'Hebei') = 0
_C73: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_A')
 - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'AUS_B')
 - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IND_A')
 - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_A')
 - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + flow_total_('Inner_Mongolia',_'Hebei') = 0
_C74: - flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_A')
 - flow_by_coaltype_('Australia',_'Caofeidian',_'AUS_B')
 - flow_by_coaltype_('Australia',_'Caofeidian',_'IM_A')
 - flow_by_coaltype_('Australia',_'Caofeidian',_'IND_A')
 - flow_by_coaltype_('Australia',_'Caofeidian',_'SX_A')
 - flow_by_coaltype_('Australia',_'Caofeidian',_'SX_B')
 + flow_total_('Australia',_'Caofeidian') = 0
_C75: - flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_A')
 - flow_by_coaltype_('Indonesia',_'Caofeidian',_'AUS_B')
 - flow_by_coaltype_('Indonesia',_'Caofeidian',_'IM_A')
 - flow_by_coaltype_('Indonesia',_'Caofeidian',_'IND_A')
 - flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_A')
 - flow_by_coaltype_('Indonesia',_'Caofeidian',_'SX_B')
 + flow_total_('Indonesia',_'Caofeidian') = 0
_C76: - flow_by_coaltype_('Hebei',_'Beijing',_'AUS_A')
 - flow_by_coaltype_('Hebei',_'Beijing',_'AUS_B')
 - flow_by_coaltype_('Hebei',_'Beijing',_'IM_A')
 - flow_by_coaltype_('Hebei',_'Beijing',_'IND_A')
 - flow_by_coaltype_('Hebei',_'Beijing',_'SX_A')
 - flow_by_coaltype_('Hebei',_'Beijing',_'SX_B')
 + flow_total_('Hebei',_'Beijing') = 0
_C77: - flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'AUS_B')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'IM_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'IND_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_A')
 - flow_by_coaltype_('Caofeidian',_'Beijing',_'SX_B')
 + flow_total_('Caofeidian',_'Beijing') = 0
_C78: - flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_A')
 - flow_by_coaltype_('Beijing',_'Tianjin',_'AUS_B')
 - flow_by_coaltype_('Beijing',_'Tianjin',_'IM_A')
 - flow_by_coaltype_('Beijing',_'Tianjin',_'IND_A')
 - flow_by_coaltype_('Beijing',_'Tianjin',_'SX_A')
 - flow_by_coaltype_('Beijing',_'Tianjin',_'SX_B')
 + flow_total_('Beijing',_'Tianjin') = 0
_C8: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'SX_B')
 + supply_coaltype_by_node_('Inner_Mongolia',_'SX_B') >= 0
_C9: - flow_by_coaltype_('Inner_Mongolia',_'Hebei',_'IM_A')
 + supply_coaltype_by_node_('Inner_Mongolia',_'IM_A') >= 0
Bounds
supply_coaltype_by_node_('Australia',_'AUS_A') <= 1200
supply_coaltype_by_node_('Australia',_'AUS_B') <= 10000
supply_coaltype_by_node_('Australia',_'IM_A') = 0
supply_coaltype_by_node_('Australia',_'IND_A') = 0
supply_coaltype_by_node_('Australia',_'SX_A') = 0
supply_coaltype_by_node_('Australia',_'SX_B') = 0
supply_coaltype_by_node_('Beijing',_'AUS_A') = 0
supply_coaltype_by_node_('Beijing',_'AUS_B') = 0
supply_coaltype_by_node_('Beijing',_'IM_A') = 0
supply_coaltype_by_node_('Beijing',_'IND_A') = 0
supply_coaltype_by_node_('Beijing',_'SX_A') = 0
supply_coaltype_by_node_('Beijing',_'SX_B') = 0
supply_coaltype_by_node_('Caofeidian',_'AUS_A') = 0
supply_coaltype_by_node_('Caofeidian',_'AUS_B') = 0
supply_coaltype_by_node_('Caofeidian',_'IM_A') = 0
supply_coaltype_by_node_('Caofeidian',_'IND_A') = 0
supply_coaltype_by_node_('Caofeidian',_'SX_A') = 0
supply_coaltype_by_node_('Caofeidian',_'SX_B') = 0
supply_coaltype_by_node_('Hebei',_'AUS_A') = 0
supply_coaltype_by_node_('Hebei',_'AUS_B') = 0
supply_coaltype_by_node_('Hebei',_'IM_A') = 0
supply_coaltype_by_node_('Hebei',_'IND_A') = 0
supply_coaltype_by_node_('Hebei',_'SX_A') = 0
supply_coaltype_by_node_('Hebei',_'SX_B') = 0
supply_coaltype_by_node_('Indonesia',_'AUS_A') = 0
supply_coaltype_by_node_('Indonesia',_'AUS_B') = 0
supply_coaltype_by_node_('Indonesia',_'IM_A') = 0
supply_coaltype_by_node_('Indonesia',_'IND_A') <= 4000
supply_coaltype_by_node_('Indonesia',_'SX_A') = 0
supply_coaltype_by_node_('Indonesia',_'SX_B') = 0
supply_coaltype_by_node_('Inner_Mongolia',_'AUS_A') = 0
supply_coaltype_by_node_('Inner_Mongolia',_'AUS_B') = 0
supply_coaltype_by_node_('Inner_Mongolia',_'IM_A') <= 5000
supply_coaltype_by_node_('Inner_Mongolia',_'IND_A') = 0
supply_coaltype_by_node_('Inner_Mongolia',_'SX_A') = 0
supply_coaltype_by_node_('Inner_Mongolia',_'SX_B') = 0
supply_coaltype_by_node_('Shaanxi',_'AUS_A') = 0
supply_coaltype_by_node_('Shaanxi',_'AUS_B') = 0
supply_coaltype_by_node_('Shaanxi',_'IM_A') = 0
supply_coaltype_by_node_('Shaanxi',_'IND_A') = 0
supply_coaltype_by_node_('Shaanxi',_'SX_A') <= 4000
supply_coaltype_by_node_('Shaanxi',_'SX_B') <= 2000
supply_coaltype_by_node_('Tianjin',_'AUS_A') = 0
supply_coaltype_by_node_('Tianjin',_'AUS_B') = 0
supply_coaltype_by_node_('Tianjin',_'IM_A') = 0
supply_coaltype_by_node_('Tianjin',_'IND_A') = 0
supply_coaltype_by_node_('Tianjin',_'SX_A') = 0
supply_coaltype_by_node_('Tianjin',_'SX_B') = 0
End
