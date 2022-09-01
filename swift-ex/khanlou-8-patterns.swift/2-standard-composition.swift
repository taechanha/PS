var headerViewController: SKHeaderViewController!
var gridViewController: SKGridViewController!

override func viewDidLoad() {
    super.viewDidLoad()

    headerViewController = SKHeaderViewController()
    addChildViewController(headerViewController)
    headerViewController.didMoveToParentViewController(self)
    view.addSubview(headerViewController.view)

    gridViewController = SKGridViewController()
    addChildViewController(gridViewController)
    gridViewController.didMoveToParentViewController(self)
    view.addSubview(gridViewController.view)
}

override func viewDidLayoutSubviews() {
    super.viewDidLayoutSubviews()

    var workingRect = view.bounds
    var headerRect = CGRectZero, gridRect = CGRectZero
    CGRectDivide(workingRect, &headerRect, &gridRect, 44, CGRectMinYEdge)

    headerViewController.view.frame = headerRect
    gridViewController.view.frame = gridRect
}
