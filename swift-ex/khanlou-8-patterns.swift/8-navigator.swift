protocol SKUserNavigator {
    func navigateToFollowersForUser(user: SKUser)
}

class SKiPhoneUserNavigator: SKUserNavigator {
    let navigationController: UINavigationController
    
    init(navigationController: UINavigationController) {
        self.navigationController = navigationController
    }
    
    func navigateToFollowersForUser(user: SKUser) {
        let followerList = SKFollowerListViewController(user: user)
        self.navigationController.pushViewController(followerList, animated: true)
    }
}

class SKiPadUserNavigator: SKUserNavigator {
    let userViewController: SKUserViewController
    
    init(userViewController: SKUserViewController) {
        self.userViewController = userViewController
    }
    
    func navigateToFollowersForUser(user: SKUser) {
        let followerList = SKFollowerListViewController(user: user)
        self.userViewController.supplementalViewController = followerList
    }
}
