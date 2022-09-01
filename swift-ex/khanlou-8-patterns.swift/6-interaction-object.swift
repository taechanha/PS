class SKProfileViewController: UIViewController {
    var followUserInteraction: SKFollowUserInteraction?

    func followButtonTapped(sender: AnyObject) {
        followUserInteraction = SKFollowUserInteraction(userToFollow: user, delegate: self)
        followUserInteraction?.follow()
    }

    func interactionCompleted(interaction: SKFollowUserInteraction) {
        binding.updateView()
    }
}

class SKFollowUserInteraction: NSObject, UIAlertViewDelegate {
    let user: SKUser
    let delegate: InteractionDelegate

    init(userToFollow: SKUser, delegate: InteractionDelegate) {
        self.user = userToFollow
        self.delegate = delegate
    }

    func follow() {
        let alertView = UIAlertView(title: nil, message: "Are you sure you want to follow this user?", delegate: self, cancelButtonTitle: "Cancel", otherButtonTitles: "Follow")
        alertView.show()
    }

    func alertView(alertView: UIAlertView, clickedButtonAtIndex buttonIndex: Int) {
        if alertView.buttonTitleAtIndex(buttonIndex) == "Follow" {
            user.APIGateway.followWithCompletionBlock {
                self.delegate.interactionCompleted(self)
            }
        }
    }
}