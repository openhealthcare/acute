//
// This is step 1 of The "Next step" exit flow controller for OPAL Acute
//
controllers.controller(
    'AcuteTakeDischargeCtrl', 
    function(
        $scope, $modalInstance, $modal, $rootScope, $q,
        growl,
        options, episode, tags
    ){
        $scope.episode = episode;
        $scope.state = 'initial';
        $scope.meta = {};

        $scope.discharge = function(){
            var deferred = $q.defer();
            $rootScope.open_modal(
                'DischargeEpisodeCtrl',
                '/templates/modals/discharge_episode.html/',
                'md',
                {episode: episode, options: options, tags: tags}
            ).result.then(
                function(r){ deferred.resolve('discharged') },
                function(r){ deferred.reject('discharged') }                    
            );
            $modalInstance.close(deferred.promise);
        };
        
        $scope.move_to_aau = function(){
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.take = false;
            tagging.aau = true;
            $scope.episode.tagging[0].save(tagging).then(function(){
                growl.success('Moved to AAU');
                $modalInstance.close('discharged');
            });
        };
        
        $scope.refer_to_team = function(){
            $scope.state = 'referring';
        };

        $scope.refer = function(){
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.take = false;
            tagging.aau = false;
            tagging[$scope.meta.target_team] = true;
            $scope.episode.tagging[0].save(tagging).then(function(){
                growl.success('Referred successfully');
                $modalInstance.close('discharged');
            });
            
        }

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
            $modalInstance.close('cancel');
        };

    }
)
