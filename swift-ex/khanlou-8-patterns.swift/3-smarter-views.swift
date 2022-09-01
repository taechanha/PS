class SKProfileViewController: UIViewController {
    override func loadView() {
        self.view = SKProfileView()
    }
}

class SKProfileView: UIView {
    lazy var nameLabel: UILabel = {
        let nameLabel = UILabel()
        //configure font, color, etc
        self.addSubview(nameLabel)
        return nameLabel
    }()
    
    lazy var avatarImageView: UIImageView = {
        let avatarImageView = UIImageView()
        self.addSubview(avatarImageView)
        return avatarImageView
    }()
    
    override func layoutSubviews() {
        //perform layout
    }
}

