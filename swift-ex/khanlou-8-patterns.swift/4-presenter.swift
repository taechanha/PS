class SKUserPresenter {
    let user: SKUser
    init(user: SKUser) {
        self.user = user
    }
    var name: String {
        return user.name
    }
    var followerCountString: String {
        if user.followerCount == 0 {
            return ""
        }
        return NSNumberFormatter.localizedStringFromNumber(user.followerCount, numberStyle: .DecimalStyle) + " followers"
    }
    var followersString: String {
        var followersString = "Followed by "
        followersString += TTTArrayFormatter.arrayFormatter().stringFromArray(user.topFollowers.map { $0.name })
        return followersString
    }
}
