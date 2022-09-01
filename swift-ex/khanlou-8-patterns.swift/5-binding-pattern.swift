class SKProfileBinding: NSObject {
    let view: SKProfileView
    let presenter: SKUserPresenter
    
    init(view: SKProfileView, presenter: SKUserPresenter) {
        self.view = view
        self.presenter = presenter
    }
    
    func bindings() -> [String: String] {
        return [
            "name": "nameLabel.text",
            "followerCountString": "followerCountLabel.text",
        ]
    }
    
    func updateView() {
        for (presenterKeyPath, viewKeyPath) in bindings() {
            let newValue = self.presenter.valueForKeyPath(presenterKeyPath)
            self.view.setValue(newValue, forKeyPath: viewKeyPath)
        }
    }
}
