class GetData:

    def __init__(self):




        def dicto_parser():
            diction = {}
            keys = []
            values = []

            with open('nota.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for ln in lines:
                key, value = ln.strip('\n').split('=')
                diction[key] = value

            return diction

        self.name_col_x_tab0 = dicto_parser()['name_col_x_tab0']
        self.name_col_y_tab_0 = dicto_parser()['name_col_y_tab_0']
        self.name_serial_var = dicto_parser()['name_serial_var']
        self.polynom_degree = dicto_parser()['polynom_degree']
        self.step_value = dicto_parser()['step_value']
        self.scope_down_entry_tab0 = dicto_parser()['scope_down_entry_tab0']
        self.scope_up_entry_tab0 = dicto_parser()['scope_up_entry_tab0']
        self.formula_x = dicto_parser()['formula_x']
        self.formula_y = dicto_parser()['formula_y']
        self.time_tag = dicto_parser()['time_tag']
        self.column_x_tag_tab1 = dicto_parser()['column_x_tag_tab1']
        self.column_y_tag_tab1 = dicto_parser()['column_y_tag_tab1']
        self.down_scope_tab1 = dicto_parser()['down_scope_tab1']
        self.up_scope_tab_1 = dicto_parser()['up_scope_tab_1']
        self.scale_time_chart = dicto_parser()['scale_time_chart']
        self.name_of_chart = dicto_parser()['name_of_chart']
        self.name_of_X_axis_tab3 = dicto_parser()['name_of_X_axis_tab3']
        self.unit_of_X_axis_tab3 = dicto_parser()['unit_of_X_axis_tab3']
        self.name_of_Y_axis_tab3 = dicto_parser()['name_of_Y_axis_tab3']
        self.unit_of_Y_axis_tab3 = dicto_parser()['unit_of_Y_axis_tab3']
        self.scope_down_x_background_entry_tab0 = dicto_parser()['scope_down_x_background_entry_tab0']
        self.scope_up_x_background_entry_tab0 = dicto_parser()['scope_up_x_background_entry_tab0']
        self.scope_down_y_background_entry_tab0 = dicto_parser()['scope_down_y_background_entry_tab0']
        self.scope_up_y_background_entry_tab0 = dicto_parser()['scope_up_y_background_entry_tab0']
        self.trasparency_picture = dicto_parser()['trasparency_picture']
        #
    #
