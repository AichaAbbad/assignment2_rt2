from ipywidgets import Button, GridBox, Layout, ButtonStyle, FloatSlider

up = Button(
    description='',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='forward',
    icon='arrow-up', 
    layout=Layout(width='auto', height='50px', grid_area='up')

)

down = Button(
    description='',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='backward',
    icon='arrow-down',  
    layout=Layout(width='auto', height='50px', grid_area='down')
)

right = Button(
    description='',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip=' turn right',
    icon='arrow-right',
    layout=Layout(width='auto', height='50px', grid_area='right')

)

left = Button(
    description='',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='turn left',
    icon='arrow-left',  
    layout=Layout(width='auto', height='50px', grid_area='left')
)

stops = Button(
    description='',
    disabled=False,
    button_style='danger',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='stop',
    icon='stop',  
    layout=Layout(width='auto', height='50px', grid_area='stop')
)

start = Button(
    description='Start',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Start Simulation',
    icon='play',  
    layout=Layout(width='50%', height='80px')
)
stop = Button(
    description='Stop',
    disabled=False,
    button_style='danger',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Stop Simulation',
    icon='stop', 
    layout=Layout(width='50%', height='80px')
)

l_velSlider = FloatSlider(
    value=1.0,
    min=0.0, max=2.0, step=0.1,
    description='Linear Velocity: ')

a_velSlider = FloatSlider(  value=1.0,
    min=0.0, max=2.0, step=0.1,
    description='Angular Velocity: ')

control_pad = GridBox(children=[up,down,left,right, stops],
        layout=Layout(
            width='100%',
            grid_template_rows='auto auto auto auto',
            grid_template_columns='16.5% 16.5% 16.5% 16.5% 16.5% 16.5%',
            grid_template_areas='''
            ". up . . . . "
            " left . right . stop ."
            " . down . . . . "
            ''')
       )