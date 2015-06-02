"""
Define the patient flows for our system
"""
acute_flow = {
     'enter': {
         'controller': 'HospitalNumberCtrl',
         'template'  : '/templates/modals/hospital_number.html/'
     },
     'exit': {
         'controller': 'AcuteTakeDischargeCtrl',
         'template'  : '/templates/modals/acute_take_discharge_modal.html'
     }
}

flows = {
    'default': {
        'enter': {
            'controller': 'HospitalNumberCtrl',
            'template'  : '/templates/modals/hospital_number.html/'
        },
        'exit': {
            'controller': 'DischargeEpisodeCtrl',
            'template'  : '/templates/modals/discharge_episode.html/'
        }
    },
    'take': { 'default': acute_flow },
    'aau': { 'default': acute_flow }
}
