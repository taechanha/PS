func beginPhotoCreationProcess() {  
	let coordinator = PhotoCreationCoordinator(
                        rootViewController: rootViewController, 
                        delegate: self)  
	childCoordinators.append(coordinator)  
	coordinator.beginPhotoCreationProcess()  
}
	
func photoCreationCompletedSuccessfully(_ coordinator: PhotoCreationCoordinator) {  
	childCoordinators.remove(coordinator)  
}
	
func photoCreationCanceled(_ coordinator: PhotoCreationCoordinator) {  
	childCoordinators.remove(coordinator)  
}  
