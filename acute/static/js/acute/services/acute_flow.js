//
// Service for locating controllers and templates for
//
angular.module('opal.services').factory('AcuteFlow', function($routeParams){
    "use strict";

    var base = {
        'enter': {
            'controller': 'HospitalNumberCtrl',
            'template'  : '/templates/modals/hospital_number.html/'
        },
        'exit': {
            'controller': 'DischargeEpisodeCtrl',
            'template'  : '/templates/modals/discharge_episode.html/'
        }
    }

    var acute_flow = {
        'enter': {
            'controller': 'HospitalNumberCtrl',
            'template'  : '/templates/modals/hospital_number.html/'
        },
        'exit': {
            'controller': 'AcuteTakeDischargeCtrl',
            'template'  : '/templates/modals/acute_take_discharge_modal.html'
        }
    }


    var Flow = {
        enter: function(){
            var target = base;
            if($routeParams.slug){
                if($routeParams.slug == 'take' || $routeParams.slug == 'aau'){
                    target = acute_flow;
                }
            }
            return target.enter
        },
        exit: function(episode){
            var target = base;
            if($routeParams.slug){
                if($routeParams.slug == 'take' || $routeParams.slug == 'aau'){
                    target = acute_flow;
                }
            }
            return target.exit
        }
    }
    return Flow
})
