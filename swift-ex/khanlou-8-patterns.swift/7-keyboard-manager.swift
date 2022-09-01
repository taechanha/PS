class SKNewPostKeyboardManager: NSObject {
    var tableView: UITableView
    var oldBottomContentInset: CGFloat = 0.0

    init(tableView: UITableView) {
        self.tableView = tableView
    }

    func beginObservingKeyboard() {
        NSNotificationCenter.defaultCenter().addObserver(self, selector: "keyboardDidHide:", name: UIKeyboardDidHideNotification, object: nil)
        NSNotificationCenter.defaultCenter().addObserver(self, selector: "keyboardWillShow:", name: UIKeyboardWillShowNotification, object: nil)
    }

    func endObservingKeyboard() {
        NSNotificationCenter.defaultCenter().removeObserver(self, name: UIKeyboardDidHideNotification, object: nil)
        NSNotificationCenter.defaultCenter().removeObserver(self, name: UIKeyboardWillShowNotification, object: nil)
    }

    func keyboardWillShow(note: NSNotification) {
        let keyboardRect = note.userInfo![UIKeyboardFrameEndUserInfoKey]!.CGRectValue()

        let contentInsets = UIEdgeInsetsMake(self.tableView.contentInset.top, 0.0, CGRectGetHeight(keyboardRect), 0.0)
        self.tableView.contentInset = contentInsets
        self.tableView.scrollIndicatorInsets = contentInsets
    }

    func keyboardDidHide(note: NSNotification) {
        let contentInset = UIEdgeInsetsMake(self.tableView.contentInset.top, 0.0, self.oldBottomContentInset, 0.0)
        self.tableView.contentInset = contentInset
        self.tableView.scrollIndicatorInsets = contentInset
    }
}